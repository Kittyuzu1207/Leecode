#三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
#实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

#My:注意规避重复计算的问题,超时了

class Solution:
    def waysToStep(self, n: int) -> int:
        #必然需要递归
        return self.helper(n)
    def helper(self,n):
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 4
        else:
            return (self.helper(n-1)+self.helper(n-2)+self.helper(n-3))%1000000007
 
 
#这道题次要考察动态规划，主要是考察为什么可以在过程中取模而不影响最终结果
class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0]*n
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3,n):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000007
        return dp[n-1] 

