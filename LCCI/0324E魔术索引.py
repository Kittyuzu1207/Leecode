#魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，
#如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

#我:直接遍历一遍,时间复杂度O（n）

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==i:
                return i
        return -1

#二分法：O(logn)
#假如不存在重复元素的话，则二分法很好实现，但此题存在重复元素，所以会比较复杂一点。
#对于 [0, 1, 4, 4, 4] 这个数组，使用二分法拿出位于中间的 idx 为 2 的数字 4，然后我们发现 nums[idx] > idx
#此刻我们除了可以确认 idx2 不是魔术索引外，还可以确定 idx3 也肯定不是魔术索引。因为假如 idx3 是魔术索引的话那 idx3 的值就必须是 3，
#这将导致 nums[idx3] < nums[idx2]，和题目的“递增数组”矛盾。
#所以，此刻魔术索引只可能出现在 [0, mid - 1] 和 [nums[mid], nums.length - 1] 这两个范围里。

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        return helper(nums,0,len(nums)-1)

def helper(nums,left,right):
    if left>right:
        return -1
    mid=int((left+right)/2)
    if mid==nums[mid]:  #mid肯定是，但mid之前也可能有(在left和right-1之间找)
        res1=mid
        res2=helper(nums,left,right-1)
        if res2==-1:
            return res1
        else:
            return res2
    elif mid<nums[mid]:  
#      mid 不是魔术索引，但 [left, mid - 1] 和 [nums[mid], right] 可能存在魔术索引
        res1=helper(nums,left,mid-1)
        if res1!=-1:
            return res1
        else:
            return helper(nums,nums[mid],right)
    else:
#     mid 不是魔术索引，但 [left, nums[mid]] 和 [mid + 1, right] 可能存在魔术索引
        res1=helper(nums,left,nums[mid])
        if res1!=-1:
            return res1
        else:
            return helper(nums,mid+1,right)
      
      
    
