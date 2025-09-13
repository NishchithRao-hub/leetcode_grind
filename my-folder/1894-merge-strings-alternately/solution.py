class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Two pointers
        i, j = 0, 0
        result = []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)

# Time -> O(n+m) (n is length of word1 and m in length of word2)
# Space -> O(n+m)
        
