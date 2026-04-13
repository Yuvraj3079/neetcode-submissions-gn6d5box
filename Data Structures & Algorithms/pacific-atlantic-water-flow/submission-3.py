class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def bfs(r, c, visited, prevElement):
            #print(visited)
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or 
                (r,c) in visited or
                heights[r][c] < prevElement):
                return
            visited.add((r,c))
            
            bfs(r + 1, c, visited, heights[r][c])
            bfs(r - 1, c, visited, heights[r][c])
            bfs(r, c + 1, visited, heights[r][c])
            bfs(r, c - 1, visited, heights[r][c])
        
        for c in range(cols):
            bfs(0, c, pacific, heights[0][c])
            bfs(rows - 1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            bfs(r,0, pacific, heights[r][0])
            bfs(r, cols - 1, atlantic, heights[r][cols-1])
        res = []
        #print(f'{pacific} and {atlantic}')
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])
        return res
