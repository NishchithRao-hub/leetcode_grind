class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack
        result = [0] * len(temperatures)
        stack = [] # pair -> (temp, idx)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx
            stack.append([t, i])
        return result

# Time -> O(n)
# Space -> O(n)
        
