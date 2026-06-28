class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        while l <= r:
            med = (r+l)//2
            if matrix[med][-1] < target:
                l = med + 1
            elif matrix[med][0] > target:
                r = med - 1
            else: break

        if not l<=r:
            return False

        row = (l+r)//2
        l, r = 0, len(matrix[0])-1


        

        while l <= r:
            med = (r+l)//2
            if matrix[row][med] > target:
                r = med - 1
            elif matrix[row][med] < target:
                l = med + 1
            else: return True
        
        return False