class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right, self.left = Node(0,0), Node (0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.cache.pop(node.key)
        return node
    
    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.remove(self.cache[key])
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.remove(self.cache[key])
            node.value = value
            self.insert(node)
        else:
            self.insert(Node(key,value))
        
        if len(self.cache) > self.capacity:
            self.remove(self.left.next)
        return None
        
