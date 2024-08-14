class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        # Regular expression for a valid number
        pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')
        return bool(pattern.match(s))
