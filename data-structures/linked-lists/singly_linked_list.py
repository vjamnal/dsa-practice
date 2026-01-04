"""
Singly Linked List Implementation
A linear data structure where each element points to the next.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data):
        if self.is_empty():
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
