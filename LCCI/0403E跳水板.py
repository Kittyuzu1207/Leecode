#你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，
#长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

#My:枚举容易，从小到大排列用sort是不是作弊。。。
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k==0:
            return []
        res=[]
        for i in range(0,k+1):
            res.append(shorter*i+(k-i)*longer)
        res=sorted(list(set(res)))
        return res
        
#其他
#确定上下限和间隔
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k==0:
            return []
        elif shorter==longer:
            return [k*shorter]
        return [i for i in range(shorter*k,longer*k+1,(longer-shorter))]

#递归：
 #只看递归思路，会超时
    def divingBoard2(self, shorter: int, longer: int, k: int) -> List[int]:
        # 0块板    0, 0
        # 1       shorter, longer
        # 2       rec(k-1)+shorter, rec(k-1)+longer
        def recursion(k):
            nonlocal re
            if k==0:return 0, 0
            if k==1:return shorter, longer
            min, max = recursion(k-1)
            return min+shorter, max+longer
        small, big = recursion(k)
        if longer-shorter==0 :return []
        re = list(range(small, big+1, longer-shorter))
        return re

