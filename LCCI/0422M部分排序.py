#给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。
#注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。

#My：
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n=len(array)
        for i in range(1,len(array)):
            if array[i]<max(array[:i]):
                n=i
        if n==len(array):
            return [-1,-1]
        m=-1
        if array[n]<min(array[:n]):
            m=0
            return [m,n]
        for i in range(len(array)-1):
            if array[i]<array[n] and array[i+1]>array[n]:
                m=i+1
                return [m,n]
        return [-1,-1]
        
        
#其他：
#我的思路基本正确了
#对于元素 a[i] 来说，如果它左边存在大于 a[i] 的元素，那么 a[i] 是一定要参与到排序里去的。
#或者说如果它右边存在小于 a[i] 的元素，那么 a[i] 也是要参与到排序里去的。
#所以我们只需要寻找最靠右的那个数（满足左边存在大于它的数），和最靠左的那个数（满足右边存在小于它的数），那么这两个数之间就是要排序的区间了。
#为什么最靠右的那个（满足左边存在大于它的数）数一定能保证右边没有更小的数了呢？因为如果右边还有更小的数，那么那个更小的数才是更靠右的啊，这就矛盾了。
#所以我们只需要从左到右扫描一遍，用一个变量维护一下最大值就行了，然后反向再遍历一遍，维护一个最小值。

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        maxx, minn = -10000000, 10000000
        l, r = -1, -1
        for i in range(n):
            if array[i] < maxx: r = i
            else: maxx = array[i]
        for i in range(n-1, -1, -1):
            if array[i] > minn: l = i
            else: minn = array[i]
        return [l, r]

