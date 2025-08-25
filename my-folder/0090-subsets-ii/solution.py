class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            result.append(subset[::])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()

        backtrack(0, [])
        return result 

# Time -> O(n * 2^n)
# Space -> O(n) extra space, O(2^n) for output
