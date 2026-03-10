#!/usr/bin/env python3
"""
Script 03: Collect historical OHLCV data for Spore.fun agents.
Uses GeckoTerminal API (free), Solana RPC, and DexScreener.
"""

import requests
import json
import os
import csv
import time
from datetime import datetime, timezone

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
AGENTS_FILE = os.path.join(BASE_DIR, 'agents.json')
MARKET_DIR = os.path.join(BASE_DIR, 'market_data')


def load_agents():
    with open(AGENTS_FILE) as f:
        return json.load(f)['agents']


def get_gecko_pools(network, token_addr):
    """Get all pools for a token from GeckoTerminal."""
    url = f"https://api.geckoterminal.com/api/v2/networks/{network}/tokens/{token_addr}/pools"
    headers = {'accept': 'application/json;version=20230302'}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code == 200:
            return r.json().get('data', [])
        print(f"    GeckoTerminal pools error {r.status_code}: {r.text[:200]}")
    except Exception as e:
        print(f"    GeckoTerminal error: {e}")
    return []


def get_gecko_ohlcv(network, pool_addr, timeframe='day', limit=1000, aggregate=1):
    """Get OHLCV data for a pool from GeckoTerminal."""
    url = f"https://api.geckoterminal.com/api/v2/networks/{network}/pools/{pool_addr}/ohlcv/{timeframe}"
    params = {'limit': limit, 'aggregate': aggregate}
    headers = {'accept': 'application/json;version=20230302'}
    try:
        r = requests.get(url, params=params, headers=headers, timeout=20)
        if r.status_code == 200:
            data = r.json()
            return data.get('data', {}).get('attributes', {}).get('ohlcv_list', [])
        print(f"    GeckoTerminal OHLCV error {r.status_code}")
    except Exception as e:
        print(f"    GeckoTerminal OHLCV error: {e}")
    return []


def get_solana_tx_count(address, rpc_url='https://api.mainnet-beta.solana.com'):
    """Get approximate transaction count for an address."""
    payload = {
        'jsonrpc': '2.0', 'id': 1,
        'method': 'getSignaturesForAddress',
        'params': [address, {'limit': 1000}]
    }
    try:
        r = requests.post(rpc_url, json=payload, timeout=30)
        data = r.json()
        sigs = data.get('result', [])
        return len(sigs), sigs
    except Exception as e:
        print(f"    Solana RPC error: {e}")
        return 0, []


def get_solana_account_balance(address, rpc_url='https://api.mainnet-beta.solana.com'):
    """Get SOL balance for an address."""
    payload = {
        'jsonrpc': '2.0', 'id': 1,
        'method': 'getBalance',
        'params': [address]
    }
    try:
        r = requests.post(rpc_url, json=payload, timeout=20)
        data = r.json()
        lamports = data.get('result', {}).get('value', 0)
        return lamports / 1e9  # Convert to SOL
    except Exception as e:
        print(f"    Balance error: {e}")
        return None


def save_ohlcv_csv(agent_slug, pool_id, dex, ohlcv_data, timeframe='day'):
    """Save OHLCV data to CSV."""
    if not ohlcv_data:
        return None
    
    filename = os.path.join(MARKET_DIR, f"{agent_slug}_{dex}_{timeframe}_ohlcv.csv")
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'datetime', 'open', 'high', 'low', 'close', 'volume'])
        writer.writeheader()
        for row in ohlcv_data:
            if len(row) >= 6:
                ts = row[0]
                dt = datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
                writer.writerow({
                    'timestamp': ts,
                    'datetime': dt,
                    'open': row[1],
                    'high': row[2],
                    'low': row[3],
                    'close': row[4],
                    'volume': row[5],
                })
    
    return filename


def get_dexscreener_pairs(token_address):
    """Get current data from DexScreener."""
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    try:
        r = requests.get(url, timeout=20)
        if r.status_code == 200:
            return r.json().get('pairs', [])
    except Exception as e:
        print(f"    DexScreener error: {e}")
    return []


