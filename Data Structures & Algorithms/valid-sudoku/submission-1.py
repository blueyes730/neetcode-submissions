class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for square in range(9):
        #     init_row = (square // 3) * 3 # row index increases with division
        #     init_col = (square % 3) * 3 # col index increases with modulus
        #     visited = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = init_row + i
        #             col = init_col + j
        #             if board[row][col] == '.': continue
        #             if board[row][col] in visited: return False
        #             visited.add(board[row][col])
        
        # for row in range(9):
        #     visited = set()
        #     for col in range(9):
        #         if board[row][col] == '.': continue
        #         if board[row][col] in visited: return False
        #         visited.add(board[row][col]) 

        # for col in range(9):
        #     visited = set()
        #     for row in range(9):
        #         if board[row][col] == '.': continue
        #         if board[row][col] in visited: return False
        #         visited.add(board[row][col])   

        # return True       

        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):
                    if (board[row][col] == '.'): continue

                    curr = int(board[row][col]) - 1 # val has to be brought to 0-index for the bit representation
                    bit_shift = 1 << curr

                    if (bit_shift & rows[row]) or (bit_shift & cols[col]) or (bit_shift & squares[(row//3) * 3 + (col//3)]): 
                        # 2d->1d coord: row*total_col + col for squares
                        return False
                    
                    rows[row] |= bit_shift
                    cols[col] |= bit_shift
                    squares[(row//3)*3 + (col//3)] |= bit_shift
        
        return True



        