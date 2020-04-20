#设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。

#My:用字典来记录每个数出现的次数，更新；注意k=target-k的情况
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        #先转换为字典
        dic={}
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        res=[]
        for k in dic.keys():
            if target-k in dic and dic[target-k]>0 and dic[k]>0:
                while dic[target-k]>0 and dic[k]>0:
                    if k!=target-k:
                        res.append([k,target-k])
                        dic[k]-=1
                        dic[target-k]-=1
                    else:
                        if dic[k]>=2:
                            res.append([k,k])
                            dic[k]-=2
                        else:
                            dic[k]=0  #只有一个target/2，手动置零
        return res
        
        
#其他
#双指针法
#1.将数组排序
#2.定义双指针，初始化l=0，r=len(nums)-1
#3.遍历整个数组，若当前指针指引的元素和大于target，则右指针-1，小于target则左指针+1，相等则添加到结果中，同时将l+1，r-1。
#注：对于排序好的数组，第一次出现符合题意的数组时，也就限制了剩余其他可能的答案也在这个范围之内，范围之外的不用考虑了。
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == []:
            return []
        nums.sort()
        l,r,res = 0,len(nums)-1,[]
        while l<r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1 
            elif nums[l] + nums[r] == target:
                res.append([nums[l],nums[r]])
                l += 1
                r -= 1
        return res




