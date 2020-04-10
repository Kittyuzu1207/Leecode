#给定N个人的出生年份和死亡年份，第i个人的出生年份为birth[i]，死亡年份为death[i]，实现一个方法以计算生存人数最多的年份。
#你可以假设所有人都出生于1900年至2000年（含1900和2000）之间。
#如果一个人在某一年的任意时期都处于生存状态，那么他们应该被纳入那一年的统计中。
#例如，生于1908年、死于1909年的人应当被列入1908年和1909年的计数。
#如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。

#示例：
#输入：
#birth = {1900, 1901, 1950}
#death = {1948, 1951, 2000}
#输出： 1901

#My:用字典来记录每一年的人数
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        #用字典来存储，每一年生存的人数
        start=min(birth)
        end=max(death)
        live={}
        for i in range(start,end+1):
            live[i]=0
        for i in range(len(birth)):
            for j in range(birth[i],death[i]+1):
                live[j]+=1
        return max(live,key=live.get)
        
#其他：
#改进1：只记录有人数变化的年份，字典记录人数的变化值
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        dic = collections.defaultdict(int)
        
        for c in birth:
            dic[c]+=1
        for c in death:
            dic[c+1]-=1
        
        maxn = 0
        cur =0
        res = -1
        for i in range(1900,2001):
            cur+=dic[i]
            if cur>maxn:
                res=i
                maxn = cur
                
        return res

#法2：双指针
#先对出生和死亡时间排序 时间复杂度o(log(n));
#然后设置两个指针指向出生序列和死亡序列，出生时间<=死亡时间时，总人口+1，否则-1；
#并且设置一个标记，记录总人口最大时的序列号。
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        i=0
        j=0
        sum=0
        max=0
        flag=0;
        birth=list(sorted(birth))
        death=list(sorted(death))
        while i <len(birth):
            if birth[i]<=death[j]:
                sum+=1
                if max<sum:
                    max=sum
                    flag=i
                i+=1
            elif birth[i]==death[j]:
                i+=1
                j+=1
            
            else:
                j+=1
                sum-=1        
        return birth[flag]



