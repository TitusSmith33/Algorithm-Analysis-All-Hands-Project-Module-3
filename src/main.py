"""Doubling experiment testing collision rate and lookup time of hash tables."""

import random
import string
from typing import List, Tuple, Any, Dict
import time

import chain
import hybrid
import open_addressing
import benchmark

def random_string(length=5):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_pairs(k: int) -> List[Tuple[str, int]]:
    """Generate k random key-value pairs."""
    return [(random_string(), random.randint(1, 100)) for _ in range(k)]

def generate_and_fill_hash_table(k: int, strategy: str) -> Tuple[Any, List[Tuple[str, int]]]:
    """Generates a hash table using the given strategy and fills it with k random pairs."""
    # choose the hash table configuration based on strategy
    if strategy == 'hybrid':
        table = hybrid.HashTableHybrid(capacity=k)
    elif strategy == 'open':
        table = open_addressing.HashTableOpenAddressing(capacity=k)
    elif strategy == 'chain':
        table = chain.HashTableChainning(capacity=k)
    else:
        raise ValueError("Invalid configuration. Choose from: 'hybrid', 'open', or 'chain'.")

    # generate key-value pairs and insert into hash table
    pairs = generate_random_pairs(k)
    for key, value in pairs:
        table.put(key, value)

    return table, pairs

def generate_experiment_data(initial_size: int = 1000, max_size: int = 1000000) -> Tuple[List[List[Tuple[str, int]]], List[List[str]], List[List[str]]]:
    """Generate data for the doubling experiment.
    
    Returns:
        Tuple containing:
        - List of key-value pairs for each size
        - List of existing keys for each size
        - List of non-existing keys for each size
    """
    kv_pairs_list = []
    existing_keys_list = []
    non_existing_keys_list = []
    
    current_size = initial_size
    while current_size <= max_size:
        # Generate key-value pairs
        kv_pairs = generate_random_pairs(current_size)
        kv_pairs_list.append(kv_pairs)
        
        # Generate existing keys (1000 random keys from the current pairs)
        existing_keys = [random.choice(kv_pairs)[0] for _ in range(1000)]
        existing_keys_list.append(existing_keys)
        
        # Generate non-existing keys (1000 random strings)
        non_existing_keys = [random_string() for _ in range(1000)]
        non_existing_keys_list.append(non_existing_keys)
        
        current_size *= 2
    
    return kv_pairs_list, existing_keys_list, non_existing_keys_list

def run_strategy_experiment(strategy: str, sizes: List[int]) -> Dict[int, Tuple[float, int]]:
    """Run experiment for a specific strategy across different sizes."""
    results = {}
    for size in sizes:
        table, pairs = generate_and_fill_hash_table(size, strategy)
        results[size] = (table.collisions, len(pairs))
    return results

def main():
    """Run the hash table comparison experiments."""
    print("Starting hash table comparison experiments...")
    
    # Define experiment sizes
    sizes = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000]
    
    # Run experiments for each strategy
    strategies = ['chain', 'open', 'hybrid']
    results = {}
    
    for strategy in strategies:
        print(f"\nRunning experiment for {strategy} strategy...")
        results[strategy] = run_strategy_experiment(strategy, sizes)
    
    # Print results
    print("\nResults Summary:")
    print("Size\tChain Collisions\tOpen Collisions\tHybrid Collisions")
    print("----\t---------------\t--------------\t----------------")
    
    for size in sizes:
        chain_collisions = results['chain'][size][0]
        open_collisions = results['open'][size][0]
        hybrid_collisions = results['hybrid'][size][0]
        print(f"{size}\t{chain_collisions}\t{open_collisions}\t{hybrid_collisions}")
    
    # Run lookup experiment with the largest size
    print("\nRunning lookup experiment...")
    largest_size = sizes[-1]
    for strategy in strategies:
        table, pairs = generate_and_fill_hash_table(largest_size, strategy)
        existing_keys = [random.choice(pairs)[0] for _ in range(1000)]
        non_existing_keys = [random_string() for _ in range(1000)]
        
        # Time lookups for existing keys
        start_time = time.time()
        for key in existing_keys:
            table.get(key)
        existing_time = time.time() - start_time
        
        # Time lookups for non-existing keys
        start_time = time.time()
        for key in non_existing_keys:
            table.get(key)
        non_existing_time = time.time() - start_time
        
        print(f"\n{strategy.capitalize()} Strategy Lookup Performance:")
        print(f"Existing Keys Time: {existing_time:.6f}")
        print(f"Non-existing Keys Time: {non_existing_time:.6f}")

if __name__ == "__main__":
    main()