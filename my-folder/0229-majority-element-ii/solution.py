class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Frequency count
        count = Counter(nums)
        result = []

        for num in count:
            if count[num] > len(nums)//3:
                result.append(num)

        return result

# Time -> O(n)
# Space -> O(n)
        
