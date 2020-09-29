#设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。
#机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。

#网格中的障碍物和空位置分别用 1 和 0 来表示。
#返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

#法1：DFS
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        ans,r,c=[],len(obstacleGrid),len(obstacleGrid[0])
        path=[[0,0]]
        def f(path):
           if not ans:
               i,j=path[-1]
               if not obstacleGrid[i][j]:
                    obstacleGrid[i][j]=1
                    if i<r-1:f(path+[[i+1,j]])
                    if j<c-1:f(path+[[i,j+1]])
                    if (i,j)==(r-1,c-1):
                        ans.extend(path)
        f([[0,0]])
        return ans


#法2：状态压缩
#主要思路同上，在数据规模较大时可以提升
#考虑到长宽最大只有一百，则可以把计算中的路径压缩，输出时再解压成二维数组。
#（不过又考虑到数据规模只有这么小，其实压缩了也不会有太显著的性能提升）
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        ans, m, r, c = [], 101, len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        def f(path):
            if not ans:
                p = path[-1]
                i, j = divmod(p, m)
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 1
                    j < c and f(path + [p + 1])
                    i < r and f(path + [p + m])
                    i == r and j == c and ans.extend([[p // m, p % m] for p in path])
        f([0])
        return ans

#法3：BP 动态规划
#遍历矩阵，用状态码2和3分别表示该点可以向下还是像右，最后回溯路径
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        ans,r,c=[],len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[-1][-1] != 0:
            return ans
        obstacleGrid[-1][-1]=2
        for i in reversed(range(r)):
            for j in reversed(range(c)):
                if obstacleGrid[i][j]>1:
                    if not obstacleGrid[i-1][j]:
                        obstacleGrid[i-1][j]=2
                    if not obstacleGrid[i][j-1]:
                        obstacleGrid[i][j-1]=3
        if obstacleGrid[0][0]>1:
            i,j=0,0
            while i<r and j<c:
                ans.append([i, j])
                if obstacleGrid[i][j]==2:
                    i+=1
                else:
                    j+=1
        return ans

            
