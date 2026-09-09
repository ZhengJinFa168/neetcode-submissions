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
        if not matrix:
            return False

        mid = len(matrix)//2
        row = matrix[mid]
        if row[-1] == target:
            return True
        elif target < row[0]:
            return self.searchMatrix(matrix[:mid],target)
        elif row[-1] < target:
            return self.searchMatrix(matrix[mid+1:],target)
        else:
            return self.binarySearch(row,target)
                    