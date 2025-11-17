class Solution:
    def calculate(self, s: str) -> int:
        # Stack solution
        stack = []
        num = 0
        op = "+"
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if (not char.isdigit()) or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                op = char
                num = 0

        return sum(stack)

# Time -> O(n)
# Space -> O(n)
        
