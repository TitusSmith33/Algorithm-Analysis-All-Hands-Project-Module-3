# Compare hash table configurations using a doubling experiment with randomly generated key-value pairs to analyze collision frequency and time overhead for searching for keys.

## Introduction

RQ: Compare hash table configurations (open addressing, chaining, hybrid) using a doubling experiment with randomly generated key-value pairs to analyze collision frequency and time overhead for lookups, including searches for both existing and non-existing keys.

## Source Code

### chain.py

### open_addressing.py

Open addressing is a collision resolution method used in hash tables. When a collision occurs (two keys hashing into the same index) open addressing will search for the next available slot in the hash table to store the collided key. This element will ensure that all elements are to be stored in the hash table itself. 

I used linear probing in the hash table which is a sequential checking method. The sequence starts by checking the original hash location. If that location is occupied the next location will be checked. This process will continue until an empty slot is found. 

`index = (index + 1) % self.capacity`

This section of code is the rehashing function that will find the empty slot in the hash table.

### hybrid.py

## Running the Code

### Finley Banas

#### Run of Systemsense

#### Run of the program

### Name

#### Run of Systemsense

#### Run of the program

### Name

#### Run of Systemsense

#### Run of the program

### Name

#### Run of Systemsense

#### Run of the program

### Name

#### Run of Systemsense

#### Run of the program

### Name

#### Run of Systemsense

#### Run of the program

## Conclusion