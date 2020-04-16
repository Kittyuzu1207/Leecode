#节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

#My:迭代,超时了
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        #用递归
        return self.helper(n,graph,start,target)
    def helper(self,n,graph,start,target):
        #从start到target是否有通路
        if [start,target] in graph:
            return True
        else:
            for i in range(n):
                if [start,i] in graph:
                    flag=self.helper(n,graph,i,target)
                    if flag:
                        return True
            return False


#其他：
#1.邻接表+BFS广度优先搜索
#思路：构建邻接表，将每个结点的邻接结点表示出来，便于后续遍历
#利用队列进行BFS，访问当前结点邻接结点，未访问过得结点加进队列，直至队列为空
#访问完当前结点的所有邻接结点，将该点visted置为1

#判定条件：能访问到目标结点——True
#1- visted[target]==1
#2- target in link_table[cur_node]
#遍历结束也没找到——False

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 构建邻接表
        link_table=[[] for _ in range(n)]
        for i,j in graph:
            link_table[i].append(j)
        queue=[start]
        visited=[0]*n
        while queue:
            cur=queue.pop()
            if target in link_table[cur]:
                return True
            for node in link_table[cur]:
                if visited[node]==0:
                    queue.insert(0,node)
            visited[cur_node] = 1
        return False

                
 #2. 邻接表+深度优先搜索
 class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        from collections import defaultdict
        dic = defaultdict(list)
        for g in graph:
            dic[g[0]].append(g[1])
        visted = [False] * n
        def dfs(vertex, visted):
            if vertex == target:
                return True
            if visted[vertex]:
                return False
            visted[vertex] = True
            ans = False
            for post in dic[vertex]:
                ans = ans or dfs(post, visted)
            return ans
        return dfs(start, visted)


         
