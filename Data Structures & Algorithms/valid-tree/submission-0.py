class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = [[] for _ in range(n)]

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(node, parent):
            #to see a loop exists
            if node in visited:
                #print("loop")
                return False
            
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
                
            return True
        #n == len(visited), to checki all the nodes are connected()
        
        if dfs(0,-1) and (n == len(visited)):
            return True
        else:
            return False
        