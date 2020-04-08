#给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
#不占用额外内存空间能否做到？
#e.g.
'''给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]'''

#My:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x=len(matrix)
        #原来的第i列->现在的第i行
        #我只能想到用额外内存空间的
        new=[]
        for j in range(0,x):
            tmp=[]
            i=x-1
            for i in range(x-1,-1,-1):
                tmp.append(matrix[i][j])
            new.append(tmp)
        for i in range(x):
            for j in range(x):
                matrix[i][j]=new[i][j]
                
 #其他 不占用额外空间
 #matrix 顺时针转 90 度就是矩阵先上下翻转，后沿对角线翻转。
 class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        # 先在纵向上进行上下翻转
        # 切片会创建新的对象进而开辟新地址
        matrix[:] = matrix[::-1]
        # 然后沿对角线翻转
        for i in range(length):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#！！！！！！！！！！！Python中赋值、深拷贝、浅拷贝、切片中的坑
(https://pic.leetcode-cn.com/27feb0233090917b7735a9d622e29162b5a2bbca04a1d3f821fa3470a23c1ea1-%E5%B9%BB%E7%81%AF%E7%89%871.PNG)
(https://pic.leetcode-cn.com/7f7e551bfec3e1a69667ae2d5ab6611529228057ec2bfe506f2faf56a5919e2f-%E5%B9%BB%E7%81%AF%E7%89%872.PNG)
