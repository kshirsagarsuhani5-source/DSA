class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        box_set = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur in row_set[i] or cur in col_set[j] or cur in box_set[(i//3) * 3 + j//3]:
                    return False
                row_set[i].add(cur)
                col_set[j].add(cur)
                box_set[(i//3) * 3 + j//3].add(cur)
        return True 
