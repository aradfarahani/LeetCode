class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix, n):
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps

        current = 1
        k -= 1  # We start from the first number, so we need k-1 steps
        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        return current

# Example usage:
solution = Solution()
print(solution.findKthNumber(13, 2))  # Output: 10
print(solution.findKthNumber(1, 1))  # Output: 1
