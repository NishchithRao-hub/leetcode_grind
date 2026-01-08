class Solution:
    # Bottom up DP + Binary Search
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        index = list(range(n))
        index.sort(key=lambda i: startTime[i])
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            left, right, j = i+1, n, n
            while left < right:
                mid = (left + right) // 2
                if startTime[index[mid]] >= endTime[index[i]]:
                    j = mid
                    right = mid
                else:
                    left = mid + 1

            dp[i] = max(dp[i+1], profit[index[i]] + dp[j])

        return dp[0]

# Time -> O(nlogn)
# Space -> O(n)
        
