class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))

        time = -1

        while q:
            for _ in range(len(q)):
                print(f'{grid}')
                r,c = q.popleft()
                grid[r][c] = 2
                directions = [[0,1], [0,-1], [1,0], [-1,0]]

                for dr, dc in directions:

                    nRow, nCol = r+dr, c+dc

                    if (0 <= nRow < rows and
                        0 <= nCol < cols and
                        (nRow, nCol) not in visited and
                        grid[nRow][nCol] == 1
                        ):
                        q.append((nRow, nCol))
                        visited.add((nRow, nCol))
            time += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return time if time >=0 else 0


