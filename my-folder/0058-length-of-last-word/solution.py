class Solution:
    # Iteration
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        result = 0

        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            i -= 1
            result += 1

        return result

# Time -> O(n)
# Space -> O(1)
        
