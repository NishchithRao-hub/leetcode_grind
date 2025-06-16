class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer solution
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNumeric(s[l]):
                l += 1
            while r > l and not self.alphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True 

    
    def alphaNumeric(self, c):
        return ((ord('a') <= ord(c) <= ord('z')) or 
                (ord('A') <= ord(c) <= ord('Z')) or 
                (ord('0') <= ord(c) <= ord('9')))

# Time: O(n) — each character is visited at most once.
# Space: O(1) — constant extra space (no new strings are created).
        
