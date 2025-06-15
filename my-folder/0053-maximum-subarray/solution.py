class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Recursive approach(Time-> O(2^n), Space-> O(1))
        # def dfs(i, flag):
        #     if i == len(nums):
        #         return 0 if flag else -1e6
        #     if flag:
        #         return max(0, nums[i]+dfs(i+1, True))
        #     return max(dfs(i+1, False), nums[i]+dfs(i+1, True))

        # return dfs(0, False)

        # Kadane's algorithm
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0

            currSum += num
            maxSum = max(maxSum, currSum)

        return maxSum

# Time complexity: O(n)
# Space complexity: O(1)
        
