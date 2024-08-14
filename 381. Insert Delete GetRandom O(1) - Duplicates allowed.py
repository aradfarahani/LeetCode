import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.indices[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        remove_idx = self.indices[val].pop()
        last_val = self.nums[-1]
        self.nums[remove_idx] = last_val
        self.indices[last_val].add(remove_idx)
        self.indices[last_val].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Example usage:
randomizedCollection = RandomizedCollection()
print(randomizedCollection.insert(1))  # Output: True
print(randomizedCollection.insert(1))  # Output: False
print(randomizedCollection.insert(2))  # Output: True
print(randomizedCollection.getRandom())  # Output: 1 or 2
print(randomizedCollection.remove(1))  # Output: True
print(randomizedCollection.getRandom())  # Output: 1 or 2
