"""Doubling experiment testing collision rate and lookup time of hash tables."""

import random
import string
from typing import List, Tuple, Any, Dict

import benchmark

def random_string(length=5):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_pairs(k: int) -> List[Tuple[str, int]]:
    """Generate k random key-value pairs."""
    return [(random_string(), random.randint(1, 100)) for _ in range(k)]

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

def main():
    """Run the hash table comparison experiments."""
    print("Starting hash table comparison experiments...")
    
    # Generate data for doubling experiment
    print("\nGenerating experiment data...")
    kv_pairs_list, existing_keys_list, non_existing_keys_list = generate_experiment_data()
    
    # Run doubling experiment using benchmark module
    print("\nRunning doubling experiment...")
    benchmark.run_doubling_experiment(kv_pairs_list, existing_keys_list, non_existing_keys_list)
    
    # Run lookup experiment using benchmark module
    print("\nRunning lookup experiment...")
    benchmark.run_lookup_experiment(
    kv_pairs_list,
    existing_keys_list,
    non_existing_keys_list
    )

if __name__ == "__main__":
    main()