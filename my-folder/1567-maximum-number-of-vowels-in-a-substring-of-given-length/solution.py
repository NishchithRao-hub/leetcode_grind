class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = max_vowels = 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
# Once the first window is fully formed, checks whether the character that is sliding out of the current window is a vowel.            
            if i >= k and s[i - k] in vowels:
                count -= 1
            max_vowels = max(max_vowels, count)
            
            if max_vowels == k:  # Early stopping: can't get better than this
                return k

        return max_vowels
        
# Time Complexity: O(n)
# (Each character is visited once.)

# Space Complexity: O(1)
# (Constant space for tracking vowels.)
