class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        if len(arr) == 1:
            return res
        maxLen = arr[len(arr)-1]
        for i in range(len(arr) - 2, -1, -1):
            maxLen = max(maxLen, arr[i+1])
            res[i] = maxLen
        return res
        
