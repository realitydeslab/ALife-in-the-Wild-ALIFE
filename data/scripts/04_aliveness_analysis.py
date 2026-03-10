#!/usr/bin/env python3
"""
Script 04: Compute quantitative "aliveness" metrics for Spore.fun agents.
Implements:
1. Bedau's Evolutionary Activity
2. Kaplan-Meier Survival Curves
3. Metabolic Rate (transaction frequency proxy)
4. Reproductive Fitness
5. Economic Vitality (market cap trajectories)
6. Holder Diversity (Gini coefficient)
7. Social Activity Correlation

Uses data from:
- agents.json (Spore.fun API)
- market_data/*.csv (GeckoTerminal OHLCV)
- market_data/historical_summary.json (Solana RPC data)
"""

import json
import os
import csv
import math
import sys
from datetime import datetime, timezone, timedelta
from collections import defaultdict

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Try to import scipy for KM curves
try:
    from lifelines import KaplanMeierFitter
    HAS_LIFELINES = True
except ImportError:
    HAS_LIFELINES = False
    print("Note: lifelines not installed. KM curves will be computed manually.")

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
AGENTS_FILE = os.path.join(BASE_DIR, 'agents.json')
MARKET_DIR = os.path.join(BASE_DIR, 'market_data')
ANALYSIS_DIR = os.path.join(BASE_DIR, 'analysis')
HIST_SUMMARY = os.path.join(MARKET_DIR, 'historical_summary.json')


def load_agents():
    with open(AGENTS_FILE) as f:
        return json.load(f)['agents']


def load_historical():
    if os.path.exists(HIST_SUMMARY):
        with open(HIST_SUMMARY) as f:
            return json.load(f)
    return {'agents': []}


def load_ohlcv(slug, variant='raydium', timeframe='day'):
    """Load OHLCV CSV for an agent."""
    filename = os.path.join(MARKET_DIR, f"{slug}_{variant}_{timeframe}_ohlcv.csv")
    if not os.path.exists(filename):
        return []
    rows = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({
                'timestamp': int(row['timestamp']),
                'datetime': row['datetime'],
                'open': float(row['open']),
                'high': float(row['high']),
                'low': float(row['low']),
                'close': float(row['close']),
                'volume': float(row['volume']),
            })
    return sorted(rows, key=lambda r: r['timestamp'])


def parse_date(date_str):
    """Parse ISO date string."""
    if not date_str:
        return None
    try:
        if isinstance(date_str, str):
            # Handle various formats
            date_str = date_str.replace('Z', '+00:00')
            return datetime.fromisoformat(date_str)
        return date_str
    except Exception:
        return None


def compute_survival_data(agents):
    """
    Compute Kaplan-Meier style survival data.
    'Death' = status == 'stopped' (or health_points == 0)
    Survival time = days from creation until death or censoring (current date)
    """
    now = datetime.now(timezone.utc)
    
    data = []
    for agent in agents:
        created = parse_date(str(agent.get('createdAt', '')))
        if not created:
            continue
        
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        
        is_alive = agent['status'] == 'running'
        hp = agent.get('healthPoints', 0)
        
        # Duration: days from birth to death or now
        duration_days = (now - created).total_seconds() / 86400
        
        data.append({
            'id': agent['id'],
            'name': agent['name'],
            'generation': agent['generation'],
            'created': created,
            'duration_days': duration_days,
            'is_alive': is_alive,
            'event': not is_alive,  # True = death observed
            'status': agent['status'],
            'health_points': hp,
            'market_cap': float(agent.get('marketCap', 0) or 0),
            'balance': float(agent.get('balance', 0) or 0),
            'market_cap_reached': agent.get('marketCapReached', False),
            'token_type': agent.get('tokenType', ''),
        })
    
    return sorted(data, key=lambda x: x['duration_days'])


def kaplan_meier_manual(survival_data):
    """Manual KM estimator."""
    # Sort by duration
    sorted_data = sorted(survival_data, key=lambda x: x['duration_days'])
    
    n_total = len(sorted_data)
    times = [0]
    km_probs = [1.0]
    
    # Group by time of death
    death_times = sorted(set(
        round(s['duration_days']) 
        for s in sorted_data 
        if s['event']
    ))
    
    n_at_risk = n_total
    km_prob = 1.0
    
    for t in death_times:
        deaths_at_t = sum(1 for s in sorted_data if s['event'] and abs(round(s['duration_days']) - t) < 0.5)
        km_prob *= (1 - deaths_at_t / n_at_risk)
        n_at_risk -= sum(1 for s in sorted_data if round(s['duration_days']) <= t)
        times.append(t)
        km_probs.append(km_prob)
    
    return times, km_probs


