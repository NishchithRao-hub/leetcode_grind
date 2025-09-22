class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search (One pass)
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows*cols-1

        while left <= right:
            mid = left + (right-left) // 2
            r, c = mid // cols, mid % cols
            if target > matrix[r][c]:
                left = mid + 1
            elif target < matrix[r][c]:
                right = mid - 1
            else:
                return True
        
        return False

# Time -> O(log(m*n))
# Space -> O(1)
        
