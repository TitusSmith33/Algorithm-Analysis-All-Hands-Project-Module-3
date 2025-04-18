"""Doubling experiment testing collision rate and lookup time of has tables."""

# TODO: implement doubling experiment and driver function

import random
import string

import chain
import hybrid
import open_addressing

def random_string(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_pairs(k):
    return [(random_string(), random.randint(1, 100)) for _ in range(k)]

# hash table generator
def generate_and_fill_hash_table(k, strategy):
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