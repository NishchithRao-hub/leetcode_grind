class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search solution
        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                result = k
                r = k-1
            else:
                l = k+1
            
        return result

# Time complexity = O(n log m)
# Space complexity = O(1) 
        
