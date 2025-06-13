class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequency of each task
        count = Counter(tasks)

        # Step 2: Max-heap to always pick the task with highest remaining count
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Step 3: Queue to manage cooldown (cnt, ready_time)
        cooldown = deque()

        time = 0

        while maxHeap or cooldown:
            time += 1

            # Step 4: Check if any task is ready to come out of cooldown
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

            # Step 5: Execute the most frequent task if available
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  # reduce count (we use negative for maxHeap)
                if cnt:  # if more instances left, push to cooldown queue
                    cooldown.append([cnt, time + n + 1])  # task becomes ready again after n cycles + 1

        return time
        
