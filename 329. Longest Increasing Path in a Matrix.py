class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]

        def dfs(x, y):
            if memo[x][y] != -1:
                return memo[x][y]

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            max_length = 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                    max_length = max(max_length, 1 + dfs(nx, ny))

            memo[x][y] = max_length
            return max_length

        return max(dfs(x, y) for x in range(rows) for y in range(cols))

# Example usage:
matrix1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
matrix2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
matrix3 = [[1]]

solution = Solution()
print(solution.longestIncreasingPath(matrix1))  # Output: 4
print(solution.longestIncreasingPath(matrix2))  # Output: 4
print(solution.longestIncreasingPath(matrix3))  # Output: 1
