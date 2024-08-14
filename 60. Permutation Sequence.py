class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        # Create a list of numbers to get permutations from
        numbers = list(range(1, n + 1))
        # Convert k to zero-based index
        k -= 1
        # Initialize the result
        result = []
        
        # Generate the permutation
        for i in range(n, 0, -1):
            # Determine the index of the current digit
            idx = k // math.factorial(i - 1)
            # Append the digit to the result
            result.append(str(numbers[idx]))
            # Remove the used digit from the list
            numbers.pop(idx)
            # Update k
            k %= math.factorial(i - 1)
        
        return ''.join(result)
