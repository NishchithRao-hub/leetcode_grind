class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n # Optional (efficient)

        def reverse(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1

        # Rotate entire array
        reverse(0, n-1)
        # Rotate only the first k elements
        reverse(0, k-1)
        # Rotate k to n elements
        reverse(k, n-1)

# Time -> O(n)
# Space -> O(1)
        
