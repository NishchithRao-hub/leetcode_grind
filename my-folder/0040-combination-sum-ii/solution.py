class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        curr = []
        self.count = defaultdict(int)
        A = []

        for num in candidates:
            if self.count[num] == 0:
                A.append(num)
            self.count[num] += 1

        self.backtrack(A, target, curr, 0)
        return self.result

    def backtrack(self, candidates, target, curr, i):
        if target == 0:
            return self.result.append(curr.copy())
        if target < 0 or i >= len(candidates):
            return
        
        if self.count[candidates[i]] > 0:
            curr.append(candidates[i])
            self.count[candidates[i]] -= 1
            self.backtrack(candidates, target - candidates[i], curr, i)
            self.count[candidates[i]] += 1
            curr.pop()

        self.backtrack(candidates, target, curr, i+1)

# Time = O(n * 2^n)
# Space = O(n)
        
