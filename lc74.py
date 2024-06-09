class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1
        while l<=r:
            mid = (l+r)//2
            i, j = mid//n, mid%n
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                r-=1
            elif matrix[i][j]<target:
                l+=1
        
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))