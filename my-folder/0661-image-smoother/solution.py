class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = self.smoother(img , i , j)
        
        return result

    def smoother(self, img, a, b):
        m, n = len(img), len(img[0])
        sum, count = 0, 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                na, nb = a + i, b + j
                if 0 <= na < m and 0 <= nb < n:
                    sum += img[na][nb]
                    count += 1

        return sum // count 
