#有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。
#注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

#My:利用迭代，把之前的都找出来  ,k较大的时候报错
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        if k==1:
            return 1
        else:
            ans=[1]
            i=1
            j=1 #因子的个数
            while i<=k:
                ans+=self.helper(j)
                ans=list(set(ans))
                j+=1
                i=len(ans)     
            ans=sorted(ans) 
            print(ans)      
            return ans[k-1]
    def helper(self,n): #n个因子产生的
        if n==1:
            return [3,5,7]
        else:
            tmp=self.helper(n-1)
            ans=[]
            for t in tmp:
                ans.append(3*t)
                ans.append(5*t)
                ans.append(7*t)
            return ans

#其他
#动态规划,丑数问题
#定义三个指针p3,p5,p7，p3指向的数字永远乘3，p5指向的数字永远乘5，p7指向的数字永远乘7
#初始化所有指针都指向第一个丑数，即1
#我们从dp[p3]*3,dp[p5]*5,dp[p7]*7选取最小的一个数字，作为新的丑数。这边新的丑数就是3*dp[p3]=3*1=3，然后p3++
#此时p5和p7指向第1个丑数，p3指向第2个丑数。然后重复上一步
#这里基于的一个事实是，丑数数列是递增的，当p5指针在当前位置时，后面的数乘以5必然比前面的数乘以5大，所以下一个丑数必然是先考虑前面的数乘以5。
#p3,p7同理，所以才可以使用指针
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        res = [1] * k
        idx3, idx5, idx7 = 0, 0, 0   # 分别表示能被3 5 7整除的数的下表
        for i in range(1, k):
            res[i] = min(res[idx3]*3, res[idx5]*5, res[idx7]*7)  # 最小的填充到当前位置
            
            if res[i] == res[idx3]*3:   # 如果3的倍数最小，那么当前是能被3整除的数，更新idx3
                idx3 += 1
            if res[i] == res[idx5]*5:   # 如果5的倍数最小，那么当前是能被5整除的数
                idx5 += 1
            if res[i] == res[idx7]*7: 
                idx7 += 1
        return res[k-1]

#那么每一行的指针就表示了有资格和 3，5，7 相乘的最小的丑数。比如 p_3=3，那就说明只有 f[3]f[3] 才有资格和 3 相乘，生成新的丑数，
#而之前的 f[2]f[2] 早就和 3 乘过了，再乘就重复了没有意义。但是可能这时 p_5=2，也就是 f[2]f[2] 还没和 5 乘过，所以还是有资格乘 5 生成新的丑数的。


