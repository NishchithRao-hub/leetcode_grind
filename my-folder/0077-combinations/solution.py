class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Iteration using Backtracking
        result = []
        comb = [0] * k
        i = 0

        while i >= 0:
            comb[i] += 1
            if comb[i] > n:
                i -= 1
                continue

            if i == k-1:
                result.append(comb.copy())
            else:
                i += 1
                comb[i] = comb[i-1]

        return result

# Time and Space -> O(k * n!/(n-k)! * k!)
        

