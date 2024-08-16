class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        size = len(s)
        count = 0
        
        for index in range(0, size//2):
            if s[index] in vowels:
                count += 1

            if s[index + size//2] in vowels:
                count -= 1
        
        return count == 0
