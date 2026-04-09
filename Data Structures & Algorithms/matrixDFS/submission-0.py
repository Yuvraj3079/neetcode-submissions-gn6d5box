class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, r, c, visited):
            row, col = len(grid), len(grid[0])

            if (min(r,c) < 0 or
                r == row or c == col or
                (r,c) in visited or 
                grid[r][c] == 1):
                return 0
            #We have reached the bottom right corner
            if r == row -1 and c == col - 1:
                return 1
            
            count = 0
            visited.add((r,c))

            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r, c - 1, visited)

            visited.remove((r,c))
            return count
        
        return dfs(grid, 0, 0, set())