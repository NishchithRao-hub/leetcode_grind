class Solution:
    def decodeString(self, s: str) -> str:
        # Two Stacks
        string_stack = []
        count_stack = []
        curr = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k*10 + int(char)
            elif char == "[":
                string_stack.append(curr)
                count_stack.append(k)
                curr = ""
                k = 0
            elif char == "]":
                temp = curr
                curr = string_stack.pop()
                count = count_stack.pop()
                curr += temp * count
            else:
                curr += char

        return curr   

# Time -> O(n + N) (n is input length and N is output length)
# Space -> O(n + N)  
        
