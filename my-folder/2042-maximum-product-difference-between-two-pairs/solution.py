class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        f_large = s_large = 0
        f_small = s_small = float("inf")

        for n in nums:
            if n < f_small:
                s_small , f_small = f_small, n
            elif n < s_small:
                s_small = n

            if n > f_large:
                s_large, f_large = f_large, n
            elif n > s_large:    
                s_large = n

        return f_large * s_large - f_small * s_small 
