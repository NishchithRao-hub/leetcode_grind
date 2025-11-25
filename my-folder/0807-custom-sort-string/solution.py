class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Frequency count solution
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        result = []
        for char in order:
            index = ord(char) - ord('a')
            while count[index]:
                result.append(char)
                count[index] -= 1

        for index in range(26):
            char = chr(ord('a') + index)
            while count[index]:
                count[index] -= 1
                result.append(char)

        return ''.join(result)

# Time -> O(n)
# Space -> O(n)
        
