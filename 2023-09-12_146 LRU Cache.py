# https://leetcode.com/problems/lru-cache/

class LRUCache: # T: 92.89% M: 96.93%
    def __init__(self, capacity: int):
        self.ht = dict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key in self.ht.keys():
            value = self.ht[key]
            del self.ht[key]
            self.ht[key] = value 
            return self.ht[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.ht.keys():
            del self.ht[key]
        elif len(self.ht) == self.capacity:
            del self.ht[next(iter(self.ht))]
        self.ht[key] = value    
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)