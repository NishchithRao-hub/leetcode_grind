class Solution:
    # Prefix sum with arrays
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        count = [0] * (n+1)
        count[0] = 1
        prefixSum = 0
        result = 0

        for num in nums:
            prefixSum += num
            if prefixSum >= goal:
                result += count[prefixSum - goal]
            count[prefixSum] += 1

        return result

# Time -> O(n)
# Space -> O(n)
        
