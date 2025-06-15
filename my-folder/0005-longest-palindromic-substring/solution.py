class Solution:
    def longestPalindrome(self, s: str) -> str:
        resId = 0
        resLen = 0

        for i in range(len(s)):
            # odd len palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resId = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even len palindrome
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resId = l
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return s[resId: resId + resLen]
        
