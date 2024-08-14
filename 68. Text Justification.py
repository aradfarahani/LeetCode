class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - current_length):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line, current_length = [], 0
            current_line.append(word)
            current_length += len(word)

        result.append(' '.join(current_line).ljust(maxWidth))
        return result

