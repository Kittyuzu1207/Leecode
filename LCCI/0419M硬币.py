#硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
#和上楼梯问题类似的递归

#My:
#记忆化搜索卡了很久，使用一维记忆化的时候，总是出错，后来考虑到可能是记忆化过程中重复计算， 
#比如计算10的时候，1+1+1+1+1+5 和 5+1+1+1+1+1 计算了两次。

#动态规划二维的比较好理解
# dp[i][j] 代表使用前 i 种硬币能组成 j 的数量
# dp[i][0] = 1
# dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
# 不使用第 i 个硬币和使用第 i 个硬币的情况相加

class SolutionI:
    def waysToChange(self, n: int) -> int:
        # dp[i][j] 代表使用前 i 种硬币能组成 j 的数量
        # dp[i][0] = 1
        # dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        coins = [1, 5, 10, 25]
        dp = [[0 for _ in range(n+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 1

        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[-1][-1] % 1000000007
        
        
        
#为什么这样就不会重复呢?因为是把用第i种硬币和不用第i种分开了

