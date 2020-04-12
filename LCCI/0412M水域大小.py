#你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。
#若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。
#编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

#My:与耕地问题类似，dfs，原来是四个方向，现在还要考虑对角线
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
    #和耕地的题目类似，迭代+DFS?
    #被计算过的要做个标记以免重复
        row=[1,1,1,0,0,-1,-1,-1]
        col=[-1,0,1,-1,1,-1,0,1]
        m,n=len(land),len(land[0])
        def dfs(x,y,land): #(x,y)是起始点的坐标
            if land[x][y]!=0:
                return 0
            else:
                count=1
                land[x][y]='*' #做标记
                for i in range(len(row)):
                    if -1<x+row[i]<m and -1<y+col[i]<n:
                        count+=dfs(x+row[i],y+col[i],land)       
                return count
        res=[]
        for i in range(m):
            for j in range(n):
                r=dfs(i,j,land)
                if r!=0:
                    res.append(r)
        return sorted(res)
        

