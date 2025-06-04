from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for src, dest in trust:
            outdegree[src] += 1
            indegree[dest] += 1

        for i in range(1, n+1):
            if outdegree[i] == 0 and indegree[i] == n-1:
                return i

        return -1
        
