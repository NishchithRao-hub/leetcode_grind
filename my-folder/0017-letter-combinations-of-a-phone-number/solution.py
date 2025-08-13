class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = [""]

        for digit in digits:
            temp = []
            for curr in result:
                for ch in digitToChar[digit]:
                    temp.append(curr + ch)

            result = temp
        return result
        
