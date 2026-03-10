#!/usr/bin/env python3
"""
Script 02: Collect market data for all Spore.fun agents from DexScreener.
Also tries Birdeye and Solscan for historical data.
Saves to data/market_data/{agent_slug}.csv and data/market_data/{agent_slug}_raw.json
"""

import requests
import json
import os
import time
import csv
from datetime import datetime, timezone

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
AGENTS_FILE = os.path.join(BASE_DIR, 'agents.json')
MARKET_DIR = os.path.join(BASE_DIR, 'market_data')


def load_agents():
    with open(AGENTS_FILE) as f:
        data = json.load(f)
    return data['agents']


def fetch_dexscreener(token_address):
    """Fetch current token data from DexScreener."""
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  DexScreener error: {e}")
        return None


def fetch_dexscreener_pairs(token_address):
    """Get all trading pairs for a token."""
    data = fetch_dexscreener(token_address)
    if not data:
        return []
    return data.get('pairs', [])


def get_token_stats(token_address, agent_name):
    """Get comprehensive token statistics."""
    print(f"  Fetching DexScreener data for {agent_name} ({token_address[:8]}...)")
    pairs = fetch_dexscreener_pairs(token_address)
    
    if not pairs:
        print(f"  No pairs found for {agent_name}")
        return None
    
    # Get the most liquid pair (primary pair)
    primary_pair = max(pairs, key=lambda p: p.get('liquidity', {}).get('usd', 0) or 0)
    
    stats = {
        'token_address': token_address,
        'agent_name': agent_name,
        'num_pairs': len(pairs),
        'pairs_data': []
    }
    
    for pair in pairs:
        pair_stat = {
            'pair_address': pair.get('pairAddress'),
            'dex': pair.get('dexId'),
            'chain': pair.get('chainId'),
            'price_usd': pair.get('priceUsd'),
            'price_native': pair.get('priceNative'),
            'market_cap': pair.get('marketCap'),
            'fdv': pair.get('fdv'),
            'liquidity_usd': pair.get('liquidity', {}).get('usd'),
            'volume_24h': pair.get('volume', {}).get('h24'),
            'volume_6h': pair.get('volume', {}).get('h6'),
            'volume_1h': pair.get('volume', {}).get('h1'),
            'txns_24h_buys': pair.get('txns', {}).get('h24', {}).get('buys', 0),
            'txns_24h_sells': pair.get('txns', {}).get('h24', {}).get('sells', 0),
            'txns_1h_buys': pair.get('txns', {}).get('h1', {}).get('buys', 0),
            'txns_1h_sells': pair.get('txns', {}).get('h1', {}).get('sells', 0),
            'price_change_5m': pair.get('priceChange', {}).get('m5'),
            'price_change_1h': pair.get('priceChange', {}).get('h1'),
            'price_change_6h': pair.get('priceChange', {}).get('h6'),
            'price_change_24h': pair.get('priceChange', {}).get('h24'),
            'pair_created_at': pair.get('pairCreatedAt'),
        }
        stats['pairs_data'].append(pair_stat)
    
    # Primary pair summary
    stats['primary'] = {
        'dex': primary_pair.get('dexId'),
        'price_usd': primary_pair.get('priceUsd'),
        'market_cap': primary_pair.get('marketCap'),
        'liquidity_usd': primary_pair.get('liquidity', {}).get('usd'),
        'volume_24h': primary_pair.get('volume', {}).get('h24'),
        'pair_created_at': primary_pair.get('pairCreatedAt'),
        'pair_age_days': None,
    }
    
    if primary_pair.get('pairCreatedAt'):
        created_ts = int(primary_pair['pairCreatedAt']) / 1000
        now_ts = datetime.now(timezone.utc).timestamp()
        stats['primary']['pair_age_days'] = (now_ts - created_ts) / 86400
    
    return stats


