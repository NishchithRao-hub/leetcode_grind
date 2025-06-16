import random
class RandomizedSet:

    def __init__(self):
        self.val_idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False
        
        self.val_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False
        
        idx_remove = self.val_idx[val]
        last_element = self.nums[-1]

        self.nums[idx_remove] = last_element
        self.val_idx[last_element] = idx_remove

        self.nums.pop()
        del self.val_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Operation	  Time	    Space
# Insert	    O(1)	O(n)
# Remove	    O(1)	O(n)
# GetRandom	   O(1)	    O(n)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