def main():
    print("=" * 60)
    print("Spore.fun Historical Data Collection")
    print("=" * 60)
    
    os.makedirs(MARKET_DIR, exist_ok=True)
    agents = load_agents()
    
    summary = {}
    
    for agent in agents:
        name = agent['name']
        slug = agent['slug']
        token_addr = agent.get('tokenAddress')
        wallet_addr = agent.get('walletAddress')
        
        print(f"\n--- {name} (Gen {agent['generation']}, {agent['status']}) ---")
        
        agent_data = {
            'id': agent['id'],
            'name': name,
            'slug': slug,
            'generation': agent['generation'],
            'status': agent['status'],
            'token_address': token_addr,
            'wallet_address': wallet_addr,
            'pools': [],
            'ohlcv_files': {},
            'tx_count': None,
            'tx_details': [],
            'wallet_sol_balance': None,
        }
        
        # 1. Get pools and OHLCV from GeckoTerminal
        if token_addr:
            print(f"  Fetching GeckoTerminal pools...")
            pools = get_gecko_pools('solana', token_addr)
            print(f"  Found {len(pools)} pools")
            
            # Save pool info
            for pool in pools:
                pool_id = pool.get('id', '').replace('solana_', '')
                dex_id = pool.get('relationships', {}).get('dex', {}).get('data', {}).get('id', 'unknown')
                attrs = pool.get('attributes', {})
                
                pool_info = {
                    'pool_address': pool_id,
                    'dex': dex_id,
                    'market_cap_usd': attrs.get('market_cap_usd'),
                    'volume_24h': attrs.get('volume_usd', {}).get('h24'),
                    'reserve_in_usd': attrs.get('reserve_in_usd'),
                    'created_at': attrs.get('pool_created_at'),
                }
                agent_data['pools'].append(pool_info)
            
            # Get OHLCV for the best pool (most liquidity)
            if pools:
                # Sort by market cap
                best_pool = None
                for pool in pools:
                    attrs = pool.get('attributes', {})
                    mc = attrs.get('market_cap_usd')
                    if mc:
                        if best_pool is None or (mc and float(mc) > float(best_pool.get('attributes', {}).get('market_cap_usd', 0) or 0)):
                            best_pool = pool
                
                if best_pool:
                    pool_id = best_pool.get('id', '').replace('solana_', '')
                    dex_id = best_pool.get('relationships', {}).get('dex', {}).get('data', {}).get('id', 'unknown')
                    
                    print(f"  Fetching daily OHLCV from GeckoTerminal ({dex_id})...")
                    ohlcv_day = get_gecko_ohlcv('solana', pool_id, 'day', 1000)
                    
                    if ohlcv_day:
                        filename = save_ohlcv_csv(slug, pool_id, dex_id, ohlcv_day, 'day')
                        if filename:
                            agent_data['ohlcv_files']['day'] = filename
                            print(f"  Saved {len(ohlcv_day)} days of OHLCV to {os.path.basename(filename)}")
                            
                            # Print date range
                            first_ts = ohlcv_day[-1][0]
                            last_ts = ohlcv_day[0][0]
                            print(f"  Date range: {datetime.fromtimestamp(first_ts).strftime('%Y-%m-%d')} to {datetime.fromtimestamp(last_ts).strftime('%Y-%m-%d')}")
                    else:
                        print(f"  No OHLCV data from GeckoTerminal")
                    
                    time.sleep(0.5)
                    
                    # Also get hourly OHLCV (last ~100 hours)
                    print(f"  Fetching hourly OHLCV...")
                    ohlcv_hour = get_gecko_ohlcv('solana', pool_id, 'hour', 500)
                    if ohlcv_hour:
                        filename = save_ohlcv_csv(slug, pool_id, dex_id, ohlcv_hour, 'hour')
                        if filename:
                            agent_data['ohlcv_files']['hour'] = filename
                            print(f"  Saved {len(ohlcv_hour)} hours of OHLCV")
                    
                    time.sleep(0.5)
        
        # 2. Get DexScreener current data
        if token_addr:
            print(f"  Fetching DexScreener data...")
            pairs = get_dexscreener_pairs(token_addr)
            if pairs:
                best_pair = max(pairs, key=lambda p: p.get('liquidity', {}).get('usd', 0) or 0)
                agent_data['dexscreener'] = {
                    'num_pairs': len(pairs),
                    'price_usd': best_pair.get('priceUsd'),
                    'market_cap': best_pair.get('marketCap'),
                    'fdv': best_pair.get('fdv'),
                    'liquidity_usd': best_pair.get('liquidity', {}).get('usd'),
                    'volume_24h': best_pair.get('volume', {}).get('h24'),
                    'txns_24h_buys': best_pair.get('txns', {}).get('h24', {}).get('buys', 0),
                    'txns_24h_sells': best_pair.get('txns', {}).get('h24', {}).get('sells', 0),
                    'pair_created_at': best_pair.get('pairCreatedAt'),
                }
                print(f"  DexScreener: MC=${agent_data['dexscreener']['market_cap']}, {len(pairs)} pairs")
        
        # 3. Get transaction count for wallet
        if wallet_addr:
            print(f"  Fetching wallet transactions...")
            tx_count, tx_sigs = get_solana_tx_count(wallet_addr)
            agent_data['tx_count'] = tx_count
            
            # Get recent tx timestamps
            tx_timestamps = []
            for sig in tx_sigs[:20]:
                bt = sig.get('blockTime')
                if bt:
                    tx_timestamps.append({
                        'signature': sig['signature'][:20] + '...',
                        'block_time': bt,
                        'datetime': datetime.fromtimestamp(bt, tz=timezone.utc).isoformat()
                    })
            agent_data['recent_tx'] = tx_timestamps
            print(f"  Wallet: {tx_count} recent transactions")
            time.sleep(0.3)
        
        # 4. Get wallet SOL balance
        if wallet_addr:
            sol_balance = get_solana_account_balance(wallet_addr)
            agent_data['wallet_sol_balance'] = sol_balance
            print(f"  Wallet SOL balance: {sol_balance:.4f} SOL" if sol_balance is not None else "  SOL balance: N/A")
        
        summary[slug] = agent_data
        
        # Rate limiting
        time.sleep(0.5)
    
    # Save comprehensive summary
    output_file = os.path.join(MARKET_DIR, 'historical_summary.json')
    with open(output_file, 'w') as f:
        json.dump({
            'collected_at': datetime.now(timezone.utc).isoformat(),
            'agents': list(summary.values())
        }, f, indent=2, default=str)
    
    print(f"\n{'='*60}")
    print(f"Saved historical summary to: {output_file}")
    
    # Print summary table
    print(f"\n{'Agent':<22} {'Gen':<4} {'Status':<10} {'OHLCV Days':<12} {'TXs':<8} {'SOL Bal':<12} {'Pools'}")
    print("-" * 90)
    for slug, data in summary.items():
        ohlcv_days = 0
        if 'day' in data.get('ohlcv_files', {}):
            # Count rows in CSV
            try:
                with open(data['ohlcv_files']['day']) as f:
                    ohlcv_days = sum(1 for _ in f) - 1  # subtract header
            except:
                pass
        
        sol = f"{data['wallet_sol_balance']:.4f}" if data.get('wallet_sol_balance') is not None else 'N/A'
        num_pools = len(data.get('pools', []))
        print(f"{data['name']:<22} {data['generation']:<4} {data['status']:<10} {ohlcv_days:<12} {data.get('tx_count', 'N/A'):<8} {sol:<12} {num_pools}")


if __name__ == '__main__':
    main()
