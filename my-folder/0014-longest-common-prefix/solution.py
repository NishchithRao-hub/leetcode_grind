class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Normal iteration
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix

# Time -> O(n*m) (n is length of shortest string, m is num of strings)
# Space -> O(1)
        
