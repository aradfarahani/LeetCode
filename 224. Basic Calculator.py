class Solution:
    def calculate(self, s: str) -> int:
        def update(op, val):
            if op == '+':
                return val
            if op == '-':
                return -val
            return 0
        
        stack = []
        num, op = 0, '+'
        s += '+'
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-':
                stack.append(update(op, num))
                num, op = 0, char
            elif char == '(':
                stack.append(op)
                stack.append('(')
                num, op = 0, '+'
            elif char == ')':
                stack.append(update(op, num))
                num = 0
                while stack and stack[-1] != '(':
                    num += stack.pop()
                stack.pop()  # pop '('
                op = stack.pop() if stack and stack[-1] in '+-' else '+'
                stack.append(update(op, num))
                num = 0
        
        return sum(stack)

# Example usage:
solution = Solution()
print(solution.calculate("1 + 1"))  # Output: 2
print(solution.calculate(" 2-1 + 2 "))  # Output: 3
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
