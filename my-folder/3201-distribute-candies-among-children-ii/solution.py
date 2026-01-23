class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for a in range(min(n, limit) + 1):
            if n - a <= 2 * limit:
                b_max = min(n-a, limit)
                b_min = max(0, n-a-limit)
                result += b_max - b_min + 1

        return result

# Time -> O(min(limit, n))
# Space -> O(1)
        
