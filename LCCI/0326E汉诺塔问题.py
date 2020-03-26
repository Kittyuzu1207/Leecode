#在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。
#一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
#(1) 每次只能移动一个盘子;
#(2) 盘子只能从柱子顶端滑出移到下一根柱子;
#(3) 盘子只能叠在比它大的盘子上。
#请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

#经典递归问题
#我：定义递归函数：从A移动n个盘子到B，借用C
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.move(A,C,B,len(A))

    #从A往B移动n个盘子,借用C
    def move(self,A,B,C,n):
        if n==1:
            B.append(A.pop())
        else:
            #借用C
            self.move(A,C,B,n-1)
            self.move(A,B,C,1)
            self.move(C,B,A,n-1)
