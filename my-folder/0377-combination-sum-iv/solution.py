class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # DP Bottom up
        nums.sort()
        dp = defaultdict(int)
        dp[target] = 1

        for total in range(target, 0, -1):
            for num in nums:
                if total < num:
                    break
                dp[total-num] += dp[total]

        return dp[0]

# Time -> O(n*t)
# Space -> O(t)
        
