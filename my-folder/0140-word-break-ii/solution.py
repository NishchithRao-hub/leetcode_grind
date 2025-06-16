class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Backtracking solution
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                result.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                w = s[i: j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
                
        cur = []
        result = []
        backtrack(0)
        return result

# Component	                Time Complexity	        Space Complexity
# Convert wordDict to set	           O(m)	                    O(m)
# Backtracking recursive calls	   O(2^n)	            O(n) (stack)
# Sentence generation	              O(n * 2^n)	        O(2^n) (results)
# Total	                        O(m + n * 2^n)	            O(m + 2^n)
        
