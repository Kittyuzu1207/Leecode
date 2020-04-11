#在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。
#例如，在数组{5, 8, 6, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。

#My:先排序，再粗暴分割，俺真的不知道.做出来虽然是交替，但和题目答案不一样
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums=sorted(nums)
        new=[]
        r=nums[len(nums)//2:]
        v=nums[:len(nums)//2]
        if len(nums)%2==1:
            for i in range(len(v)):
                new.append(r[i])
                new.append(v[i])
            new.append(r[-1])
        else:
            for i in range(len(v)):
                new.append(r[i])
                new.append(v[i])
        return new
        
#其他：
#尽量少地减少判断次数，遍历一次判断的同时交换
#现假设 a > b ? c ? d ? ...
#经过第一次交换后，得到 b<a ? c ? d? 
#  若 a>c， 则有 b< a > c ? d ? ...， 无需处理 a 和 c
#  若 a<c, 推出 b<a<c?d?..., 则交换 a,c 得到 b<c>a?d?.
#到这里，前两位已经处理好，接下来处理 > c?d?... or > a?d?
#  若 c<d 或者 a < d, 则在往后一位，无需处理
#  若 c>d 或者 a>d, 则需要交换 c d 或者 a d
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 可以证明峰谷交错的顺序总是可以实现的， 且同一组数，既可以 峰谷..., 也可以 谷峰...
        n = len(nums)
        if n <= 1:
            return None
        # 先要求0,2,4 为谷，1,3,5.. 为峰
        for i in range(1, n):
            if i%1 == 0 and nums[i-1] > nums[i]:  # 相同值无需处理，交不交换都一样
                nums[i-1], nums[i] = nums[i], nums[i-1]  # 交换两者的值
            if i%2 == 0 and nums[i-1] < nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1] # 交换两者的值
        


