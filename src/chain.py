"""Configure a hash table using a chain approach."""

# TODO: implement chain approach

class HashTableChainning:
    """ A hash table implementation using separate chaining."""

    def  __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.collisions = 0

    def put(self, key, value):
        """Inserts the key-value pair into the hash table.
        A collison is recorded if the target bucket is not empty.
        if the key already exists in the bucket, its value is updated.
        """

        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        # Record a collison if there is already at least one element in the bucket.
        if bucket:
            self.collisions += 1
            # Update the value if the key already exists.
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return
            bucket.append((key, value))

    def get(self, key):
        """Retrieves the value associated with the given key from the hash table."""

        index = hash(key) % self.capacity
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
            return None