def fetch_solscan_transfers(token_address, limit=20):
    """Fetch token transfer/holder data from Solscan (free tier)."""
    url = f"https://api.solscan.io/v2/token/meta?tokenAddress={token_address}"
    headers = {
        'user-agent': 'Mozilla/5.0',
        'accept': 'application/json',
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"  Solscan error: {e}")
    return None


def fetch_holder_count(token_address):
    """Get holder count from Solscan."""
    url = f"https://api-v2.solscan.io/v2/token/holders?token={token_address}&page=1&page_size=1"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'accept': 'application/json',
        'origin': 'https://solscan.io',
        'referer': 'https://solscan.io/',
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            data = r.json()
            return data.get('data', {}).get('total', None)
    except Exception as e:
        print(f"  Holder count error: {e}")
    return None


def fetch_birdeye_overview(token_address):
    """Fetch token overview from Birdeye (free tier, no key needed for basic data)."""
    url = f"https://public-api.birdeye.so/defi/token_overview?address={token_address}"
    headers = {
        'accept': 'application/json',
        'X-Chain': 'solana',
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"  Birdeye error: {e}")
    return None


def save_agent_market_data(agent, stats, holder_count, birdeye_data):
    """Save market data for a single agent."""
    slug = agent['slug']
    
    # Save raw JSON
    raw_file = os.path.join(MARKET_DIR, f"{slug}_raw.json")
    raw_data = {
        'agent': {
            'id': agent['id'],
            'name': agent['name'],
            'slug': agent['slug'],
            'generation': agent['generation'],
            'token_address': agent['tokenAddress'],
            'wallet_address': agent['walletAddress'],
            'token_type': agent['tokenType'],
            'twitter': agent.get('twitterUsername'),
            'parent_id': agent.get('parentId'),
            'status': agent['status'],
            'market_cap_reached': agent.get('marketCapReached'),
            'created_at': str(agent.get('createdAt', '')),
            'capabilities': agent.get('capabilities', []),
            'health_points': agent.get('healthPoints'),
            'balance': agent.get('balance'),
            'api_market_cap': agent.get('marketCap'),
        },
        'dexscreener': stats,
        'holder_count': holder_count,
        'birdeye': birdeye_data,
        'collected_at': datetime.now(timezone.utc).isoformat()
    }
    
    with open(raw_file, 'w') as f:
        json.dump(raw_data, f, indent=2, default=str)
    
    # Save CSV with current snapshot
    csv_file = os.path.join(MARKET_DIR, f"{slug}_snapshot.csv")
    
    rows = []
    timestamp = datetime.now(timezone.utc).isoformat()
    
    if stats and stats.get('pairs_data'):
        for pair in stats['pairs_data']:
            rows.append({
                'timestamp': timestamp,
                'agent_id': agent['id'],
                'agent_name': agent['name'],
                'generation': agent['generation'],
                'token_address': agent['tokenAddress'],
                'pair_address': pair['pair_address'],
                'dex': pair['dex'],
                'price_usd': pair['price_usd'],
                'market_cap': pair['market_cap'],
                'fdv': pair['fdv'],
                'liquidity_usd': pair['liquidity_usd'],
                'volume_24h': pair['volume_24h'],
                'volume_6h': pair['volume_6h'],
                'volume_1h': pair['volume_1h'],
                'txns_24h_buys': pair['txns_24h_buys'],
                'txns_24h_sells': pair['txns_24h_sells'],
                'price_change_24h': pair['price_change_24h'],
                'holder_count': holder_count,
                'pair_created_at': pair['pair_created_at'],
                'agent_status': agent['status'],
                'market_cap_reached': agent.get('marketCapReached'),
            })
    else:
        # No DexScreener data, use API data
        rows.append({
            'timestamp': timestamp,
            'agent_id': agent['id'],
            'agent_name': agent['name'],
            'generation': agent['generation'],
            'token_address': agent['tokenAddress'],
            'pair_address': None,
            'dex': None,
            'price_usd': None,
            'market_cap': agent.get('marketCap'),
            'fdv': None,
            'liquidity_usd': None,
            'volume_24h': None,
            'volume_6h': None,
            'volume_1h': None,
            'txns_24h_buys': None,
            'txns_24h_sells': None,
            'price_change_24h': None,
            'holder_count': holder_count,
            'pair_created_at': None,
            'agent_status': agent['status'],
            'market_cap_reached': agent.get('marketCapReached'),
        })
    
    if rows:
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    
    print(f"  Saved: {raw_file}")
    print(f"  Saved: {csv_file}")


