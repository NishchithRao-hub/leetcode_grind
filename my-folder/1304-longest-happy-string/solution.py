class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Greedy approach with max heap
        result = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                result += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
                heapq.heappush(maxHeap, (count, char))

            else:
                result += char
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))
        
        return result

# Time -> O(n)
# Space -> O(n) for o/p, O(1) extra space
        
