class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setsOfRows = [set() for _ in range(9)]
        setsOfColumns = [set() for _ in range(9)]
        setsOf3x3 = [set() for _ in range(9)]
        i = 0
        for row in board:
            j=0
            for col in row:
                if col ==".":
                    j += 1
                    continue
                if col in setsOfRows[i]:
                    return False
                if col in  setsOfColumns[j]:
                    return False
                if col in setsOf3x3[(i // 3) * 3 + (j // 3)]:
                    return False
                setsOf3x3[(i // 3) * 3 + (j // 3)].add(col)
                setsOfRows[i].add(col)
                setsOfColumns[j].add(col)
                j += 1
            i += 1

        return True
