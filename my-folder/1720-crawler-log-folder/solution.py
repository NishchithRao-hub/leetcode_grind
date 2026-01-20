class Solution:
    # Iterative solution
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for log in logs:
            if log == "./":
                continue
            if log == "../":
                result = max(0, result-1)
            else:
                result += 1

        return result

# Time -> O(n)
# Space -> O(1)
        
