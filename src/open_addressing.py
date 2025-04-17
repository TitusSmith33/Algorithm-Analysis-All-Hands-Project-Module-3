"""Configure a hash table using an open addressing approach."""

class HashTableOpenAddressing:
    """A hash table implementation using open addressing with linear probing."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.collisions = 0

    def put(self, key, value):
        """Inserts the key-value pair into the hash table.
        A collision is recorded if the initial index is occupied.
        If the key already exists, update the value.
        """
        index = hash(key) % self.capacity
        start_index = index
        first = True

        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                self.table[index] = (key, value)
                return
            if first:
                self.collisions += 1
                first = False
            index = (index + 1) % self.capacity
            if index == start_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)


    def get(self, key):
        """Retrieves the value associated with the given key from the hash table."""

        index = hash(key) % self.capacity
        start_index = index

        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                return v
            index = (index + 1) % self.capacity
            if index == start_index:
                break

        return None