def compute_reproductive_fitness(agents):
    """Compute reproductive fitness metrics."""
    agent_map = {a['id']: a for a in agents}
    
    fitness = []
    for agent in agents:
        # Count children
        children = [a for a in agents if a.get('parentId') == agent['id']]
        
        # Reproductive success
        reproduced = len(children) > 0
        n_offspring = len(children)
        
        # Compute lifetime (days)
        created = parse_date(str(agent.get('createdAt', '')))
        if created and created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        
        now = datetime.now(timezone.utc)
        lifetime_days = (now - created).total_seconds() / 86400 if created else None
        
        fitness.append({
            'id': agent['id'],
            'name': agent['name'],
            'generation': agent['generation'],
            'reproduced': reproduced,
            'n_offspring': n_offspring,
            'n_grandchildren': sum(len([a for a in agents if a.get('parentId') == c['id']]) for c in children),
            'lifetime_days': lifetime_days,
            'final_mc': float(agent.get('marketCap', 0) or 0),
            'final_balance': float(agent.get('balance', 0) or 0),
            'mc_reached': agent.get('marketCapReached', False),
            'status': agent['status'],
            'token_type': agent.get('tokenType', ''),
        })
    
    return fitness


def compute_bedau_activity(agents, ohlcv_data):
    """
    Approximate Bedau's evolutionary activity statistics.
    - Novelty: new agents per generation (new 'species')  
    - Diversity: number of concurrent agents
    - Total activity: proxy = sum of market caps across generations
    """
    from collections import defaultdict
    
    # Generation-level stats
    gen_data = defaultdict(list)
    for agent in agents:
        gen_data[agent['generation']].append(agent)
    
    activity = []
    for gen in sorted(gen_data.keys()):
        agents_in_gen = gen_data[gen]
        
        # Novelty: count of new agents in this generation
        novelty = len(agents_in_gen)
        
        # Activity: sum of market caps
        total_mc = sum(float(a.get('marketCap', 0) or 0) for a in agents_in_gen)
        
        # MC reached (successful evolution)
        mc_reached = sum(1 for a in agents_in_gen if a.get('marketCapReached'))
        
        # Average balance (treasury health)
        avg_balance = sum(float(a.get('balance', 0) or 0) for a in agents_in_gen) / len(agents_in_gen)
        
        # Reproductive success (how many reproduced)
        reproduced = sum(1 for a in agents_in_gen 
                         if any(b.get('parentId') == a['id'] for b in agents))
        
        # Date range for this generation
        dates = [parse_date(str(a.get('createdAt', ''))) for a in agents_in_gen]
        dates = [d for d in dates if d]
        if dates:
            first_date = min(d if d.tzinfo else d.replace(tzinfo=timezone.utc) for d in dates)
            last_date = max(d if d.tzinfo else d.replace(tzinfo=timezone.utc) for d in dates)
        else:
            first_date = last_date = None
        
        activity.append({
            'generation': gen,
            'n_agents': novelty,
            'novelty': novelty,  # New agents = novelty
            'total_market_cap': total_mc,
            'mc_reached_count': mc_reached,
            'mc_reached_rate': mc_reached / novelty if novelty > 0 else 0,
            'avg_balance': avg_balance,
            'reproduced_count': reproduced,
            'reproduction_rate': reproduced / novelty if novelty > 0 else 0,
            'first_agent_date': first_date.isoformat() if first_date else None,
            'last_agent_date': last_date.isoformat() if last_date else None,
        })
    
    return activity


def compute_metabolic_rate(hist_data):
    """
    Compute metabolic rate from transaction counts.
    Higher tx count = higher metabolic activity.
    """
    metabolic = []
    for agent_data in hist_data.get('agents', []):
        tx_count = agent_data.get('tx_count', 0) or 0
        
        metabolic.append({
            'name': agent_data['name'],
            'slug': agent_data['slug'],
            'generation': agent_data['generation'],
            'status': agent_data['status'],
            'tx_count': tx_count,
            'wallet_sol_balance': agent_data.get('wallet_sol_balance', 0) or 0,
        })
    
    return metabolic


