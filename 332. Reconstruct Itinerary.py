from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        # Build the graph
        graph = defaultdict(list)
        for src, dst in sorted(tickets):
            graph[src].append(dst)
        
        # Result list to store the itinerary
        result = []
        
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop(0)
                dfs(next_airport)
            result.append(airport)
        
        # Start DFS from 'JFK'
        dfs('JFK')
        
        # The result list will be in reverse order
        return result[::-1]

# Example usage:
solution = Solution()
print(solution.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))  # Output: ["JFK","MUC","LHR","SFO","SJC"]
print(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))  # Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
