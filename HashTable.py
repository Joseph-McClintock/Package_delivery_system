class HashMap:
    # Initialization - O(n)
    def __init__(self, size=10):
        self.map = []
        for i in range(size):
            self.map.append([])

    # Creates a hash for the inserted value - O(1)
    def get_hash(self, key):
        hash_key = hash(key) % len(self.map)
        return hash_key

    # Inserts a key and value into a hash-table - O(n)
    def insert(self, key, value):
        bucket = self.get_hash(key)
        bucket_value = [key, value]

        if self.map[bucket] is None:
            self.map[bucket] = list([bucket_value])
            return True
        else:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[bucket].append(bucket_value)
            return True

    # Returns an item in the hash-table based on a key - O(n)
    def get(self, key):
        for item in self.map[self.get_hash(key)]:
            if item[0] == key:
                return item[1]
        return None

    # Deletes an item from the hash-table - O(n)
    def delete(self, key):
        hash_key = self.get_hash(key)

        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