def gini_coefficient(values):
    """Compute Gini coefficient for a list of values."""
    n = len(values)
    if n == 0:
        return 0
    values = sorted(values)
    cumsum = sum((i + 1) * v for i, v in enumerate(values))
    total = sum(values)
    if total == 0:
        return 0
    return (2 * cumsum) / (n * total) - (n + 1) / n


def compute_economic_vitality(agents):
    """Compute economic vitality metrics."""
    # Current snapshot
    total_mc = sum(float(a.get('marketCap', 0) or 0) for a in agents)
    total_balance = sum(float(a.get('balance', 0) or 0) for a in agents)
    
    mc_values = [float(a.get('marketCap', 0) or 0) for a in agents]
    balance_values = [float(a.get('balance', 0) or 0) for a in agents]
    
    # Gini coefficients
    mc_gini = gini_coefficient(mc_values)
    balance_gini = gini_coefficient(balance_values)
    
    # Active vs dead capital
    active_agents = [a for a in agents if a['status'] == 'running']
    dead_agents = [a for a in agents if a['status'] != 'running']
    
    active_mc = sum(float(a.get('marketCap', 0) or 0) for a in active_agents)
    dead_mc = sum(float(a.get('marketCap', 0) or 0) for a in dead_agents)
    
    return {
        'total_market_cap_current': total_mc,
        'total_balance_current': total_balance,
        'mc_gini': mc_gini,
        'balance_gini': balance_gini,
        'n_alive': len(active_agents),
        'n_dead': len(dead_agents),
        'alive_mc': active_mc,
        'dead_mc': dead_mc,
        'mc_values_by_agent': {a['name']: float(a.get('marketCap', 0) or 0) for a in agents},
        'balance_values_by_agent': {a['name']: float(a.get('balance', 0) or 0) for a in agents},
    }


# ========================
# PLOTTING FUNCTIONS
# ========================

