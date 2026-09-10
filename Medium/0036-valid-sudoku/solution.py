class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9,3):
            for col in range(0,9,3):
                m=set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j]=='.':
                            continue
                        if board[i][j] in m:
                            return False
                        m.add(board[i][j])
        for i in range(0,9):
            m=set()
            for j in range(0,9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in m:
                    return False
                m.add(board[i][j])
        for i in range(0,9):
            m=set()
            for j in range(0,9):
                if board[j][i]=='.':
                    continue
                if board[j][i] in m:
                    return False
                m.add(board[j][i])
        return True
    

