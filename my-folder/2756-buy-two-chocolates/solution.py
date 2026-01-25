class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float('inf')

        for price in prices:
            if price < min1:
                min1, min2 = price, min1
            elif price < min2:
                min2 = price

        saving = money - min1 - min2
        return saving if saving >= 0 else money

# Time -> O(n)
# Space -> O(1)    
