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
                if i < 3:
                    if j < 3:
                        if col in setsOf3x3[0]:
                            return False
                        setsOf3x3[0].add(col)
                    elif j<6:
                        if col in setsOf3x3[1]:
                            return False
                        setsOf3x3[1].add(col)
                    else:
                        if col in setsOf3x3[2]:
                            return False
                        setsOf3x3[2].add(col)
                elif i < 6:
                    if j < 3:
                        if col in setsOf3x3[3]:
                            return False
                        setsOf3x3[3].add(col)
                    elif j<6:
                        if col in setsOf3x3[4]:
                            return False
                        setsOf3x3[4].add(col)
                    else:
                        if col in setsOf3x3[5]:
                            return False
                        setsOf3x3[5].add(col)
                else:
                    if j < 3:
                        if col in setsOf3x3[6]:
                            return False
                        setsOf3x3[6].add(col)
                    elif j<6:
                        if col in setsOf3x3[7]:
                            return False
                        setsOf3x3[7].add(col)
                    else:
                        if col in setsOf3x3[8]:
                            return False
                        setsOf3x3[8].add(col)
                setsOfRows[i].add(col)
                setsOfColumns[j].add(col)
                j += 1
            i += 1

        return True
