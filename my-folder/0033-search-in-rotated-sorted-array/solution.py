class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search (One Pass)
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l += 1
                else:
                    r -= 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r -= 1
                else:
                    l += 1

        return -1 
        
# Time complexity = O(log n)
# Space complexity = O(1)
        
