class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)

        for num in count:
            if count[num] > n//2:
                return num

# Time -> O(n)
# Space -> O(n)
        
