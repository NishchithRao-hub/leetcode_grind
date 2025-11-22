class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Stack solution
        s = list(s)
        stack = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
            
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)

# Time -> O(n)
# Space -> O(n)
        
