class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtracking(start, combination):
            if len(combination) == k:
                result.append(combination[:])
                return
            
            for i in range(start, n+1):
                combination.append(i)
                backtracking(i+1,combination)
                combination.pop()

        result = []
        backtracking(1, [])
        return result
