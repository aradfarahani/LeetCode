class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        categories = int(has_lower) + int(has_upper) + int(has_digit)
        
        if n < 6:
            return max(6 - n, 3 - categories)
        
        if n <= 20:
            replace = 0
            i = 2
            while i < n:
                if password[i] == password[i - 1] == password[i - 2]:
                    replace += 1
                    i += 3
                else:
                    i += 1
            return max(replace, 3 - categories)
        
        delete = n - 20
        replace = 0
        one_seq = two_seq = 0
        i = 2
        
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                
                if length % 3 == 0:
                    one_seq += 1
                elif length % 3 == 1:
                    two_seq += 1
                replace += length // 3
            else:
                i += 1
        
        use_one_seq = min(one_seq, delete)
        replace -= use_one_seq
        delete -= use_one_seq
        
        use_two_seq = min(two_seq * 2, delete)
        replace -= use_two_seq // 2
        delete -= use_two_seq
        
        return (n - 20) + max(replace, 3 - categories)

# Example usage:
solution = Solution()
print(solution.strongPasswordChecker("a"))  # Output: 5
print(solution.strongPasswordChecker("aA1"))  # Output: 3
print(solution.strongPasswordChecker("1337C0d3"))  # Output: 0
