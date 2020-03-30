#颜色填充。编写函数，实现许多图片编辑软件都支持的“颜色填充”功能。
#给定一个屏幕（以二维数组表示，元素为颜色值）、一个点和一个新的颜色值，将新颜色值填入这个点的周围区域，直到原来的颜色值全都改变。

#My：递归，但不能正确返回
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #递归
        self.helper(image,sr,sc,newColor)
        return image


    def helper(self,image,sr,sc,newColor): #把上下左右有颜色的都染色
        if image[sr][sc]!=0:
            image[sr][sc]=newColor
            try:
                if image[sr-1][sc]:
                    image[sr-1][sc]=newColor
                    self.helper(image,sr-1,sc,newColor)
            except:
                pass
            try:
                if image[sr+1][sc]:
                    image[sr+1][sc]=newColor
                    self.helper(image,sr+1,sc,newColor)
            except:
                pass
            try:
                if image[sr][sc-1]:
                    image[sr][sc-1]=newColor
                    self.helper(image,sr,sc-1,newColor)
            except:
                pass
            try:
                if image[sr][sc+1]:
                    image[sr][sc+1]=newColor
                    self.helper(image,sr,sc+1,newColor)
            except:
                pass
        else:
            return
            
#其他题解
#DFS 深度优先搜索
class Solution:
    direction = [[0,1],[1,0],[0,-1],[-1,0]]  #右->下->左->上
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n=len(image),len(image[0])
        oriColor=image[sr][sc]
        if oriColor==newColor:
            return image
        self.dfs(image,sr,sc,newColor,oriColor,m,n)
        return image
    
    def dfs(self,image,x,y,newColor,oriColor,m,n):
        image[x][y]=newColor
        for i in range(4):
            tx=x+self.direction[0]
            ty=y+self.direction[1]
            if(0 <= tx < m and 0 <= ty < n and image[tx][ty] == oriColor):
                self.dfs(image,tx,ty,newColor,oriColor,m,n)
        return
