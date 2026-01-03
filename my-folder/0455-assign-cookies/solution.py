class Solution:
    # Two pointers
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j == len(s):
                break
            i += 1
            j += 1

        return i

# Time -> O(nlogn + mlogn + (n+m)) = O(nlogn + mlogn) (sorting)
# (n = num of children and m is num of cookies)
# Space -> O(1) or O(n) based on sorting algo
        
