
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]

        for r in range(9):
               for c in range(9):
                    num=board[r][c]

                    box_num=(r//3)*3+(c//3)
                    if num==".":
                         continue

                    if num in rows[r] or num in col[c] or num in boxes[box_num]:
                         return False
                    
                    rows[r].add(num)
                    col[c].add(num)
                    boxes[box_num].add(num)
        return True
