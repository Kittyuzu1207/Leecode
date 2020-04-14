#设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
#My:用py排序偷懒
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]
        
#其他：
#法1：利用堆排序：
#思路：堆排序 复杂度O(nlogk)
#1.遍历输入数组，将前k个数插入到推中；
#2.继续从输入数组中读入元素做为待插入整数，并将它与堆中最大值比较：
#如果待插入的值比当前已有的最大值小，则用这个数替换当前已有的最大值；如果待插入的值比当前已有的最大值还大，则抛弃这个数，继续读下一个数。
#这样动态维护堆中这k个数，以保证它只储存输入数组中的前k个最小的数，最后输出堆即可。
import heapq
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k>len(arr) or k==0:
            return []
        heap = []
        for i in arr[:k]:
            heapq.heappush(heap, -i)
        for i in arr[k:]:
            if i < -heap[0]:
                heapq.heappop(heap)  #堆弹出最小元素，所以前面要取负数
                heapq.heappush(heap, -i)
        result = []
        for i in range(k):
            result.append(-heapq.heappop(heap))
        return result[::-1]

#法2：快速排序
#通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
#然后再按此方法对这两部分数据分别进行快速排序
#因为只要返回前k个小数，而无需这k个数间的顺序，所以应用快速排序的思想，对原数组的给定区间进行分块，当分块的点
#刚好等于k时，直接返回，否则对相应的子块进行递归分块。
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        def helper(arr, k, left, right):
            ##### 标准快速排序
            pivot = left
            low, high = left, left+1
            for high in range(left+1, right+1):
                if arr[high] < arr[pivot]:
                    low += 1
                    arr[low], arr[high] = arr[high], arr[low]
            arr[left], arr[low] = arr[low], arr[left]
            ###若当前分块长度不等于目标长度k，则根据情况进行下一步细分
            if low-left+1 < k:
                helper(arr, k-low+left-1, low+1, right)
            elif low-left+1 > k:
                helper(arr, k, left, low-1)
        
        if not arr or not k:
            return []
        helper(arr, k, 0, len(arr)-1)
        return arr[:k]
