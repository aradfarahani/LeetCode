class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        sec = set(path[1] for path in paths)
        fir = set(path[0] for path in paths)
        ans = sec - fir
        return ans.pop()
        
