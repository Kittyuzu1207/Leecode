#递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。
#可以使用加号、减号、位移，但要吝啬一些。

#My:把乘法变加法【可是我没有用递归啊。。。。】
class Solution:
    def multiply(self, A: int, B: int) -> int:
        res=0
        x,y=min(A,B),max(A,B)   #这一步是精髓
        for i in range(x):   #把for循环改成递归即可
            res+=y
        return res
     
     
#其他：
class Solution:
    def _multiply(self, A: int, B: int) -> int:
        if B == 0:
            return 0
        elif B == 1:
            return A
        else:
            return A + self._multiply(A, B-1)   #这里用递归

    def multiply(self, A: int, B: int) -> int:
        if A < 0 and B < 0:
            A, B = abs(A), abs(B)
        if A < B:
            A, B = B, A
        if B < 0:
            return 0 - self._multiply(A, B)
        else:
            return self._multiply(A, B)

\
