class Solution:
        # Two Pointers
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return len(t) - j

# Time -> O(n * m) (n, m being num of chars in s and t)
# Space -> O(1)
        
