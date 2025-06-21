class Solution:
    def reorganizeString(self, s: str) -> str:
        # Max heap frequency count approach
        count  = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        result = ""

        while prev or maxHeap:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return result

# Time complexity = O(n)
# Space complexity = O(n) -> output, O(1) -> extra space
        
