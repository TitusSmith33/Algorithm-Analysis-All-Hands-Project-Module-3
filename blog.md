---
author: [Titus Smith, Daniel Bekele, Meghan Wolfarth, Darius Googe, Finley Banas]
title: Analyzing Collision Frequency and Lookup Performance on a Chaining, Open Addressing, and Hybrid Hash Table Configurations
page-layout: full
categories: [post, hash table, chaining, open addressing, hybrid]
date: "2025-04-24"
date-format: long
toc: true
---

## Introduction

## Motivation

TODO: Danny

## Experiment Design

Our experiment was designed to tackle the following research question. **RQ:** Compare hash table configurations (open addressing, chaining, hybrid) using a doubling experiment with randomly generated key-value pairs to analyze collision frequency and time overhead for lookups, including searches for both existing and non-existing keys. In order to successfully design a tool to test these features we split our tool into three algorithms (chaining, open addressing, and hybrid), benchmarking to measure performance metrics of our implementations, and a doubling experiment. This approach allows for clear implementation, running, and analysis of data.

## Implementation

### Chaining

TODO: Darius

### Open Addressing

Open addressing is a collision resolution method used in hash tables. When a collision occurs (two keys hashing into the same index) open addressing will search for the next available slot in the hash table to store the collided key. This element will ensure that all elements are to be stored in the hash table itself.

I used linear probing in the hash table which is a sequential checking method. The sequence starts by checking the original hash location. If that location is occupied the next location will be checked. This process will continue until an empty slot is found.

```python
index = (index + 1) % self.capacity
```

This section of code is the rehashing function that will find the empty slot in the hash table.

### Hybrid

TODO: Meghan

### Experiment and Benchmarking

To evaluate the performance of our hash table configurations (chaining, open addressing, and hybrid), we implemented a benchmarking structure that compares how each algorithm handles insertion and lookup in a doubling experiment. Our primary goal was to measure collision frequency during insertion and runtime during lookups. For the lookup experiment, we were concerned for both keys that existed in the table and those that did not. By doubling the number of key-value pairs with each test, from 1000 to 512,000 pairs, we can observe each implementation's worst-case time complexity and how well they maintain performance as the table becomes more populated.

To simulate realistic and diverse inputs, we used randomly generated strings as keys and integers as values. The random keys were created using combinations of uppercase and lowercase letters, while the values were simply random integers. This method ensured that our experiments weren't biased toward any particular pattern and better represented unpredictable real-world data.

```python
def random_string(length=5):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_pairs(k: int) -> List[Tuple[str, int]]:
    """Generate k random key-value pairs."""
    return [(random_string(), random.randint(1, 100)) for _ in range(k)]
```

Our benchmarking implementation is split into two main tests, insertion benchmarking and lookup benchmarking. For insertion, we measure the total time it takes to populate the table and count how many collisions occur. This benchmarking design gives us insight into how each method handles collisions in the hash space. Lookup benchmarking is performed by timing look-up for both existing keys and non-existing keys. This approach allows us to see not only how efficient each hash table is under successful look-up, but also how well each algorithm handles lookup failures. This is an important consideration because failed lookups may be common in real-world scenarios like caching or spell checking.

Overall, both approaches use a similar benchmarking technique by using the `time` function, to test the total tie to call the `put` and `get` methods for each of our hash table configurations. Together, out measurements provide a holistic view of the strengths and trade-offs of each collision resolution technique, and presented the data in a way that was simple to analyze and directly see the worst-case time complexity.

## Running the Experiments

To run our experiment, we have opted to use Python directly. In order to run the program, all that the user needs to do is clone the repo to their laptop. From there, the user simply enters the `src` directory of our tool, and types `python main.py` in their terminal and the program will produce 6 basic tables. Each of the tables represented the doubling experiment conducted, three for collision testing and 3 for look-up testing. The data should be displayed in a clear and labeled manner to ensure readability and easy analysis.

When using the tool, it is important to note that there should be no need for alteration of the code to properly run this edition of our experiment, as we have handled all the variables and key-value pair generation through the individual implementations and experiment design.

### Example Output

Below is an example of what the expected output from running our tool looks like. This data, along with the analysis from other runs across operating systems, will help guide our analysis and conclusion on collision frequency and lookup performance of various hash table configurations.

```text
Starting hash table comparison experiments...

Generating experiment data...

Running doubling experiment...

Chaining Hash Table Population Performance (seconds)
Size    Populate Time    Num. of Collisions
----    --------------  ----------
1000    0.000551        0
2000    0.000539        0
4000    0.000535        0
8000    0.001102        0
16000   0.004733        0
32000   0.012599        0
64000   0.023571        0
128000  0.047765        0
256000  0.084535        0
512000  0.188057        0

Open Addressing Hash Table Population Performance (seconds)
Size    Populate Time    Num. of Collisions
----    --------------  ----------
1000    0.001745        509
2000    0.006581        980
4000    0.016572        1997
8000    0.059750        3990
16000   0.145642        7962
32000   0.767986        15972
64000   2.548893        32008
128000  5.890426        63845
256000  24.904955       127993
512000  32.579744       255330

Hybrid Hash Table Population Performance (seconds)
Size    Populate Time    Num. of Collisions
----    --------------  ----------
1000    0.000000        918
2000    0.000000        1768
4000    0.000000        3617
8000    0.016283        7232
16000   0.004849        14407
32000   0.018594        28789
64000   0.041206        57284
128000  0.116695        115051
256000  0.246317        229837
512000  0.716221        458745

Running lookup experiment...

Chaining Hash Table Lookup Performance (seconds)
Size    Existing Lookup         Non-Existing Lookup
----    ----------------        -------------------
1000    0.000543                0.000000
2000    0.000529                0.000000
4000    0.000000                0.000534
8000    0.000564                0.000000
16000   0.000524                0.000000
32000   0.000000                0.000000
64000   0.000000                0.000000
128000  0.000000                0.000000
256000  0.000556                0.000000
512000  0.000000                0.009288

Open Addressing Hash Table Lookup Performance (seconds)
Size    Existing Lookup         Non-Existing Lookup
----    ----------------        -------------------
1000    0.002285                0.084326
2000    0.001909                0.170237
4000    0.003496                0.368865
8000    0.006198                0.964839
16000   0.015819                1.990731
32000   0.033609                3.385081
64000   0.049811                8.993584
128000  0.046854                11.788684
256000  0.079588                37.889480
512000  0.056853                19.009886

Hybrid Hash Table Lookup Performance (seconds)
Size    Existing Lookup         Non-Existing Lookup
----    ----------------        -------------------
1000    0.000000                0.000000
2000    0.000000                0.000000
4000    0.001080                0.000503
8000    0.000000                0.000000
16000   0.000000                0.000000
32000   0.000000                0.000000
64000   0.000000                0.000000
128000  0.001000                0.001000
256000  0.005110                0.000000
512000  0.000000                0.000000
```

Importantly, while this result was ran on a Windows system, our results and analysis were ran across a variety of operating systems, including Windows and macOS, in order to provide the most inclusive and well-rounded analysis possible.

### Data Analysis

## Future Work

## Conclusion
