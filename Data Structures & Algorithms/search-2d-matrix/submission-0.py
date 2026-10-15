class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=(m*n)-1

        while left<=right:
            mid=(left+right)//2
            row=mid//n
            col=mid%n

            if matrix[row][col]<target:
                mid+=1
                left=mid
            elif matrix[row][col]>target:
                mid-=1
                right=mid
            else:
                return True

        return False