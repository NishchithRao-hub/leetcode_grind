class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        size = len(candidates)
        def dfs(curr, curr_sum, index):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(curr)
            for i in range(index, size):
                dfs(curr + [candidates[i]], curr_sum + candidates[i], i)
        
        dfs([],0,0)
        return result
        
