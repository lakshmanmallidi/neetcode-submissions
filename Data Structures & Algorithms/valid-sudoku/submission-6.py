class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        board_2 = [set() for _ in range(rows)]
        board_sub = [set() for _ in range(rows)]
        for i in range(rows):
            row_hashset = set()
            for j in range(cols):
                if board[i][j] in row_hashset:
                    return False
                else:
                    if board[i][j] != '.':
                        row_hashset.add(board[i][j])
                if board[i][j] in board_2[j]:
                    return False
                else:
                    if board[i][j] != '.':
                        board_2[j].add(board[i][j])
                sub_idx = ((i//3)*3) + j//3
                if board[i][j] in board_sub[sub_idx]:
                    print(sub_idx,i,j)
                    return False
                else:
                    if board[i][j] != '.':
                        board_sub[sub_idx].add(board[i][j])
                print(board_sub)
        return True
                