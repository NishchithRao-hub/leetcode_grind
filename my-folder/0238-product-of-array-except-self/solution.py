class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and Suffix (Space Optimized):
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
        
        # Prefix and Suffix
        # n = len(nums)
        # result  = [0] * n
        # prefix = [0] * n
        # suffix = [0] * n

        # prefix[0] = suffix[n-1] = 1
        # for i in range(1, n):
        #     prefix[i] = nums[i-1] * prefix[i-1]
        # for i in range(n-2, -1, -1):
        #     suffix[i] = nums[i+1] * suffix[i+1]
        # for i in range(n):
        #     result[i] = prefix[i] * suffix[i]

        # return result
        
        
