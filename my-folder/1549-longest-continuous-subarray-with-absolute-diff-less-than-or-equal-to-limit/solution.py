class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Deque sliding window
        increasing  = deque([nums[0]])
        decreasing  = deque([nums[0]])
        left = 0

        for right in range(1, len(nums)):
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()
            
            increasing.append(nums[right])
            decreasing.append(nums[right])

            if decreasing[0] - increasing[0] > limit:
                if decreasing[0] == nums[left]:
                    decreasing.popleft()
                if increasing[0] == nums[left]:
                    increasing.popleft()
                left += 1
        
        return len(nums) - left

# Time -> O(n)
# Space -> O(n)
        
