class Solution:
    def countLargestGroup(self, n: int) -> int:

        # This method provides the sum of the digits of a number
        def sumDigits(number: int) -> int:

            return sum([int(d) for d in str(number)])
        
        # We initializate a dictionary to group the number by sumDigits
        freq = {}

        for j in range(1, n+1):

            sumD = sumDigits(j)

            if sumD in freq:
                freq[sumD] += [sumD]
            else: 
                freq[sumD] = [sumD]
        
        # We look at the number of elements with a given digitSum
        groupLenght = [len(val) for val in freq.values()]

        # We return the number of the largest groups
        return groupLenght.count(max(groupLenght))
