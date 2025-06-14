class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        original_k = nums.count(k)
        max_gain = 0
        for m in range(1, 51):
            if m == k:
                continue

            current = max_current = 0
            for num in nums:
                if num == m:
                    current += 1
                elif num == k:
                    current -= 1

                current = max(current, 0)
                max_current = max(current, max_current)
            max_gain = max(max_gain, max_current)

        return original_k + max_gain

# | Complexity Type | Value    |
# | --------------- | -------- |
# | Time            | **O(n)** | O(n) - > count, 50 * O(n) -> inner loop. Total -> O(n)
# | Space           | **O(1)** |

            

