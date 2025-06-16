class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reverse = 0
        number  = x

        while number != 0:
            reverse = reverse*10 + number%10
            number  = number // 10

        return reverse == x
        
