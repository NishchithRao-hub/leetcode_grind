class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Two pointers
        a, b = 0, 1
        result = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                result[a] = nums[i]
                a += 2
            else:
                result[b] = nums[i]
                b += 2

        return result

# Time -> O(n)
# Space -> O(n)
        
