class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])  # Sort logs by time
        q_with_index = sorted([(q, i) for i, q in enumerate(queries)])

        res = [0] * len(queries)
        left = 0
        right = 0
        count = defaultdict(int)  # server_id -> count in window

        for q, idx in q_with_index:
            start_time = q - x
            end_time = q

            # Move `right` to include logs <= end_time
            while right < len(logs) and logs[right][1] <= end_time:
                server_id = logs[right][0]
                count[server_id] += 1
                right += 1

            # Move `left` to exclude logs < start_time
            while left < len(logs) and logs[left][1] < start_time:
                server_id = logs[left][0]
                count[server_id] -= 1
                if count[server_id] == 0:
                    del count[server_id]
                left += 1

            # Servers with 0 requests = total - number of keys in count
            res[idx] = n - len(count)

        return res

# Time:
# Sorting logs: O(L log L)
# Sorting queries: O(Q log Q)
# Each log processed at most once → O(L + Q)
# Total: O((L + Q) log(L + Q))

# Space:
# O(n) for server count map
# O(Q) for results


