class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        visited = set()
        maxArea = 0
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            area = 1
            print("loop")
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    directions =[[0,1], [0,-1], [1,0], [-1,0]]

                    for dr,dc in directions:
                        newRow, newCol = row + dr, col + dc
                        if (0 <= newRow < (rows) and
                            0 <= newCol < (cols) and 
                            grid[newRow][newCol] == 1 and 
                            (newRow, newCol) not in visited):
                            queue.append((newRow, newCol))
                            visited.add((newRow, newCol))
                            area += 1
            
            print(f"Area for ({r},{c}: {area})")
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:

                    area = bfs(r,c)
                    
                    maxArea = max(area, maxArea)
        return maxArea
