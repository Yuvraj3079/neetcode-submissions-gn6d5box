class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        countIslands = 0

        visited = set()

        def bfs(r,c):
            visited.add((r,c))
            queue = deque()
            queue.append((r,c))

            while queue:
                for _ in range(len(queue)):

                    row, col = queue.popleft()

                    directions = [[0,1], [0,-1], [1,0], [-1,0]]

                    for dr, dc in directions:
                        newRow, newCol = row + dr, col + dc

                        if (newRow in range(rows) and 
                            newCol in range(cols) and
                            (newRow, newCol) not in visited and
                            grid[newRow][newCol] == "1"):
                            queue.append((newRow, newCol))
                            visited.add((newRow, newCol))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    countIslands += 1
        
        return countIslands