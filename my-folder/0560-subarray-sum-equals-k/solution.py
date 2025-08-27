class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hash Map solution
        result = currSum = 0
        prefixSum = {0 : 1}

        for num in nums:
            currSum += num
            diff = currSum - k

            result += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return result

# Time -> O(n)
# Space -> O(n)
        
