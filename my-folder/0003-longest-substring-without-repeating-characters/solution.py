class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window solution
        charSet = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right-left+1)

        return result

# Time complexity = O(n)
# Space complexity = O(m)
# n is length of string and m is unique characters in string
        
