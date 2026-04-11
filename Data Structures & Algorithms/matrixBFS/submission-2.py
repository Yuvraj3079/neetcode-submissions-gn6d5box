class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        queue = collections.deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        
        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                if r == row -1 and c == col -1:
                    return length
                neighbours = [[-1,0], [0,-1], [1,0], [0,1] ]
                for dr, dc in neighbours:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == row or c + dc == col or
                        (r + dr,c + dc) in visited 
                        or grid[r + dr][c + dc] == 1
                    ):
                        continue
                    queue.append((r + dr,c + dc))
                    visited.add((r + dr,c + dc))
            length += 1
        
        return -1


