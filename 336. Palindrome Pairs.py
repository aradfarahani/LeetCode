class Solution:
    def palindromePairs(self, words):
        def is_palindrome(word):
            return word == word[::-1]
        
        word_to_index = {word: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                
                # If prefix is a palindrome, check if reverse of suffix exists
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_index and word_to_index[reversed_suffix] != i:
                        result.append([word_to_index[reversed_suffix], i])
                
                # If suffix is a palindrome, check if reverse of prefix exists
                # Check j != len(word) to avoid duplicates
                if j != len(word) and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_index and word_to_index[reversed_prefix] != i:
                        result.append([i, word_to_index[reversed_prefix]])
        
        return result

# Example usage:
solution = Solution()
print(solution.palindromePairs(["abcd","dcba","lls","s","sssll"]))  # Output: [[0,1],[1,0],[3,2],[2,4]]
print(solution.palindromePairs(["bat","tab","cat"]))  # Output: [[0,1],[1,0]]
print(solution.palindromePairs(["a",""]))  # Output: [[0,1],[1,0]]
