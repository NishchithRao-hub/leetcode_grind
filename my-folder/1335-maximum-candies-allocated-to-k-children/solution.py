class Solution:
    # Binary Search
    def maximumCandies(self, candies: List[int], k: int) -> int:
        maxCandies = 0
        for candy_pile in candies:
            maxCandies = max(maxCandies, candy_pile)

        left = 0
        right = maxCandies
        
        while left < right:
            middle = (left+right+1) // 2

            if self.canAllocateCandies(candies, k, middle):
                left = middle
            else:
                right = middle - 1

        return left
        
    def canAllocateCandies(self, candies, k, numCandies):
        maxChildren = 0
        for pile in candies:
            maxChildren += pile // numCandies

        return maxChildren >= k

# Time -> O(n* logm) canAllocateCandies is O(n) (n is candy piles) and (logm) for binary search in main. 
# Space -> O(1)
