class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # BFS solution
        n = len(isConnected)
        visited = [False] * n
        result = 0
        q = deque()

        for i in range(n):
            if not visited[i]:
                result += 1
                visited[i] = True
                q.append(i)
                while q:
                    node = q.popleft()
                    for nei in range(n):
                        if isConnected[node][nei] and not visited[nei]:
                            visited[nei] = True
                            q.append(nei)

        return result

# Time -> O(n^2)
# Space -> O(n)
        
