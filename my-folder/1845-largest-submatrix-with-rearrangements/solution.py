class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        result = 0

        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c]:
                    matrix[r][c] += matrix[r-1][c]

        for r in range(rows):
            matrix[r].sort(reverse=True)
            for i in range(cols):
                result = max(result, (i+1) * matrix[r][i])

        return result

# Time -> O(m * nlogn)
# Space -> O(1) or O(n)
# Where m is the number of rows and n is the number of columns.
        
