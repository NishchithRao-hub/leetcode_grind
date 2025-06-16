class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking solution
        stack = []
        result = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return result

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return result

# Time complexity: O(4^n/sqrt(n)) (Catalan number)
# Space complexity: O(n)
