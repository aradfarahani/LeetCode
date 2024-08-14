class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def findWords(self, board, words):
        def dfs(node, i, j):
            char = board[i][j]
            if char not in node.children:
                return
            node = node.children[char]
            if node.word:
                result.add(node.word)
                node.word = None  # Avoid duplicate entries
            
            board[i][j] = '#'  # Mark the cell as visited
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != '#':
                    dfs(node, x, y)
            board[i][j] = char  # Restore the cell
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(trie.root, i, j)
        
        return list(result)

# Example usage:
solution = Solution()
print(solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))  # Output: ["eat","oath"]
print(solution.findWords([["a","b"],["c","d"]], ["abcb"]))  # Output: []
