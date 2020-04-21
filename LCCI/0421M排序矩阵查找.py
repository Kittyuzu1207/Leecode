#给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。
#e.g. matrix:
#[
#  [1,   4,  7, 11, 15],
#  [2,   5,  8, 12, 19],
#  [3,   6,  9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
#]
#给定 target = 5，返回 true。
#给定 target = 20，返回 false。

#My:偷懒，拉成一个列表检查
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tmp=[]
        for m in matrix:
            tmp+=m
        tmp=set(tmp)
        if target in tmp:
            return True
        else:
            return False
            
#其他
#从右上角的元素出发：
#（1）如果当前元素>目标值，说明这一列都大于目标值，向左移动一列
#（2）如果当前元素<目标值，说明这一列其他的元素有可能是目标值，向下移动一行
#终止条件: 找到了目标元素 或者 行或列越界
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) and len(matrix[0]): #特判一下矩阵为空的情况
            row = 0
            col = len(matrix[0]) - 1
            while row != len(matrix) and col != -1:
                if matrix[row][col] > target:
                    col -= 1
                elif matrix[row][col] < target:
                    row += 1   
                else:
                    return True
            return False
        else:
            return False


