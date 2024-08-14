class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def backtrack(s, start, l, r):
            if l == 0 and r == 0:
                if is_valid(s):
                    result.add(s)
                return
            
            for i in range(start, len(s)):
                if i != start and s[i] == s[i - 1]:
                    continue
                if s[i] in ('(', ')'):
                    curr = s[:i] + s[i + 1:]
                    if r > 0 and s[i] == ')':
                        backtrack(curr, i, l, r - 1)
                    elif l > 0 and s[i] == '(':
                        backtrack(curr, i, l - 1, r)

        l = r = 0
        for char in s:
            if char == '(':
                l += 1
            elif char == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        
        result = set()
        backtrack(s, 0, l, r)
        return list(result)

# Example usage:
solution = Solution()
print(solution.removeInvalidParentheses("()())()"))  # Output: ["(())()","()()()"]
print(solution.removeInvalidParentheses("(a)())()"))  # Output: ["(a())()","(a)()()"]
print(solution.removeInvalidParentheses(")("))  # Output: [""]
