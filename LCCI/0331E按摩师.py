#一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
#给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

#My:动态规划，迭代，但是超时了
class Solution:
    def massage(self, nums: List[int]) -> int:
        #有点动态规划的赶脚？
        if len(nums)==0:
            return 0
        tmp=[]
        for i in range(len(nums)):
            tmp.append(self.helper(nums[i:]))
        return max(tmp)

    def helper(self,nums): #选择了nums的首个元素后的最佳选择
        if len(nums)==0:
            return 0
        if len(nums)==1 or len(nums)==2:
            return nums[0]
        else:
            choice=[]
            for i in range(2,len(nums)):
                choice.append(nums[0]+self.helper(nums[i:]))
            return max(choice)

#其他题解：
#动态规划问题，考虑相邻状态的转移方程
#法1：
#我们本质上在解决对于第[i] 个人，我接待还是不接待。
#对于接待的话就是当前接待的的价值 + dp[i - 2]
#如果不接待的话，就是dp[i - 1].
#dp[i]=max(dp[i-1],dp[i-2]+nums[i-2])
#注：这里为了方便计算，令 dp[0]和 dp[1]都等于 0,所以 dp[i]对应的是 nums[i - 2]
class Solution:
    def massage(self, nums: List[int]) -> int:
        dp=[0]*(len(nums)+2)
        for i in range(2,len(dp)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-2])
        return dp[-1]

#法2:在1的基础上再优化下空间，空间优化到O(1)
class Solution {
    public int massage(int[] nums) {
        int a = 0, b = 0;
        for (int i = 0; i < nums.length; i++) {
            int c = Math.max(b, a + nums[i]);
            a = b;
            b = c;
        }
        return b;
    }
}





