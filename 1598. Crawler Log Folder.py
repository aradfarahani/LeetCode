class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth -= 1 if depth > 0 else 0
            elif log == "./":
                depth += 0
            else:
                depth += 1
        return depth
