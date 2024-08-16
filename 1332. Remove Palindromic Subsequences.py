class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s[::-1] == s: return 1
        else: return 2
