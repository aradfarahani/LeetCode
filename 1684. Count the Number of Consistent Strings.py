class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        l=list(allowed)
        c=0
        for i in words:
            if set(i).issubset(l):
                c+=1
        return c
        
