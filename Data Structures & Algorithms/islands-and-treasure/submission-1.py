class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        print(f'[{rows},{cols}] and Queue: {q}')
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                print(f'Queue: {q} Distance: {dist}')
                grid[r][c] = dist

                directions = [[0,1], [0,-1], [1,0], [-1,0]]

                for dr, dc in directions:
                    nRow, nCol = r + dr, c+ dc
                    
                    if ( 0 <= nRow < rows and 
                        0 <= nCol < cols and
                        (nRow,nCol) not in visited and
                        grid[nRow][nCol] == 2147483647 ):
                    
                        q.append((nRow,nCol))
                        visited.add((nRow,nCol))
            dist += 1

                    
                
