class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # MinHeap implementation
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if count.get(i, 0) == 0:
                    return False
                count[i] -= 1
            
            for i in range(first, first + groupSize):
                if count[i] == 0:
                    heapq.heappop(minHeap)
            
        return True

# Time -> O(nlogn)
# Space -> O(n)
        
