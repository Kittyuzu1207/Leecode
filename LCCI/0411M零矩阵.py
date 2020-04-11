#编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
#My:粗暴，先找到位置再清零
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #粗暴，先找出那些是0，做好标记，再清零
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:  
                    row.append(i)
                    col.append(j)
        row=list(set(row))
        col=list(set(col))
        for r in row:
            matrix[r]=[0]*len(matrix[0])
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c]=0
                
#其他
#思路基本一样，写法更简洁，直接用set存
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       #出现0的行列
        row = len(matrix)
        col = len(matrix[0])
        z_row={i for i in range(row) for j in range(col) if matrix[i][j]==0}
        z_col={j for i in range(row) for j in range(col) if matrix[i][j]==0}

        for i in range(row):
            if i in z_row:
                matrix[i] = col*[0]
                continue
            for j in z_col:
                matrix[i][j]=0

