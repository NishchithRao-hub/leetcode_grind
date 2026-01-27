class Solution:
    # Two pointers
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = k = 0

        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1

            if j - i > 1:
                for char in str(j-i):
                    chars[k] = char
                    k += 1

            i = j
        return k

# Time -> O(N)
# Space -> O(1)
        
