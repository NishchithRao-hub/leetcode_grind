class Solution:
    # Dijkstra's Algorithm
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            src, dest = edges[i]
            graph[src].append((dest, succProb[i]))
            graph[dest].append((src, succProb[i]))

        maxProb = [0] * n
        maxProb[start_node] = 1.0
        pq = [(-1.0, start_node)]

        while pq:
            curr_prob, curr_node = heapq.heappop(pq)
            curr_prob *= -1

            if curr_node == end_node:
                return curr_prob
            if curr_prob > maxProb[curr_node]:
                continue

            for neighbor, edge in graph[curr_node]:
                new_prob = curr_prob * edge
                if new_prob > maxProb[neighbor]:
                    maxProb[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return 0.0

# Time -> O((V+E)log V)
# Space -> O(V+E)
        
