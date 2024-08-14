class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        
        count = 0
        factor = 1
        
        while factor <= n:
            lower_numbers = n - (n // factor) * factor
            current_digit = (n // factor) % 10
            higher_numbers = n // (factor * 10)
            
            if current_digit == 0:
                count += higher_numbers * factor
            elif current_digit == 1:
                count += higher_numbers * factor + lower_numbers + 1
            else:
                count += (higher_numbers + 1) * factor
            
            factor *= 10
        
        return count

# Example usage:
solution = Solution()
print(solution.countDigitOne(13))  # Output: 6
print(solution.countDigitOne(0))   # Output: 0
