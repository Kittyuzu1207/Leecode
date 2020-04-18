#给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。
#设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，
#若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。

#My:暴力遍历法,但检测不通过....
class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        #直线的方程可以写出来....暴力遍历
        max_=0
        S_=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                count,S=self.online(points,points[i],points[j])
                if count>max_:
                    max_=count
                    S_=S
        return S_[:2]
    def online(self,points,start,end):
        #满足直线方程的点个数
        count=0
        S=[]
        if start[0]==end[0]:
            #直线是x=start[0]
            for i in range(len(points)):
                if points[i][0]==start[0]:
                    count+=1
                    S.append(i)
            return count,S
        else:
            #y=kx+b
            k=(end[1]-start[1])/(end[0]-start[0])
            b=end[1]-k*end[0]
            for i in range(len(points)):
                if points[i][1]==k*points[i][0]+b:
                    count+=1
                    S.append(i)
            return count,S


#hash表，用一个字典保存已找到的所有直线的出现次数，和其穿过的下标最小的两个点的下标
#遍历所有点对，更新字典及最优解
#时间复杂度：O(n^2)
#空间复杂度：O(n^2)
class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        d = {}
        x = y = 0
        maxCount = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                k, b = self.f([points[i], points[j]])
                if (k, b) in d.keys():
                    d[(k, b)][0] += 1
                else:
                    d[(k, b)] = [1, (i, j)]
                if d[(k, b)][0] > maxCount or (d[(k, b)][0] == maxCount and d[(k, b)][1][0] < x) or (d[(k, b)][0] == maxCount and d[(k, b)][1][1] < y):
                    maxCount = d[(k, b)][0]
                    x, y = d[(k, b)][1]
                print(x, y)
        return [x, y]

    # 求两点之间连线的k和b
    def f(self, points: List[List[int]]) -> List[int]:
        if points[0][0] == points[1][0]:
            return [float('inf'), points[0][0]]
        else:
            return [(points[1][1]-points[0][1]) / (points[1][0]-points[0][0]),
            (points[0][1]*points[1][0]-points[1][1]*points[0][0]) / (points[1][0]-points[0][0])]

