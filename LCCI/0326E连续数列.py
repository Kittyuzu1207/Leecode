#给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。
#输入： [-2,1,-3,4,-1,2,1,-5,4]
#输出： 6
#解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

#my:傻瓜遍历法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #从每一个数字开始往后判断
        max_=nums[0]
        for i in range(len(nums)):
            for j in (i,len(nums)):
                s=sum(nums[i:j+1]) #i到j求和
                if s>max_:
                   max_=s
                #if sum(nums[i+1:j+1])>s:
                #    break #跳到下一个i
        return max_

#法1：动态规划DP，一趟遍历，时间O（n），空间O（1）
#思路：累加，当累加值大于等于0的时候，直接累加并及时更新max值，当累加值小于0的时候，放弃当前累加值。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_=-inf
        sum_=0
        for i in nums:
            sum_=max(sum_+i,i)  #取i就是抛弃前面的，即不能抵消的情况
            max_=max(max_,sum_)
        return max_
        
#法2：同上
#状态:dp[i]表示到nums[i]为止的连续数列最大和
#初态:dp[0] = nums[0]
#状态转移方程:dp[i] = max(nums[i],dp[i-1]+nums[i])考虑到前面的和可能有负数
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)

#法3：分治法
#分治的基本思想就是将大问题化解为小问题，小问题继续化解，复杂问题简单化。
#任意一个序列，最大子序列只有3种情况
#1.出现在数组左边；
#2.出现在数组右边；
#3.出现在数组中间部分，即横跨左右；
#那么我们要求的其实就是这三者中的最大值，即求数组左边的最大值，数组右边的最大值，数组中间部分的最大值。
#将数组划分为左右两部分，便可求得左右子数组的最大，在求左右子数组的过程中，leftsum,rightsum均从中间向两端相加，那么
#leftsum+rightsum即为中间部分相加的最大值。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSub(nums,0,len(nums)-1)
    def maxSub(self,nums,left,right):
        maxleftbordersum,maxrightbordersum=-inf,-inf
        maxleftsum,maxrightsum=-inf,-inf
        leftsum,rightsum=0,0
        mid=(left+right)//2
        if left==right:
            return nums[left]
        leftmax=self.maxSub(nums,left,mid)
        rightmax=self.maxSub(nums,mid+1,right)
        i=mid
        while i>=left:
            leftsum+=nums[i]
            if leftsum > maxleftbordersum:
                maxleftbordersum=leftsum
            i-=1
        i=mid+1
        while i<=right:
            rightsum+=nums[i]
            if rightsum>maxrightbordersum:
                maxrightbordersum=rightsum
            i+=1
        return max(leftmax,max(rightmax,maxleftbordersum+maxrightbordersum))
