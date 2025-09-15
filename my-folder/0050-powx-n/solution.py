class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Binary exponentiation(Iterative)
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = 1
        power = abs(n)

        while power:
            if power & 1:
                result *= x
            x *= x
            power >>= 1

        return result if n >= 0 else 1/result

# Time -> O(log n)
# Space -> O(1)
        
