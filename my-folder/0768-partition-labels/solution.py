class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Two pointers (Greedy)
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        size = end = 0
        result = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                result.append(size)
                size = 0

        return result

# Time -> O(n) (n is length of s)
# Space -> O(m) (m is unique chars in s)
        
