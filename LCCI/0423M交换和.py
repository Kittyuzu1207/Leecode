#给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
#返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。
#若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组

#My:先算两个数组和的差值,超时了
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1=sum(array1)
        sum2=sum(array2)
        diff=sum1-sum2
        if diff%2==1:
            return []
        for a in array1:
            if a-diff/2 in array2:
                return [a,a-int(diff/2)]
        return []
        
        
#其他
#1.思路和我一样，人家先set了，减小了查找范围 时间O(N),空间O(N)
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        x = sum(array2) - sum(array1)
        if x % 2 == 1:
            return []
        x /= 2
        a = set(array1)
        for num in array2:
            if num - x in a:
                return [num - x, num]
        return []

#2.排序+双指针法，时间O(Nlog(N))，空间O(1)
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        x = sum(array2) - sum(array1)
        if x % 2 == 1:
            return []
        x /= 2
        # 方法1：时间O(Nlog(N))，空间O(1)
        i = j = 0
        array1.sort()
        array2.sort()
        while j < len(array2):
            if array2[j] - array1[i] == x:
                return [array1[i], array2[j]]
            elif array2[j] - array1[i] > x and i+1 < len(array1):
                i += 1
            else:
                j += 1
        return []

