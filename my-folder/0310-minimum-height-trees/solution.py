class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = collections.defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            size = len(q)
            remaining_nodes -= size
            
            for _ in range(size):
                leaf = q.popleft()
                for nei in adj[leaf]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        return list(q)
        
