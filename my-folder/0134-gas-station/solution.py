class Solution:
    # Greedy solution
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_gas = 0
        res_idx = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]

            if total_gas < 0:
                total_gas = 0
                res_idx = i + 1

        return res_idx

# Time -> O(n)
# Space -> O(1)       
        
