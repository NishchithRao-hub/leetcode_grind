class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Greedy approach
        cost_diff = []
        for cost1, cost2 in costs:
            cost_diff.append([cost2 - cost1, cost1, cost2])

        result = 0
        cost_diff.sort()
        N = len(cost_diff) // 2
        for i in range(len(cost_diff)):
            if i < N:
                result += cost_diff[i][2]
            else:
                result += cost_diff[i][1]

        return result

# Time -> O(nlogn)
# Space -> O(n)
        
