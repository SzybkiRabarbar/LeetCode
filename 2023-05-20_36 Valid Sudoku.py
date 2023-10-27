#https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #T: 26.32% M:33.25%
        for ir, row in enumerate(board):
            temp_row=[]
            for ic, column in enumerate(row):
                #print(ic)
                if column in temp_row: return False
                if column!=".": temp_row.append(column)
                temp_column=[]
                for x in range(ir,9):
                    #print(f"x={x}, bic={board[x][ic]}, tc={temp_column}")
                    if board[x][ic] in temp_column: return False
                    if board[x][ic]!=".": temp_column.append(board[x][ic])
        for x in range(0,9,3):
            for y in range(0,9,3):
                ##print(f"{x}:{y}")
                temp=[]
                for row in range(3):
                    for col in range(3): 
                        if board[row+x][col+y]!=".": temp.append(board[row+x][col+y])
                if len(temp)!=len(set(temp)): return False
        return True
                
                

if __name__=="__main__":
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    t=Solution()
    print(t.isValidSudoku(board))