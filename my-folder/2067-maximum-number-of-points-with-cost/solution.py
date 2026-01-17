class Solution:
    # DP Bottom-up approach
    def maxPoints(self, points: List[List[int]]) -> int:

        rows, cols = len(points), len(points[0])
        dp = points[0]

        for r in range(1, rows):
            left = [0] * cols
            left[0] = dp[0]
            for c in range(1, cols):
                left[c] = max(dp[c], left[c-1] - 1)

            right = [0] * cols
            right[cols-1] = dp[cols-1]
            for c in range(cols-2, -1, -1):
                right[c] = max(dp[c], right[c+1] - 1)

            nextDp = points[r][:]
            for c in range(cols):
                nextDp[c] += max(left[c], right[c])

            dp = nextDp

        return max(dp)

# Time -> O(rows * cols)
# O(cols)
