# https://leetcode.com/problems/lru-cache/

class DLNode:
    def __init__(self,key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_val = {}
        self.LRU = DLNode()
        self.MRU = DLNode()
        self.LRU.right = self.MRU
        self.MRU.left = self.LRU
    
    def insert(self, node: DLNode):
        MRU_left = self.MRU.left
        MRU_left.right = node
        node.left = MRU_left
        self.MRU.left = node
        node.right = self.MRU
    
    def remove(self, node: DLNode):
        node_left = node.left
        node_right = node.right

        node_left.right = node_right
        node_right.left = node_left

    def get(self, key: int) -> int:
        if not key in self.key_val:
            return -1

        node = self.key_val[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_val:
            self.remove(self.key_val[key])
        
        node = DLNode(key, value)
        self.insert(node)
        self.key_val[key] = node

        if len(self.key_val.keys()) > self.capacity:
            lru_node = self.LRU.right
            self.remove(lru_node)
            del self.key_val[lru_node.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)