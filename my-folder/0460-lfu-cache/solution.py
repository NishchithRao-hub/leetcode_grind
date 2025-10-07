# Doubly LinkedList impl
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popLeft(self):
        result = self.left.next.val
        self.pop(self.left.next.val)
        return result

    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu = 0
        self.valMap = {} # Key -> Value
        self.countMap = defaultdict(int) # Key -> Count
        self.listMap = defaultdict(LinkedList) # Count of Key -> LinkedList

    def counter(self, key):
        count = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[count].pop(key)
        self.listMap[count+1].pushRight(key)
        
        if count == self.lfu and self.listMap[count].length() == 0:
            self.lfu += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key not in self.valMap and len(self.valMap) == self.capacity:
            result = self.listMap[self.lfu].popLeft()
            self.valMap.pop(result)
            self.countMap.pop(result)
        
        self.valMap[key] = value
        self.counter(key)
        self.lfu = min(self.lfu, self.countMap[key])

# Time -> O(1) for get and put operations
# Space -> O(n)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
