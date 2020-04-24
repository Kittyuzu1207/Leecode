#编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。
#e.g
#输入: 25
#输出: 9
#解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)

#My:简单粗暴 对每个数的每一位判断,超时了
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        #挨着对每个数字的每一位做判断
        count=0
        for i in range(n+1):
            count+=self.helper(i)
        return count
    
    def helper(self,num):  #判断一个数有多少个2
        count=0
        while num>0:
            r=num%10
            if r==2:
                count+=1
            num=(num-r)/10
        return count
        
        
#其他
#动态规划
#dp数组11*10，dp[i][j]：第i位为j的2的个数
#状态转移方程：
#if j≠2：dp[i][j] = dp[i-1][0~9]
#else：dp[i][j] = dp[i-1][0~9] + 10**(i-1)
#计算个数时从高数位向低数位遍历，并且需要特判当前位为2的情况，只需将结果加上低于当前位的数再加一（加一为0的情况）。
#例如：n=5263，从千分位5向个位3遍历，当遇到百分位为2时，结果加上63+1，即200~263共64个百分位为2的数。
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        tmp = n
        dp = [[0] * 10 for _ in range(11)]
        for i in range(1, 11):
            ss = 0
            for k in range(10):
                ss += dp[i - 1][k]
            for j in range(10):
                if j == 2:
                    dp[i][j] = ss + 10**(i - 1)
                else:
                    dp[i][j] = ss
        nums = [0]
        while n != 0:
            nums.append(n%10)
            n //= 10
        ans = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i]==2:
                ans += tmp%(10**(i-1))+1
            for j in range(nums[i]):ans += dp[i][j]
        return ans

###下面这一种比较好理解:2在个位的情况，2在十位的情况(10**1),2在百位的情况(10**2)....
#根据每一位b来计算当前位为2时候的个数(只考虑当前位的2)
#对于xby来说, 需要判断b与2的大小, 左边部分的个数是int(x), 如果b>2的话需要+1(即0~x之间的所有数都满足), 右边部分为10**len(y), 左边部分*右边部分的个数即为所求
#注意需要特殊处理b==2的情况, 需要加上左边部分恰好为x时右边的个数, 即为int(y)+1
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        res = 0
        s = str(n)
        for i in range(len(s))[::-1]:
            c = s[i]
            left = 0 if i == 0 else int(s[0:i])
            if c > '2':
                left += 1
            res += left * (10**(len(s) - i - 1))
            if c == '2':
                right = int(s[i + 1:]) + 1 if i + 1 < len(s) else 1
                res += right
        return res

