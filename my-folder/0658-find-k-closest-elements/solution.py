class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Two pointers
        left, right = 0, len(arr)-1

        while right - left >= k:
            if abs(x - arr[left]) <= abs(x - arr[right]):
                right -= 1
            else:
                left += 1
        
        return arr[left: right+1]

# Time -> O(n-k)
# Space -> O(k)
        
