class FreqStack:
    # Hash Map solution
    def __init__(self):
        self.stacks = {}
        self.count = {}
        self.maxCount = 0

    def push(self, val: int) -> None:
        valCount = self.count.get(val, 0) + 1
        self.count[val] = valCount
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val) 

    def pop(self) -> int:
        result = self.stacks[self.maxCount].pop()
        self.count[result] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return result

# Time -> O(1) for push and pop
# Space -> O(n)
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
