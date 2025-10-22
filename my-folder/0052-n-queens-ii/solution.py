class Solution:
    def totalNQueens(self, n: int) -> int:
        # Backtracking (Hash Set impl)
        colums = set()
        posDiag = set()
        negDiag = set()

        result = 0
        def backtrack(row):
            nonlocal result
            if row == n:
                result += 1
                return 
            
            for col in range(n):
                if col in colums or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                
                colums.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)

                backtrack(row+1)

                colums.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)

        backtrack(0)
        return result

# Time -> O(n!)
# Space -> O(n)
        
