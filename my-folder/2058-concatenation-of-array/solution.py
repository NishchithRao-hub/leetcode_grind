class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = nums[i]

        return ans

# Time -> O(n)
# Space -> O(n)
        
