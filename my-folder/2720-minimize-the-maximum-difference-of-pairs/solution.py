class Solution:
    # Greedy + Binary Search
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        def isValid(limit):
            idx, count = 0, 0
            while idx < len(nums)-1:
                if abs(nums[idx] - nums[idx+1]) <= limit:
                    count += 1
                    idx += 2
                else:
                    idx += 1
                if count == p:
                    return True
            return False

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        result = nums[-1] - nums[0]

        while left <= right:
            mid = left + (right - left)//2
            if isValid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return result

# Time -> O(nlogn + nlogd) (nlogn for sorting + logd for binary search and n for each check)
# Space -> O(1) or O(n) based on sorting algo
        
