"""
Dynamic Array Implementation
A dynamic array that automatically resizes when needed.
"""

class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def append(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1
    
    def insert(self, index, element):
        if not 0 <= index <= self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1
    
    def delete(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
    
    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def __str__(self):
        return str([self.array[i] for i in range(self.size)])
