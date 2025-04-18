"""Configure a hash table using a hybrid approach."""

class HashTableHybrid:
    """ A hybrid hash table with open addressing and chaining. """
    
    def __init__(self, capacity, probe_threshold=3):
        self.capacity = capacity
        self.table = [None] * capacity
        # number of items allowed to be probed before falling back to chaining
        self.probe_threshold = probe_threshold
        self.collisions = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        """Inserts a key-value pair into the hash table.
        If the target index is already occupied by a key, we probe for an empty slot.
        If the probe threshold is exceeded, we use chaining.
        """
        index = self._hash(key)
        probes = 0

        while probes < self.probe_threshold:
            # Use open addressing while under threshold
            if self.table[index] is None:
                self.table[index] = (key, value)
                return
            elif isinstance(self.table[index], list):
                # Already a chain here — just append
                self.table[index].append((key, value))
                self.collisions += 1
                return
            elif self.table[index][0] == key:
                # Key exists, update
                self.table[index] = (key, value)
                return
            else:
                # Collision, move to next index (linear probing)
                index = (index + 1) % self.capacity
                probes += 1
                self.collisions += 1

        # If too many probes, fall back to chaining at the last index
        if isinstance(self.table[index], list):
            # Already a chain here — just append
            self.table[index].append((key, value))
        else:
            # Turn current value into a chain
            existing = self.table[index]
            self.table[index] = [existing, (key, value)]

    def get(self, key):
        """Retrieve value associated with key."""
        index = self._hash(key)
        probes = 0

        while probes < self.probe_threshold:
            # Use open addressing while under threshold
            if self.table[index] is None:
                return None
            elif isinstance(self.table[index], list):
                # Search in the chain
                for item in self.table[index]:
                    if isinstance(item, tuple) and item[0] == key:
                        return item[1]
                return None
            elif isinstance(self.table[index], tuple) and self.table[index][0] == key:
                return self.table[index][1]
            else:
                index = (index + 1) % self.capacity
                probes += 1

        # Final chaining phase
        if isinstance(self.table[index], list):
            for item in self.table[index]:
                if isinstance(item, tuple) and item[0] == key:
                    return item[1]
        return None