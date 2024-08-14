from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        wordList.add(beginWord)
        
        # Build the graph
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                neighbors[pattern].append(word)
        
        # BFS to find the shortest path
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for neighbor in neighbors[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        
        return 0
