#!/usr/bin/env python3
"""
Script 01: Collect all Spore.fun agent data from the API.
Saves to data/agents.json
"""

import requests
import json
import os
from urllib.parse import urlencode
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..')
AGENTS_FILE = os.path.join(OUTPUT_DIR, 'agents.json')


def fetch_spore_agents():
    """Fetch all agents from Spore.fun API."""
    url = 'https://www.spore.fun/api/trpc/status,listAgent'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'referer': 'https://www.spore.fun/',
        'trpc-accept': 'application/jsonl',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-trpc-source': 'nextjs-react'
    }
    params = {
        'batch': '1',
        'input': '{"0":{"json":null,"meta":{"values":["undefined"]}},"1":{"json":null,"meta":{"values":["undefined"]}}}'
    }
    full_url = f"{url}?{urlencode(params)}"
    
    print(f"Fetching from: {full_url}")
    r = requests.get(full_url, headers=headers, timeout=30)
    r.raise_for_status()
    
    # Parse JSONL response
    agents = []
    status_data = None
    
    for line in r.text.strip().split('\n'):
        if not line.strip():
            continue
        obj = json.loads(line)
        
        # Look for the agent list (it's in a specific position in the response)
        if isinstance(obj.get('json'), list):
            json_data = obj['json']
            if len(json_data) >= 3 and isinstance(json_data[2], list):
                for item in json_data[2]:
                    if isinstance(item, list):
                        for subitem in item:
                            if isinstance(subitem, list) and len(subitem) > 0:
                                for agent in subitem:
                                    if isinstance(agent, dict) and 'id' in agent and 'name' in agent:
                                        agents.append(agent)
                            elif isinstance(subitem, dict) and 'breedingCount' in subitem:
                                status_data = subitem
    
    return agents, status_data


def build_family_tree(agents):
    """Build parent-child relationships."""
    agent_map = {a['id']: a for a in agents}
    
    for agent in agents:
        parent_id = agent.get('parentId')
        if parent_id and parent_id in agent_map:
            agent['parentName'] = agent_map[parent_id]['name']
            agent['parentSlug'] = agent_map[parent_id]['slug']
        else:
            agent['parentName'] = None
            agent['parentSlug'] = None
        
        # Find children
        agent['children'] = [
            {'id': a['id'], 'name': a['name'], 'slug': a['slug']}
            for a in agents if a.get('parentId') == agent['id']
        ]
    
    return agents


def main():
    print("=" * 60)
    print("Spore.fun Agent Data Collection")
    print("=" * 60)
    
    agents, status = fetch_spore_agents()
    print(f"\nFound {len(agents)} agents")
    
    if status:
        print(f"Global status: {status}")
    
    # Build family tree
    agents = build_family_tree(agents)
    
    # Print summary
    print("\nAgent Summary:")
    print(f"{'ID':<4} {'Name':<20} {'Gen':<4} {'Status':<10} {'MarketCap':<15} {'Parent':<15} {'Token':<50}")
    print("-" * 120)
    for a in sorted(agents, key=lambda x: x['id']):
        parent_name = a.get('parentName') or 'None'
        print(f"{a['id']:<4} {a['name']:<20} {a['generation']:<4} {a['status']:<10} "
              f"${float(a.get('marketCap', 0) or 0):>12,.2f} {parent_name:<15} {a.get('tokenAddress', 'N/A')}")
    
    # Save to JSON
    output = {
        'collected_at': datetime.utcnow().isoformat() + 'Z',
        'data_source': 'https://www.spore.fun/api/trpc/status,listAgent',
        'global_status': status,
        'total_agents': len(agents),
        'agents': agents
    }
    
    os.makedirs(os.path.dirname(AGENTS_FILE), exist_ok=True)
    with open(AGENTS_FILE, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"\nSaved to: {AGENTS_FILE}")
    
    # Print generation breakdown
    from collections import Counter
    gen_counts = Counter(a['generation'] for a in agents)
    print("\nGeneration breakdown:")
    for gen in sorted(gen_counts.keys()):
        agents_in_gen = [a for a in agents if a['generation'] == gen]
        running = sum(1 for a in agents_in_gen if a['status'] == 'running')
        reached_mc = sum(1 for a in agents_in_gen if a.get('marketCapReached'))
        print(f"  Gen {gen}: {gen_counts[gen]} agents, {running} running, {reached_mc} reached $500K MC")


if __name__ == '__main__':
    main()
