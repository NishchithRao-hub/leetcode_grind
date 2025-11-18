class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Sliding window approach
        currSum = sum(arr[:k-1])
        counter = 0

        for left in range(0, len(arr) - k+1):
            currSum += arr[left + k-1]
            if currSum >= k * threshold:
                counter += 1
            currSum -= arr[left]

        return counter 

# Time -> O(n)
# Space -> O(1)
        
