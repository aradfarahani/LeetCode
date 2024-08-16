class Solution:
    def minStartValue(self, nums: List[int]) -> int:


        currSum = 0
        culmSum = []

        for i in range(0,len(nums)):
            currSum += nums[i]
            culmSum.append(currSum)

        currMin = min(culmSum)

        if currMin <= 0:
            return (-1*currMin) + 1
        else:
            return 1
