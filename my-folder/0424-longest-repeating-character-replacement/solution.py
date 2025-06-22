class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window soln
        charSet = set(s)
        result = 0

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                result = max(result, r - l + 1)
            
        return result

# Time complexity = O(m*n)
# Space complexity = O(m)
        
