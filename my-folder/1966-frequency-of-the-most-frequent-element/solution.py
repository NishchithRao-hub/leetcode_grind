class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sliding window
        nums.sort()
        result = total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            result = max(result, right - left + 1)

        return result

# Time -> O(n logn)
# Space -> O(1) or O(n) (based on sorting algorithm)
        
