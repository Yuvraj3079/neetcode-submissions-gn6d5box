class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        adj = [[] for _ in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(node):
            
            visited.add(node)

            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        result = 0
        for node in range(n):
            if node not in visited:
                result += 1
                dfs(node)
        return result