class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        # Two pass approach
        # for idx, num in enumerate(nums):
        #     indices[num] = idx

        # for idx, num in enumerate(nums):
        #     diff = target - num
        #     if diff in indices and indices[diff] != idx:
        #         return[idx, indices[diff]]

        # One pass approach
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in indices:
                return[indices[diff], idx]

            indices[num] = idx
        
