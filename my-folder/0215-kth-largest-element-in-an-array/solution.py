class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # min heap solution
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]

# Time complexity = O(n log k)
# Space complexity = O(k)
        
