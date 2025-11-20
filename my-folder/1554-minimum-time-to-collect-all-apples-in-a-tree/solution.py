class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Topological (Kahns) using modified BFS
        adj = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(1, n):
            if indegree[i] == 1:
                q.append(i)
                indegree[i] = 0

        time = [0] * n
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if indegree[nei] <= 0:
                    continue
                
                indegree[nei] -= 1
                if hasApple[node] or time[node] > 0:
                    time[nei] += 2 + time[node]
                if indegree[nei] == 1 and nei != 0:
                    q.append(nei)

        return time[0]

# Time -> O(V + E)
# Space -> O(V + E)
        
