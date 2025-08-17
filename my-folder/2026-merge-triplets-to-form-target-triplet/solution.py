class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Greedy approach
        result = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, value in enumerate(t):
                if value == target[i]:
                    result.add(i)

        return len(result) == 3

# Time -> O(n)
# Space -> O(1)
        
