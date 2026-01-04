class Solution:
    # Sliding window
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        result = total

        while right < len(cardPoints):
            total += cardPoints[left] - cardPoints[right]
            result = max(result, total)
            left += 1
            right += 1

        return result

# Time -> O(k) (k is number of cards to pick)
# Space -> O(1)
        
