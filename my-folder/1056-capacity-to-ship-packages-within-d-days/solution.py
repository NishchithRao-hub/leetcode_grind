class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search
        least, most = max(weights), sum(weights)
        result = most

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True

        while least <= most:
            cap = (least+most) // 2
            if canShip(cap):
                result = min(result, cap)
                most = cap - 1
            else:
                least = cap + 1
        
        return result

# Time -> O(nlogn)
# Space -> O(1)
        
