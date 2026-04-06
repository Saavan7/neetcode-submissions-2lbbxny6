class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_row(board):
            for i in range(len(board)):
                valid_row=set()
                for j in range(len(board)):
                    if board[i][j]!='.':
                        if board[i][j] in valid_row:
                            return False
                        else:
                            valid_row.add(board[i][j])
            return True

        def valid_column(board):
            for i in range(len(board)):
                valid_column=set()
                for j in range(len(board)):
                    if board[j][i]!='.':
                        if board[j][i] in valid_column:
                            return False
                        else:
                            valid_column.add(board[j][i])
            return True
        
        def valid_square(board):
            for row in range(0,len(board),3):
                for column in range(0,len(board),3):
                    valid_square=set()
                    for i in range(0,3):
                        for j in range(0,3):
                            if board[i+row][j+column]!='.':
                                if board[i+row][j+column] in valid_square:
                                    return False
                                else:
                                    valid_square.add(board[i+row][j+column])
            return True

        return valid_row(board) and valid_column(board) and valid_square(board)

