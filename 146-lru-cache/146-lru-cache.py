class Node:
    def __init__(self, key, value):
        self.right = None
        self.left = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.right = self.mru
        self.mru.left = self.lru
    
    def remove(self, node):
        prev, nxt = node.left, node.right
        prev.right, nxt.left = nxt, prev
        
    
    def insert(self, node):
        prev, nxt = self.mru.left, self.mru
        node.right = nxt
        node.left = prev
        prev.right = nxt.left = node

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.remove(self.hmap[key])
            self.insert(self.hmap[key])
            return self.hmap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.insert(self.hmap[key])
        if len(self.hmap) > self.capacity:
            node = self.lru.right
            self.remove(node)
            del self.hmap[node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)