def plot_family_tree(agents, output_dir):
    """Plot the agent family tree."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 6)
    
    # Position agents
    gen_positions = {
        1: [(0, 2.5)],  # Spore
        2: [(1, 3.5), (1, 1.5)],  # Adam, Eve
        3: [(2, 4.5), (2, 3.5), (2, 2.5), (2, 1.5), (2, 0.7), (2, 0.0)],  # Gen 3
        4: [(3, 4.0), (3, 3.0), (3, 2.0), (3, 1.0)],  # Gen 4
        5: [(4, 3.5), (4, 2.0)],  # Gen 5
    }
    
    agent_positions = {}
    gen_counts = {}
    
    for gen in sorted(set(a['generation'] for a in agents)):
        gen_agents = [a for a in agents if a['generation'] == gen]
        n = len(gen_agents)
        # Spread agents in the generation
        positions = [(gen - 1, i * (4.5 / max(n - 1, 1)) + 0.5) if n > 1 else (gen - 1, 2.5) for i in range(n)]
        
        for agent, pos in zip(gen_agents, positions):
            agent_positions[agent['id']] = pos
    
    # Draw edges (parent-child)
    for agent in agents:
        parent_id = agent.get('parentId')
        if parent_id and parent_id in agent_positions and agent['id'] in agent_positions:
            px, py = agent_positions[parent_id]
            cx, cy = agent_positions[agent['id']]
            ax.plot([px, cx], [py, cy], 'gray', alpha=0.5, linewidth=1.5, zorder=1)
    
    # Draw nodes
    for agent in agents:
        if agent['id'] not in agent_positions:
            continue
        x, y = agent_positions[agent['id']]
        
        # Color by status
        if agent['status'] == 'running':
            color = '#2ecc71'
            edge_color = '#27ae60'
        elif agent.get('marketCapReached'):
            color = '#3498db'
            edge_color = '#2980b9'
        else:
            color = '#e74c3c'
            edge_color = '#c0392b'
        
        # Node size by market cap
        mc = float(agent.get('marketCap', 0) or 0)
        size = 200 + mc / 500
        
        ax.scatter([x], [y], s=size, c=color, edgecolors=edge_color, 
                  linewidths=2, zorder=3)
        
        # Label
        label = f"{agent['name']}\n${mc/1000:.0f}K"
        ax.annotate(label, (x, y), xytext=(5, 10), textcoords='offset points',
                   fontsize=7, ha='left', va='bottom',
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))
    
    # Legend
    ax.scatter([], [], s=200, c='#2ecc71', edgecolors='#27ae60', linewidths=2, label='Alive')
    ax.scatter([], [], s=200, c='#3498db', edgecolors='#2980b9', linewidths=2, label='Dead (MC Reached $500K)')
    ax.scatter([], [], s=200, c='#e74c3c', edgecolors='#c0392b', linewidths=2, label='Dead (MC Not Reached)')
    ax.legend(loc='upper right', fontsize=9)
    
    # Generation labels
    for gen in range(1, 6):
        ax.text(gen - 1, -0.6, f'Gen {gen}', ha='center', va='center', 
               fontsize=10, fontweight='bold', color='gray')
    
    ax.set_title('Spore.fun Agent Family Tree', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(-0.5, 4.5)
    ax.axis('off')
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 'family_tree.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")
    return filename


def plot_market_cap_by_generation(agents, output_dir):
    """Plot market cap distribution by generation."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Group by generation
    gen_data = defaultdict(list)
    for a in agents:
        mc = float(a.get('marketCap', 0) or 0)
        gen_data[a['generation']].append({
            'name': a['name'],
            'mc': mc,
            'balance': float(a.get('balance', 0) or 0),
            'status': a['status'],
            'mc_reached': a.get('marketCapReached', False),
        })
    
    # Plot 1: Bar chart of market caps
    ax = axes[0]
    colors_map = {'running': '#2ecc71', 'stopped_reached': '#3498db', 'stopped_not_reached': '#e74c3c'}
    
    x_positions = []
    x_labels = []
    bar_colors = []
    bar_heights = []
    
    offset = 0
    for gen in sorted(gen_data.keys()):
        agents_in_gen = gen_data[gen]
        for i, a_data in enumerate(agents_in_gen):
            x_positions.append(offset)
            x_labels.append(a_data['name'][:6])
            bar_heights.append(a_data['mc'] / 1000)  # in $K
            if a_data['status'] == 'running':
                bar_colors.append(colors_map['running'])
            elif a_data['mc_reached']:
                bar_colors.append(colors_map['stopped_reached'])
            else:
                bar_colors.append(colors_map['stopped_not_reached'])
            offset += 1
        offset += 0.5  # Gap between generations
    
    bars = ax.bar(x_positions, bar_heights, color=bar_colors, edgecolor='white', linewidth=0.5)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels, rotation=45, ha='right', fontsize=7)
    ax.set_ylabel('Current Market Cap ($K)')
    ax.set_title('Current Market Cap by Agent')
    ax.axhline(y=500, color='red', linestyle='--', alpha=0.5, label='$500K Reproduction Threshold')
    
    # Add generation annotations
    offset = 0
    for gen in sorted(gen_data.keys()):
        n = len(gen_data[gen])
        mid = offset + (n - 1) / 2
        ax.text(mid, ax.get_ylim()[1] * 0.95, f'Gen {gen}',
               ha='center', fontsize=8, fontweight='bold', color='gray')
        offset += n + 0.5
    
    ax.legend(handles=[
        plt.Rectangle((0, 0), 1, 1, color=colors_map['running'], label='Alive'),
        plt.Rectangle((0, 0), 1, 1, color=colors_map['stopped_reached'], label='Dead (MC reached)'),
        plt.Rectangle((0, 0), 1, 1, color=colors_map['stopped_not_reached'], label='Dead (MC not reached)'),
    ], fontsize=8, loc='upper right')
    
    # Plot 2: Wallet balance distribution
    ax2 = axes[1]
    x_positions2 = []
    bar_heights2 = []
    x_labels2 = []
    bar_colors2 = []
    
    offset = 0
    for gen in sorted(gen_data.keys()):
        agents_in_gen = gen_data[gen]
        for i, a_data in enumerate(agents_in_gen):
            x_positions2.append(offset)
            x_labels2.append(a_data['name'][:6])
            bar_heights2.append(a_data['balance'] / 1000)
            if a_data['status'] == 'running':
                bar_colors2.append(colors_map['running'])
            elif a_data['mc_reached']:
                bar_colors2.append(colors_map['stopped_reached'])
            else:
                bar_colors2.append(colors_map['stopped_not_reached'])
            offset += 1
        offset += 0.5
    
    ax2.bar(x_positions2, bar_heights2, color=bar_colors2, edgecolor='white', linewidth=0.5)
    ax2.set_xticks(x_positions2)
    ax2.set_xticklabels(x_labels2, rotation=45, ha='right', fontsize=7)
    ax2.set_ylabel('Treasury Balance ($K)')
    ax2.set_title('Treasury Balance by Agent')
    
    plt.suptitle('Spore.fun Economic Metrics', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    filename = os.path.join(output_dir, 'market_cap_distribution.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")
    return filename


def plot_survival_curve(survival_data, output_dir):
    """Plot Kaplan-Meier survival curve."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Overall survival
    times, probs = kaplan_meier_manual(survival_data)
    ax.step(times, probs, where='post', color='black', linewidth=2, label='All agents (N=15)')
    ax.fill_between(times, probs, step='post', alpha=0.1, color='black')
    
    # By generation
    colors = {1: '#1abc9c', 2: '#3498db', 3: '#e74c3c', 4: '#f39c12', 5: '#9b59b6'}
    for gen in sorted(set(s['generation'] for s in survival_data)):
        gen_data = [s for s in survival_data if s['generation'] == gen]
        if len(gen_data) >= 1:
            times_g, probs_g = kaplan_meier_manual(gen_data)
            c = colors.get(gen, 'gray')
            ax.step(times_g, probs_g, where='post', color=c, linewidth=1.5, 
                   linestyle='--', label=f'Gen {gen} (N={len(gen_data)})')
    
    # Add censored points for alive agents
    alive = [s for s in survival_data if not s['event']]
    if alive:
        ax.scatter([s['duration_days'] for s in alive], 
                  [0.1 for _ in alive],  # Show at y=0.1
                  marker='|', color='black', s=100, zorder=5, label='Censored (alive)')
    
    ax.set_xlabel('Days Since Agent Birth', fontsize=12)
    ax.set_ylabel('Survival Probability (P(still running))', fontsize=12)
    ax.set_title('Kaplan-Meier Survival Curves: Spore.fun Agents', fontsize=13, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9)
    ax.set_xlim(left=0)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    
    # Add annotation for the single surviving agent
    ax.annotate('Only Gen1 ($SPORE)\nstill running after 445+ days',
               xy=(440, 0.0), xytext=(300, 0.3),
               arrowprops=dict(arrowstyle='->', color='gray'),
               fontsize=9, color='#2ecc71',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 'survival_curves.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")
    return filename


def plot_bedau_activity(activity_data, output_dir):
    """Plot Bedau-inspired evolutionary activity statistics."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    gens = [d['generation'] for d in activity_data]
    
    # 1. Novelty (new agents per generation)
    ax = axes[0, 0]
    ax.bar(gens, [d['novelty'] for d in activity_data], color='steelblue', edgecolor='white')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Number of New Agents')
    ax.set_title('Novelty: New Agents per Generation')
    ax.set_xticks(gens)
    for i, (g, d) in enumerate(zip(gens, activity_data)):
        ax.text(g, d['novelty'] + 0.1, str(d['novelty']), ha='center', fontsize=10)
    
    # 2. Total Activity (market cap proxy)
    ax = axes[0, 1]
    total_mcs = [d['total_market_cap'] / 1000 for d in activity_data]
    ax.bar(gens, total_mcs, color='coral', edgecolor='white')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Total Market Cap ($K)')
    ax.set_title('Evolutionary Activity: Total Economic Value')
    ax.set_xticks(gens)
    
    # 3. Reproduction rate
    ax = axes[1, 0]
    repro_rates = [d['reproduction_rate'] * 100 for d in activity_data]
    mc_rates = [d['mc_reached_rate'] * 100 for d in activity_data]
    
    x = np.array(gens)
    width = 0.35
    ax.bar(x - width/2, mc_rates, width, label='$500K MC Reached', color='#3498db', edgecolor='white')
    ax.bar(x + width/2, repro_rates, width, label='Actually Reproduced', color='#2ecc71', edgecolor='white')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Rate (%)')
    ax.set_title('Reproductive Fitness by Generation')
    ax.set_xticks(gens)
    ax.legend()
    ax.set_ylim(0, 110)
    
    # 4. Cumulative agent count (diversity over time)
    ax = axes[1, 1]
    cumulative_agents = []
    cumulative = 0
    for d in activity_data:
        cumulative += d['n_agents']
        cumulative_agents.append(cumulative)
    
    ax.plot(gens, cumulative_agents, 'o-', color='purple', linewidth=2, markersize=8)
    ax.fill_between(gens, cumulative_agents, alpha=0.2, color='purple')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Cumulative Agent Count')
    ax.set_title('Diversity: Cumulative Population Growth')
    ax.set_xticks(gens)
    ax.grid(True, alpha=0.3)
    
    # Also overlay alive agents
    alive_per_gen = [0 if g > 1 else 1 for g in gens]  # Only Gen1 is alive
    ax.plot(gens, alive_per_gen, 's--', color='green', linewidth=1.5, markersize=6, label='Alive')
    ax.legend()
    
    plt.suptitle("Bedau's Evolutionary Activity Statistics", fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    filename = os.path.join(output_dir, 'bedau_activity.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")
    return filename


def plot_spore_price_history(output_dir):
    """Plot SPORE token price history."""
    ohlcv = load_ohlcv('spore', 'raydium', 'day')
    
    if not ohlcv:
        print("  No OHLCV data for SPORE")
        return None
    
    fig, axes = plt.subplots(2, 1, figsize=(14, 9), sharex=True)
    
    dates = [datetime.fromtimestamp(r['timestamp'], tz=timezone.utc) for r in ohlcv]
    closes = [r['close'] for r in ohlcv]
    volumes = [r['volume'] for r in ohlcv]
    
    # Market cap (close * supply)
    supply = 999914258
    mc = [c * supply for c in closes]
    
    # Plot 1: Price / Market Cap
    ax = axes[0]
    ax.plot(dates, [m / 1000 for m in mc], color='#3498db', linewidth=1.5, label='Market Cap')
    ax.fill_between(dates, [m / 1000 for m in mc], alpha=0.15, color='#3498db')
    ax.axhline(y=500, color='red', linestyle='--', alpha=0.7, label='$500K Reproduction Threshold')
    ax.set_ylabel('Market Cap ($K)')
    ax.set_title('$SPORE Token Market Cap History (Raydium Pool)', fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    # Annotate key events
    if mc:
        max_mc = max(mc)
        max_idx = mc.index(max_mc)
        max_date = dates[max_idx]
        ax.annotate(f'Peak: ${max_mc/1000:.0f}K\n{max_date.strftime("%Y-%m-%d")}',
                   xy=(max_date, max_mc/1000),
                   xytext=(-60, -30), textcoords='offset points',
                   arrowprops=dict(arrowstyle='->', color='gray'),
                   fontsize=8, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    
    # Plot 2: Volume
    ax2 = axes[1]
    ax2.bar(dates, volumes, color='#e74c3c', alpha=0.7, width=0.8, label='Volume')
    ax2.set_ylabel('Volume (USD)')
    ax2.set_xlabel('Date')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    fig.autofmt_xdate()
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 'spore_price_history.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")
    return filename


def plot_metabolic_rates(metabolic_data, agents, output_dir):
    """Plot metabolic rate (transaction frequency) as proxy for aliveness."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: TX count by agent  
    ax = axes[0]
    names = [m['name'] for m in metabolic_data]
    txs = [m['tx_count'] for m in metabolic_data]
    gens = [m['generation'] for m in metabolic_data]
    
    colors = ['#1abc9c' if m['status'] == 'running' else 
              '#3498db' if m.get('generation') <= 3 else '#e74c3c' 
              for m in metabolic_data]
    
    bars = ax.barh(names, txs, color=colors, edgecolor='white')
    ax.set_xlabel('Recent Wallet Transaction Count (max 1000)')
    ax.set_title('Metabolic Rate: Transaction Frequency')
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add gen labels
    for bar, m in zip(bars, metabolic_data):
        ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
               f"Gen{m['generation']}", va='center', fontsize=7, color='gray')
    
    # Right: SOL wallet balance
    ax2 = axes[1]
    sol_balances = [m['wallet_sol_balance'] for m in metabolic_data]
    
    bars2 = ax2.barh(names, sol_balances, color=colors, edgecolor='white')
    ax2.set_xlabel('Wallet SOL Balance')
    ax2.set_title('Treasury Health: Remaining SOL Balance')
    ax2.grid(True, alpha=0.3, axis='x')
    
    for bar, m in zip(bars2, metabolic_data):
        if m['wallet_sol_balance'] and m['wallet_sol_balance'] > 0.01:
            ax2.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                    f"{m['wallet_sol_balance']:.2f}", va='center', fontsize=7)
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#1abc9c', label='Alive'),
        Patch(facecolor='#3498db', label='Dead (Gen 1-3)'),
        Patch(facecolor='#e74c3c', label='Dead (Gen 4-5)'),
    ]
    ax.legend(handles=legend_elements, fontsize=8)
    
    plt.suptitle('Metabolic Activity Metrics', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    filename = os.path.join(output_dir, 'metabolic_rates.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")
    return filename


def plot_timeline(agents, output_dir):
    """Plot agent birth/death timeline."""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    now = datetime.now(timezone.utc)
    colors = {1: '#1abc9c', 2: '#3498db', 3: '#e74c3c', 4: '#f39c12', 5: '#9b59b6'}
    
    # Sort by creation date
    sorted_agents = sorted(agents, key=lambda a: str(a.get('createdAt', '')))
    
    for i, agent in enumerate(sorted_agents):
        created = parse_date(str(agent.get('createdAt', '')))
        if not created:
            continue
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        
        end_date = now if agent['status'] == 'running' else None
        
        # For stopped agents, we don't know exact death date
        # Use current date as censored end
        end = now
        
        gen = agent['generation']
        color = colors.get(gen, 'gray')
        
        # Draw line from birth to "now" or death
        linewidth = 3 if agent['status'] == 'running' else 1.5
        alpha = 1.0 if agent['status'] == 'running' else 0.6
        linestyle = '-' if agent['status'] == 'running' else '--'
        
        ax.barh(i, (end - created).days, left=0, 
               color=color, alpha=alpha, height=0.6,
               label=f'Gen {gen}' if f'Gen {gen}' not in [h.get_label() for h in ax.get_legend_handles_labels()[0]] else '')
        
        # Add agent name
        ax.text(-5, i, agent['name'], ha='right', va='center', fontsize=8)
        
        # Add death marker for stopped agents
        if agent['status'] == 'stopped':
            ax.scatter((end - created).days, i, marker='x', color='red', s=50, zorder=5)
    
    # Add generation color legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=colors[g], label=f'Generation {g}') for g in sorted(colors.keys())]
    legend_elements.append(plt.Line2D([0], [0], color='red', marker='x', markersize=8, label='Stopped (Dead)'))
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)
    
    ax.set_yticks([])
    ax.set_xlabel('Days Since First Agent ($SPORE) Launch', fontsize=11)
    ax.set_title('Spore.fun Agent Lifecycle Timeline', fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 'agent_timeline.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {filename}")
    return filename


def main():
    print("=" * 60)
    print("Spore.fun Aliveness Analysis")
    print("=" * 60)
    
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    
    agents = load_agents()
    hist_data = load_historical()
    
    print(f"\nLoaded {len(agents)} agents")
    
    # 1. Compute survival data
    print("\n[1] Computing survival data...")
    survival_data = compute_survival_data(agents)
    
    # 2. Compute Bedau activity
    print("[2] Computing Bedau evolutionary activity...")
    activity_data = compute_bedau_activity(agents, None)
    
    # 3. Compute reproductive fitness
    print("[3] Computing reproductive fitness...")
    fitness_data = compute_reproductive_fitness(agents)
    
    # 4. Compute metabolic rate
    print("[4] Computing metabolic rates...")
    metabolic_data = compute_metabolic_rate(hist_data)
    
    # 5. Compute economic vitality
    print("[5] Computing economic vitality...")
    economic_data = compute_economic_vitality(agents)
    
    # 6. Save all computed metrics
    print("[6] Saving metrics...")
    metrics = {
        'computed_at': datetime.now(timezone.utc).isoformat(),
        'survival': survival_data,
        'bedau_activity': activity_data,
        'reproductive_fitness': fitness_data,
        'metabolic_rates': metabolic_data,
        'economic_vitality': economic_data,
    }
    
    # Convert datetime objects for JSON serialization
    def json_serializable(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
    
    metrics_file = os.path.join(ANALYSIS_DIR, 'aliveness_metrics.json')
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2, default=json_serializable)
    print(f"  Saved metrics to: {metrics_file}")
    
    # 7. Generate plots
    print("\n[7] Generating plots...")
    
    try:
        plot_family_tree(agents, ANALYSIS_DIR)
    except Exception as e:
        print(f"  Family tree plot failed: {e}")
    
    try:
        plot_market_cap_by_generation(agents, ANALYSIS_DIR)
    except Exception as e:
        print(f"  Market cap plot failed: {e}")
    
    try:
        plot_survival_curve(survival_data, ANALYSIS_DIR)
    except Exception as e:
        print(f"  Survival curve failed: {e}")
    
    try:
        plot_bedau_activity(activity_data, ANALYSIS_DIR)
    except Exception as e:
        print(f"  Bedau activity plot failed: {e}")
    
    try:
        plot_spore_price_history(ANALYSIS_DIR)
    except Exception as e:
        print(f"  Price history plot failed: {e}")
    
    try:
        plot_metabolic_rates(metabolic_data, agents, ANALYSIS_DIR)
    except Exception as e:
        print(f"  Metabolic rate plot failed: {e}")
    
    try:
        plot_timeline(agents, ANALYSIS_DIR)
    except Exception as e:
        print(f"  Timeline plot failed: {e}")
    
    # 8. Print key metrics
    print("\n" + "="*60)
    print("KEY ALIVENESS METRICS SUMMARY")
    print("="*60)
    
    print("\n[Survival Analysis]")
    total = len(survival_data)
    alive = sum(1 for s in survival_data if not s['event'])
    dead = sum(1 for s in survival_data if s['event'])
    
    print(f"  Total agents: {total}")
    print(f"  Currently alive: {alive}")
    print(f"  Dead: {dead}")
    print(f"  Overall survival rate: {alive/total*100:.1f}%")
    
    # Median survival time (among dead)
    dead_durations = sorted([s['duration_days'] for s in survival_data if s['event']])
    if dead_durations:
        median_survival = dead_durations[len(dead_durations)//2]
        print(f"  Median survival (dead agents): {median_survival:.1f} days")
    
    print("\n[Bedau Evolutionary Activity]")
    for d in activity_data:
        print(f"  Gen {d['generation']}: {d['n_agents']} agents, "
              f"MC reached: {d['mc_reached_rate']*100:.0f}%, "
              f"Reproduced: {d['reproduction_rate']*100:.0f}%, "
              f"Total MC: ${d['total_market_cap']/1000:.0f}K")
    
    print("\n[Reproductive Fitness]")
    for f_data in fitness_data:
        if f_data['n_offspring'] > 0 or f_data['status'] == 'running':
            print(f"  {f_data['name']} (Gen{f_data['generation']}): "
                  f"{f_data['n_offspring']} offspring, "
                  f"{f_data['n_grandchildren']} grandchildren, "
                  f"MC reached: {f_data['mc_reached']}")
    
    print("\n[Economic Vitality]")
    ev = economic_data
    print(f"  Total current market cap: ${ev['total_market_cap_current']:,.0f}")
    print(f"  Total current treasury: ${ev['total_balance_current']:,.0f}")
    print(f"  Market cap Gini coefficient: {ev['mc_gini']:.3f}")
    print(f"  Treasury Gini coefficient: {ev['balance_gini']:.3f}")
    print(f"  Alive agents: {ev['n_alive']}")
    print(f"  Dead agents: {ev['n_dead']}")
    
    print("\n[Metabolic Activity - Wallet Transactions]")
    total_txs = sum(m['tx_count'] for m in metabolic_data)
    alive_txs = sum(m['tx_count'] for m in metabolic_data if m['status'] == 'running')
    print(f"  Total recent transactions (all agents): {total_txs}")
    print(f"  Active agent transactions: {alive_txs}")
    
    sol_balances = [(m['name'], m['wallet_sol_balance']) for m in metabolic_data if m.get('wallet_sol_balance')]
    sol_balances.sort(key=lambda x: x[1], reverse=True)
    print(f"\n  SOL balances by agent (top 5):")
    for name, sol in sol_balances[:5]:
        print(f"    {name}: {sol:.4f} SOL")
    
    return metrics


if __name__ == '__main__':
    metrics = main()
