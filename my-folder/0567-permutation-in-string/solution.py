class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len1])

        if count_s1 == count_s2:
            return True

        # Slide the window through the rest of s2
        for i in range(len1, len2):
            # Add the new character at the right end of the window
            count_s2[s2[i]] += 1
            # Remove the character at the left end of the window
            count_s2[s2[i - len1]] -= 1
            # If a character's count becomes zero, remove it to keep the map clean
            if count_s2[s2[i - len1]] == 0:
                del count_s2[s2[i - len1]]

            # Check if the frequency maps are equal
            if count_s1 == count_s2:
                return True

        return False

# Time -> O(n+m) (n=len of s1, m=len of s2)
# Space -> O(1)
