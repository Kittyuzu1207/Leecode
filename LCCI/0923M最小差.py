#给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

#法1：粗暴遍历，超出时间限制了
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        #遍历？
        u=a[0]
        v=b[0]
        diff=abs(u-v)
        for i in range(len(a)):
            for j in range(len(b)):
                if abs(a[i]-b[j])<diff:
                    diff=abs(a[i]-b[j])
                    u=a[i]
                    v=b[j]
        return diff
        
 #法2：先排序再搞，【排序+双指针】
 class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        res=float('inf')
        n=len(a)
        m=len(b)
        i,j=0,0
        while i<n and j<m:
            if a[i]>b[j]:
                res=min(res,a[i]-b[j])
                j+=1
            elif a[i]<b[j]:
                res=min(res,b[j]-a[i])
                i+=1
            else:
                return 0
        return res

