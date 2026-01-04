"""
Hash Table Implementation
A data structure that maps keys to values using a hash function.
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def get(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        return any(k == key for k, v in bucket)
    
    def __str__(self):
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"
