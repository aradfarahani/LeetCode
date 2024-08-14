class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Create a new string which is the original string + a separator + the reverse of the original string
        new_s = s + "#" + s[::-1]
        
        # Compute the KMP table (partial match table)
        kmp_table = [0] * len(new_s)
        for i in range(1, len(new_s)):
            j = kmp_table[i - 1]
            while j > 0 and new_s[i] != new_s[j]:
                j = kmp_table[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            kmp_table[i] = j
        
        # The length of the longest prefix which is also a suffix
        longest_prefix_suffix = kmp_table[-1]
        
        # Add the necessary characters in front of the original string to make it a palindrome
        return s[longest_prefix_suffix:][::-1] + s

# Example usage:
solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
print(solution.shortestPalindrome("abcd"))  # Output: "dcbabcd"
