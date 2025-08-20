class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search optimal soln
        A, B = nums1, nums2
        total_length = len(A) + len(B)
        half = total_length // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half-i-2

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if i+1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if j+1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total_length % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1

# Time -> O(log min(m, n)) n - length of nums1, m - length of nums2
# Space -> O(1)
        
