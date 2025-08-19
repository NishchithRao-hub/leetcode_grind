class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Counting sort + Two pointer greedy        
        m = max(people)
        count = [0] * (m+1)
        for p in people:
            count[p] += 1

        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            idx += 1
            count[i] -= 1

        result = 0
        l, r = 0, len(people)-1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            result += 1
            if l <= r and remain >= people[l]:
                l += 1

        return result

# Time = O(n) -> (n=size of input array)
# Space = O(m) -> (m=maximum value in array)
        
