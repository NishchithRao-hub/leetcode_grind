class Solution:
    # Hash Set impl
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for num in nums:
            if num in result:
                return True
            result.add(num)
        return False

# Time -> O(n)
# Space -> O(n)
