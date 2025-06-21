class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary Search solution
        def findLeft():
            l, r = 0, len(nums) - 1
            leftIdx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid+1
                else: 
                    r = mid-1
                if nums[mid] == target:
                    leftIdx = mid #leftmost
            return leftIdx

        def findRight():
            l, r = 0, len(nums) - 1
            rightIdx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid-1
                else: 
                    l = mid+1
                if nums[mid] == target:
                    rightIdx = mid #leftmost
            return rightIdx
        
        return [findLeft(), findRight()]

# Time complexity = O(log n) each for findLeft and findRight
# Space complexity = O(1)
