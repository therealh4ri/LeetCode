class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        A = set()

        for r in range(9):
            for c in range(9):
                if board[r][c]!='.':
                    a = board[r][c]
                    row = a + 'in row'+ str(r)
                    col = a + 'in col'+ str(c)
                    box = a + 'in box'+ str(r//3)+'-'+str(c//3)
                    if row in A or col in A or box in A:
                        return False
                    A.add(row)
                    A.add(col)
                    A.add(box)
        return True
