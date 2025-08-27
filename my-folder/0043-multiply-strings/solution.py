class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Multiplication result
        if "0" in [num1, num2]:
            return "0"

        result = [0] * (len(num1)+len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                result[i+j] += digit
                result[i+j+1] += result[i+j]//10
                result[i+j] = result[i+j]%10

        result, beg = result[::-1], 0
        while beg < len(result) and result[beg] == 0:
            beg += 1
        result = map(str, result[beg:])
        return "".join(result)

# Time -> O(m*n)
# Space -> O(m+n)
# (m = length of num1 and n = length of num2)
        
