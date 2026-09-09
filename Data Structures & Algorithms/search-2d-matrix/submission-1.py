class Solution:
    def binarySearch(self, row: List[int],target: int) -> bool:
        if not row:
            return False
        mid = len(row)//2
        if row[mid] == target:
            return True
        elif row[mid] > target:
            return self.binarySearch(row[:mid],target)
        else:
            return self.binarySearch(row[mid+1:],target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] == target:
                return True
            elif row[-1] > target:
                return self.binarySearch(row,target)

        return False
                    


        