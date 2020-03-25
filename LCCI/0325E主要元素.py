#如果数组中多一半的数都是同一个，则称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。
#我：借助字典
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #借用python字典
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
                if dic[nums[i]]>len(nums)/2:
                    return nums[i]
            else:
                dic[nums[i]]=1
                if dic[nums[i]]>len(nums)/2:
                    return nums[i]
        return -1

#其他题解
#运用python3的count，sort方法，题目所求的数必然会位于sort后的数组的中间位置，然后我们就求这个数出现的次数，如果大于一半，就返回这个数；否则就返回-1

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        nums.sort()
        mid=int(len(nums)/2)
        if nums.count(nums[mid])>int(len(nums)/2):
            return nums[mid]
        else:
            return -1
       
#不sort只count也行
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        halflength = len(nums) / 2
        for i in set(nums):
            if nums.count(i) > halflength:
                return i
        return -1

