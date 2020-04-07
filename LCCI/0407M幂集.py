#幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

#My:迭代
#执行用时 :9480 ms, 在所有 Python3 提交中击败了6.09%的用户
#内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums)
    
    def helper(self,nums): #找nums的所有子集
        if len(nums)==0:
            return [[]]
        elif len(nums)==1:
            return [[],nums]
        else:
            res=[nums]
            for i in range(len(nums)):
                a=[nums[i]]
                b=nums[:i]+nums[i+1:]
                res.append(a)
                res.append(b)
                res+=self.helper(b)
            #列表unhashable，不能直接去重
            fin=[]
            for item in res:
                if item not in fin:
                    fin.append(item)
            return fin

#其他：
#！！！！每一个新元素加到前面的元素上
#先在result列表中将入一个空子集
#然后遍历nums每一个元素，将元素与result中的每个元素结合加到result中
#直到nums遍历完
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        for i in nums:
            l = len(result)
            j = 0
            while j < l:
                result.append(result[j]+[i])
                j += 1
        return result


#for a list of [1,2,3,4,5]. Assuming we have the list of subsets of [2,3,4,5],
#the right answer is all subsets of [2,3,4,5] union the single-element-set [1] 
#union the result ([s+[1] for s in subsets([2,3,4,5])]) 本质就是俺的思路，人家写的更简洁
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:return [[]]
        temp=self.subsets(nums[1:])
        return [x+[nums[0]] for x in temp]+temp

#！！！！回溯法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path,res):
            res.append(path)
            if nums==[]:
                return
            for i in range(len(nums)):
                backtrack(nums[i+1:],path+[nums[i]],res)
        backtrack(nums, [], res)
        return res
