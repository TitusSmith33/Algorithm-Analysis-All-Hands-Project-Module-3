"""Benchmarking module for comparing different hash table implementations."""

import time
from typing import List, Tuple, Any
from chain import HashTableChainning
from open_addressing import HashTableOpenAddressing
from hybrid import HashTableHybrid

def benchmark_put_operations(ht_class, capacity: int, kv_pairs: List[Tuple[Any, Any]]) -> Tuple[float, int]:
    """Benchmark put operations and return time taken and collision count."""
    ht = ht_class(capacity)
    start_time = time.time()
    
    for key, value in kv_pairs:
        ht.put(key, value)
    
    end_time = time.time()
    return end_time - start_time, ht.collisions

def benchmark_get_operations(ht_class, capacity: int, kv_pairs: List[Tuple[Any, Any]], 
                           existing_keys: List[Any], non_existing_keys: List[Any]) -> Tuple[float, float]:
    """Benchmark get operations for both existing and non-existing keys."""
    # First populate the hash table
    ht = ht_class(capacity)
    for key, value in kv_pairs:
        ht.put(key, value)
    
    # Benchmark existing keys
    start_time = time.time()
    for key in existing_keys:
        ht.get(key)
    existing_time = time.time() - start_time
    
    # Benchmark non-existing keys
    start_time = time.time()
    for key in non_existing_keys:
        ht.get(key)
    non_existing_time = time.time() - start_time
    
    return existing_time, non_existing_time

def run_doubling_experiment(kv_pairs_list: List[List[Tuple[Any, Any]]], 
                          existing_keys_list: List[List[Any]], 
                          non_existing_keys_list: List[List[Any]]):
    """Run doubling experiment comparing different hash table implementations.
    
    Args:
        kv_pairs_list: List of key-value pairs for each size
        existing_keys_list: List of existing keys to test for each size
        non_existing_keys_list: List of non-existing keys to test for each size
    """
    print("Size\tChain Time\tChain Collisions\tOpen Time\tOpen Collisions\tHybrid Time\tHybrid Collisions")
    print("----\t----------\t---------------\t---------\t--------------\t-----------\t----------------")
    
    for i, (kv_pairs, existing_keys, non_existing_keys) in enumerate(zip(
        kv_pairs_list, existing_keys_list, non_existing_keys_list)):
        
        size = len(kv_pairs)
        # Benchmark each implementation
        chain_time, chain_collisions = benchmark_put_operations(HashTableChainning, size, kv_pairs)
        open_time, open_collisions = benchmark_put_operations(HashTableOpenAddressing, size, kv_pairs)
        hybrid_time, hybrid_collisions = benchmark_put_operations(HashTableHybrid, size, kv_pairs)
        
        # Print results
        print(f"{size}\t{chain_time:.6f}\t{chain_collisions}\t{open_time:.6f}\t{open_collisions}\t{hybrid_time:.6f}\t{hybrid_collisions}")

def run_lookup_experiment(kv_pairs: List[Tuple[Any, Any]], 
                        existing_keys: List[Any], 
                        non_existing_keys: List[Any]):
    """Run experiment comparing lookup times for existing and non-existing keys.
    
    Args:
        kv_pairs: List of key-value pairs to insert
        existing_keys: List of keys that exist in the hash table
        non_existing_keys: List of keys that don't exist in the hash table
    """
    print("\nLookup Performance Comparison")
    print("Implementation\tExisting Keys Time\tNon-existing Keys Time")
    print("-------------\t-----------------\t---------------------")
    
    size = len(kv_pairs)
    # Benchmark each implementation
    chain_existing, chain_non_existing = benchmark_get_operations(
        HashTableChainning, size, kv_pairs, existing_keys, non_existing_keys)
    open_existing, open_non_existing = benchmark_get_operations(
        HashTableOpenAddressing, size, kv_pairs, existing_keys, non_existing_keys)
    hybrid_existing, hybrid_non_existing = benchmark_get_operations(
        HashTableHybrid, size, kv_pairs, existing_keys, non_existing_keys)
    
    # Print results
    print(f"Chaining\t{chain_existing:.6f}\t{chain_non_existing:.6f}")
    print(f"Open Addressing\t{open_existing:.6f}\t{open_non_existing:.6f}")
    print(f"Hybrid\t{hybrid_existing:.6f}\t{hybrid_non_existing:.6f}")

if __name__ == "__main__":
    print("Running doubling experiment...")
    run_doubling_experiment()
    
    print("\nRunning lookup experiment...")
    run_lookup_experiment()
