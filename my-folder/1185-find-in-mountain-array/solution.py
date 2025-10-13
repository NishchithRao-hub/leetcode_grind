# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Binary search + cache
        memo = {}
        length = mountainArr.length()

        def get_val(index):
            if index not in memo:
                memo[index] = mountainArr.get(index)
            return memo[index]

        # Find Peak 
        l, r = 1, length - 2
        peak = -1

        while l <= r:
            m = (l + r) // 2

            mid_val = get_val(m)
            right_val = get_val(m + 1)

            if mid_val < right_val:
                l = m + 1
            else:
                peak = m
                r = m - 1
        peak = l
        
        # 2. Search left
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = get_val(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # 3. Search right
        l, r = peak + 1, length - 1
        while l <= r:
            m = (l + r) // 2
            val = get_val(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        return -1
        
# Time -> O(logn)
# Space -> O(logn)
