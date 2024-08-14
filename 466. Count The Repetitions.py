class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0

        s1_count, s2_count = 0, 0
        index = 0
        recall = {}

        while s1_count < n1:
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        s2_count += 1
                        index = 0
            s1_count += 1

            if index in recall:
                s1_prev, s2_prev = recall[index]
                cycle_len = s1_count - s1_prev
                cycle_count = (n1 - s1_prev) // cycle_len
                s1_count = s1_prev + cycle_count * cycle_len
                s2_count = s2_prev + cycle_count * (s2_count - s2_prev)

            recall[index] = (s1_count, s2_count)

        return s2_count // n2

# Example usage:
solution = Solution()
print(solution.getMaxRepetitions("acb", 4, "ab", 2))  # Output: 2
print(solution.getMaxRepetitions("acb", 1, "acb", 1))  # Output: 1
