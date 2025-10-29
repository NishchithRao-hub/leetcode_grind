class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window soln
        if t == "":
            return ""

        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        curr, target = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                curr += 1

            while curr == target:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    curr -= 1
                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != float('infinity') else ""

# Time -> O(n + m) (n is length of string and m is unique strings in t and s)
# Space -> O(m)
        