def main():
    print("=" * 60)
    print("Spore.fun Market Data Collection")
    print("=" * 60)
    
    os.makedirs(MARKET_DIR, exist_ok=True)
    agents = load_agents()
    
    all_summaries = []
    
    for i, agent in enumerate(agents):
        print(f"\n[{i+1}/{len(agents)}] Processing: {agent['name']} (Gen {agent['generation']}, {agent['status']})")
        
        token_address = agent.get('tokenAddress')
        if not token_address:
            print(f"  No token address for {agent['name']}, skipping")
            continue
        
        # Fetch DexScreener data
        stats = get_token_stats(token_address, agent['name'])
        
        # Fetch holder count
        print(f"  Fetching holder count...")
        holder_count = fetch_holder_count(token_address)
        print(f"  Holder count: {holder_count}")
        
        # Fetch Birdeye data
        print(f"  Fetching Birdeye data...")
        birdeye = fetch_birdeye_overview(token_address)
        
        # Save data
        save_agent_market_data(agent, stats, holder_count, birdeye)
        
        # Summary
        summary = {
            'id': agent['id'],
            'name': agent['name'],
            'slug': agent['slug'],
            'generation': agent['generation'],
            'status': agent['status'],
            'token_address': token_address,
            'market_cap_api': agent.get('marketCap'),
            'market_cap_dex': None,
            'liquidity_usd': None,
            'volume_24h': None,
            'holder_count': holder_count,
            'market_cap_reached': agent.get('marketCapReached'),
            'num_pairs': 0,
        }
        
        if stats:
            summary['market_cap_dex'] = stats.get('primary', {}).get('market_cap')
            summary['liquidity_usd'] = stats.get('primary', {}).get('liquidity_usd')
            summary['volume_24h'] = stats.get('primary', {}).get('volume_24h')
            summary['num_pairs'] = stats.get('num_pairs', 0)
        
        all_summaries.append(summary)
        
        # Rate limiting
        time.sleep(1)
    
    # Save combined summary
    summary_file = os.path.join(MARKET_DIR, 'market_summary.json')
    with open(summary_file, 'w') as f:
        json.dump({
            'collected_at': datetime.now(timezone.utc).isoformat(),
            'agents': all_summaries
        }, f, indent=2)
    
    print(f"\n{'='*60}")
    print("MARKET DATA SUMMARY")
    print(f"{'='*60}")
    print(f"{'Name':<22} {'Gen':<4} {'Status':<10} {'MC (API)':<15} {'MC (DEX)':<15} {'Holders':<10} {'Vol 24h':<12}")
    print("-" * 95)
    for s in all_summaries:
        mc_api = f"${float(s['market_cap_api'] or 0):,.0f}"
        mc_dex = f"${float(s['market_cap_dex'] or 0):,.0f}" if s['market_cap_dex'] else 'N/A'
        vol = f"${float(s['volume_24h'] or 0):,.0f}" if s['volume_24h'] is not None else 'N/A'
        holders = str(s['holder_count']) if s['holder_count'] else 'N/A'
        print(f"{s['name']:<22} {s['generation']:<4} {s['status']:<10} {mc_api:<15} {mc_dex:<15} {holders:<10} {vol}")
    
    print(f"\nSaved summary to: {summary_file}")


if __name__ == '__main__':
    main()
