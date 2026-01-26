class Solution:
    # Stack soln
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_idx = {num: i for i, num in enumerate(nums1)}
        result = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                value = stack.pop()
                idx = nums1_idx[value]
                result[idx] = curr

            if curr in nums1_idx:
                stack.append(curr)
        
        return result

# Time -> O(len(nums1) + len(nums2))
# Space -> O(len(nums1))
