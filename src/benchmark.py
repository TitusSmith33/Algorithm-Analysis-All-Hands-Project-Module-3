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
    """Run doubling experiment comparing different hash table implementations."""


    def print_table(title, benchmark_func):
        """Generate structure for displaying experiment data."""
        print(f"\n{title} Hash Table Population Performance (seconds)")
        print("Size\tPopulate Time\t Num. of Collisions")
        print("----\t--------------\t----------")
        for kv_pairs in kv_pairs_list:
            size = len(kv_pairs)
            time_taken, collisions = benchmark_func(size, kv_pairs)
            print(f"{size:<4}\t{time_taken:.6f}\t{collisions}")
    
    # run and print results of generating a hash table with a given configuration
    # display results independently for comprehension
    print_table("Chaining", lambda size, pairs: benchmark_put_operations(HashTableChainning, size, pairs))
    print_table("Open Addressing", lambda size, pairs: benchmark_put_operations(HashTableOpenAddressing, size, pairs))
    print_table("Hybrid", lambda size, pairs: benchmark_put_operations(HashTableHybrid, size, pairs))


def run_lookup_experiment(kv_pairs_list: List[List[Tuple[Any, Any]]], 
                          existing_keys_list: List[List[Any]], 
                          non_existing_keys_list: List[List[Any]]):
    """Run doubling experiment comparing lookup times for existing and non-existing keys."""

    def print_lookup_table(title, benchmark_func):
        """Generate structure for displaying experiment data."""
        print(f"\n{title} Hash Table Lookup Performance (seconds)")
        print("Size\tExisting Lookup\t\tNon-Existing Lookup")
        print("----\t----------------\t-------------------")
        for kv_pairs, existing_keys, non_existing_keys in zip(
            kv_pairs_list, existing_keys_list, non_existing_keys_list):
            
            size = len(kv_pairs)
            existing_time, non_existing_time = benchmark_func(
                size, kv_pairs, existing_keys, non_existing_keys)
            print(f"{size:<4}\t{existing_time:.6f} \t\t{non_existing_time:.6f}")

    # print results for each hash table configuration independently
    # results are time took to lookup values in a given configuration
    print_lookup_table("Chaining", 
        lambda size, kvs, exists, not_exists: benchmark_get_operations(
            HashTableChainning, size, kvs, exists, not_exists))
    
    print_lookup_table("Open Addressing", 
        lambda size, kvs, exists, not_exists: benchmark_get_operations(
            HashTableOpenAddressing, size, kvs, exists, not_exists))
    
    print_lookup_table("Hybrid", 
        lambda size, kvs, exists, not_exists: benchmark_get_operations(
            HashTableHybrid, size, kvs, exists, not_exists))
