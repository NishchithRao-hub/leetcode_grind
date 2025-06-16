class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Two pointer solution
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

# Time complexity = O(n)
# Space complexity = O(1)
        
        
