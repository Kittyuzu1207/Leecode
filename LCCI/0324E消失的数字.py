#数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗
#我：先排序，再按照类似二分法  超出时间限制
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #先排序再用类似二分法
        for i in range(len(nums)-1):
            min_idx=i
            min_val=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]<min_val:
                   min_idx=j
                   min_val=nums[j]
            tmp=nums[i]
            nums[i]=min_val
            nums[min_idx]=tmp

        #如果没有缺失，则序号=值,若mid=nums[mid]，则问题在后半部分，否则在前半部分
        left=0
        right=len(nums)-1
        while left < right:
            mid=int((left+right)/2)
            if mid==nums[mid]:
                left=mid+1
            else:
                right=mid
        if nums[left]==left:
            return nums[left]+1
        else:
            return nums[left]-1
            
 
#其他题解
#法1：
#利用两次异或等于本身的性质
#构建一个顺序列表
#对res从0-nums.length进行异或。i 是顺序列表,nums[i] 是输入列表
#利用两个相同的数求异或（^）会变为0，而0与任何数m求异或都是m。
#那么将数列从头至尾、0~numsSize（让存在的数字能出现第二遍）取异或，最后的结果一定是缺失的数。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       res = 0
       for i in range(len(nums)):
           res ^= i
           res ^=nums[i]
       res ^= len(nums)
       return res
       
#法2：数组预期和减去现有所有就是缺失数
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nsum = len(nums)*(len(nums)+1)/2
        for i in nums:
            nsum=nsum-i
        return int(nsum)

