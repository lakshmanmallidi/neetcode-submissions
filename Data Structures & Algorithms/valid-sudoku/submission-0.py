class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box = [[],[],[],[],[],[],[],[],[]]
        for i in range(0, 9):
            row_hash_set = set()
            col_hash_set = set()
            for j in range(0, 9):
                if (board[i][j] in row_hash_set) or (board[j][i] in col_hash_set):
                    return False
                else:
                    if board[i][j]!='.':
                        row_hash_set.add(board[i][j])
                        m = i//3
                        n = j//3
                        sub_box[(m*3)+n].append(board[i][j])
                    if board[j][i]!='.':
                        col_hash_set.add(board[j][i])
        for i in range(0,9):
            sub_box_set = set()
            for j in range(0, len(sub_box[i])):
                if sub_box[i][j] in sub_box_set:
                    return False
                else:
                    sub_box_set.add(sub_box[i][j])
        return True
         