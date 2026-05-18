class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                n = board[i][j]
                if n == ".":
                    continue
                if n in seen:
                    return False
                seen.add(n)

        for j in range(9):
            seen = set()
            for i in range(9):
                n = board[i][j]
                if n == ".":
                    continue
                if n in seen:
                    return False
                seen.add(n)

        for i_out in range(0, 9, 3):
            for j_out in range(0, 9, 3):
                seen = set()
                for i in range(i_out, i_out + 3):
                    for j in range(j_out, j_out + 3):
                        n = board[i][j]
                        if n == ".":
                            continue
                        if n in seen:
                            return False
                        seen.add(n)

        return True
