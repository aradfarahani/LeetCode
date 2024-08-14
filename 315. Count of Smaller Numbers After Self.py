class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        
        # Normalize the values to be within the range of the Fenwick Tree
        offset = 10**4  # To handle negative values
        size = 2 * 10**4 + 1  # Range of values from -10^4 to 10^4
        fenwick_tree = FenwickTree(size)
        result = []
        
        for num in reversed(nums):
            rank = num + offset
            result.append(fenwick_tree.query(rank - 1))
            fenwick_tree.update(rank, 1)
        
        return result[::-1]

# Example usage:
solution = Solution()
print(solution.countSmaller([5, 2, 6, 1]))  # Output: [2, 1, 1, 0]
print(solution.countSmaller([-1]))          # Output: [0]
print(solution.countSmaller([-1, -1]))      # Output: [0, 0]
