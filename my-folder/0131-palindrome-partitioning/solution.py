class Solution(object):
    def partition(self, s):
        def palindrome_check(word):
            return word == word[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if palindrome_check(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result
        
