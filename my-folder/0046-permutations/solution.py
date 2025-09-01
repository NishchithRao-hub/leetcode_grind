class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            # Backtracking optimal
        self.result = []
        self.backtrack(nums, 0)
        return self.result

    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            return self.result.append(nums[:])
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.backtrack(nums, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx]

# Time -> O(n * n!)
# Space -> O(n * n!)
        
