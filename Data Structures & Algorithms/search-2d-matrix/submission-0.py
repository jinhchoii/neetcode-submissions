class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:

            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row)-1

                while left <= right:
                    middle = (left+right)//2

                    if target == row[middle]:
                        return True
                    elif target > row[middle]:
                        left = middle + 1
                    else:
                        right = middle - 1

        return False
