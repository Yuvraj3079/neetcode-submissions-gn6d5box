class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        used =[False] * (row * col)
        res = False
        def backtrack(r, c, i):

            if (i) == len(word):
                return True
            
            if not (0 <= r < row and 0 <= c < col) or board[r][c]!=word[i]:
                return False
            #mark visited
            board[r][c] = "#"

            found = (backtrack(r + 1, c, i + 1) or 
                    backtrack(r - 1, c, i + 1) or 
                    backtrack(r, c + 1, i + 1) or 
                    backtrack(r, c - 1, i + 1)) 
            board[r][c] = word[i]
            return found

            
        
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
                
        return False