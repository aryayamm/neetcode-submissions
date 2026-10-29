class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = []
        l = 0
        r = len(matrix) - 1
        if len(matrix) == 1:
            mat = matrix[0]
        else:
            while l <= r:
                m = (l+r)//2
                if matrix[m][0] <= target <= matrix[m][len(matrix[0])-1]:
                    mat = matrix[m]
                    break
                elif matrix[m][len(matrix[0])-1] < target:
                    l = m+1
                elif matrix[m][0] > target:
                    r = m-1
        l = 0
        r = len(mat) - 1
        while l <= r:
            m = (l+r)//2
            if mat[m] == target:
                return True
            elif mat[l] < target:
                l = m+1
            else:
                r = m-1
        return False

