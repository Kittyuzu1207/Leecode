#设计一个算法，算出 n 阶乘有多少个尾数零。
#输入: 3
#输出: 0
#解释: 3! = 6, 尾数中没有零。

#输入: 5
#输出: 1
#解释: 5! = 120, 尾数中有 1 个零.

#My:超时了
class Solution:
    def trailingZeroes(self, n: int) -> int:
        #找有多少个5和偶数
        #1个2 和一个5乘得到一个0
        five=0
        even=0
        for i in range(1,n+1):
            five+=self.got_mod(i,5)
            even+=self.got_mod(i,2)
        return min(five,even)
    def got_mod(self,n,m):
        count=0
        while n>0:
            if n%m==0:
                count+=1
                n=n/m
            else:
                break
        return count
        
#其他题解：2的数量肯定比5多，只数5就行了
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 2的个数肯定小于5的个数，所以尾随零取决于5的个数
        cnt = 0
        divider = 5
        while n // divider:
            cnt += n // divider
            # 计算1~n中为5,25,125...的倍数的个数
            divider *= 5
        return cnt
