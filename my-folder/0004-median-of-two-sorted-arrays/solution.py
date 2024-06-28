class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        for _ in range(0, (n+m)//2 + 1):
            m2 = m1
            if i<n and j<m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i<n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1
        
        if (n+m)%2 == 1:
            return float(m1)
        else:
            res = float(m1) + float(m2)
            return res/2.0

#Solution2: Brute Force - Merge and Sort. 
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         # Merge the arrays into a single sorted array.
#         merged = nums1 + nums2

#         # Sort the merged array.
#         merged.sort()

#         # Calculate the total number of elements in the merged array.
#         total = len(merged)

#         if total % 2 == 1:
#             # If the total number of elements is odd, return the middle element as the median.
#             return float(merged[total // 2])
#         else:
#             # If the total number of elements is even, calculate the average of the two middle elements as the median.
#             middle1 = merged[total // 2 - 1]
#             middle2 = merged[total // 2]
#             return (float(middle1) + float(middle2)) / 2.0
        
