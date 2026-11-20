class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        elementsI = defaultdict(set)
        elementsJ = defaultdict(set)
        elementsIJ = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (board[i][j] in elementsI[i] or 
                board[i][j] in elementsJ[j] or 
                board[i][j] in elementsIJ[(i//3,j//3)]):
                    return False
                elementsI[i].add(board[i][j])
                elementsJ[j].add(board[i][j])
                elementsIJ[(i//3,j//3)].add(board[i][j])
                
        return True
                

