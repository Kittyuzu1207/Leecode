#给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
#初始化 A 和 B 的元素数量分别为 m 和 n

#My:从头遍历，双指针，但结果总不对
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        #遍历A的同时插入B
        #设两个指针i和j
        i=0
        j=0
        k=m
        while j<n and i<m+n:
            if i>=k:
                    A[i:]=B[j:] #A已经遍历完，把B结尾加上即可
                    break
            if B[j]<A[i]:
                #插入
                A=A[:i]+[B[j]]+A[i:-1]
                j+=1
                k+=1
            else:
                i+=1
         
#其他题解
#双指针，用最大值开始比较
#使用 idx1 和 idx2 两个指针分别指向 A 和 B 的末端，每次将较大的数填充到 A 的末尾即可。
#当 A 已经填充完毕而 B 还有剩余时，直接将 B 的剩余部分填充到 A 的头部
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        idx1 = m - 1
        idx2 = n - 1
        cur = m + n - 1 # 添加 cur 指针追踪位置
        while idx1 > -1 and idx2 > -1:
            # print(A)
            if A[idx1] < B[idx2]:
                A[cur] = B[idx2]
                cur -= 1
                idx2 -= 1
            else:
                A[cur] = A[idx1]
                cur -= 1
                idx1 -= 1
        if idx2 != -1: A[:idx2 + 1] = B[:idx2 + 1] # 比较完B还有剩下的，全填到A前面即可
        return A

