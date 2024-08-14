class Solution:
    def addOperators(self, num: str, target: int):
        def dfs(index, path, value, last):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break
                current_str = num[index:i+1]
                current_num = int(current_str)
                
                if index == 0:
                    dfs(i + 1, current_str, current_num, current_num)
                else:
                    dfs(i + 1, path + '+' + current_str, value + current_num, current_num)
                    dfs(i + 1, path + '-' + current_str, value - current_num, -current_num)
                    dfs(i + 1, path + '*' + current_str, value - last + last * current_num, last * current_num)
        
        result = []
        dfs(0, "", 0, 0)
        return result

# Example usage:
solution = Solution()
print(solution.addOperators("123", 6))  # Output: ["1*2*3","1+2+3"]
print(solution.addOperators("232", 8))  # Output: ["2*3+2","2+3*2"]
print(solution.addOperators("3456237490", 9191))  # Output: []
