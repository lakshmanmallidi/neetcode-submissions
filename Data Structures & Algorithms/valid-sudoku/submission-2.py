class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_box = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        for i in range(0, 9):
            row_hash_set = set()
            col_hash_set = set()
            for j in range(0, 9):
                if (board[i][j] in row_hash_set) or (board[j][i] in col_hash_set):
                    return False
                else:
                    if board[i][j]!='.':
                        row_hash_set.add(board[i][j])
                        m = (i//3)*3
                        n = j//3
                        sb_idx = m+n
                        if board[i][j] in sub_box[sb_idx]:
                            return False
                        else:
                            sub_box[sb_idx].add(board[i][j])
                    if board[j][i]!='.':
                        col_hash_set.add(board[j][i])
        return True
         