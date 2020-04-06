#无重复字符串的排列组合。
#编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同

#My:
class Solution:
    def permutation(self, S: str) -> List[str]:
        #迭代的方法，长度为n的则是在长度为n-1的基础上在各个位置插入得到的
        return self.helper(S)
    def helper(self,s):
        if len(s)==1:
            return [s]
        else:
            tmp=self.helper(s[1:])
            res=[]
            for string in tmp:
                for i in range(len(string)):
                    res.append(string[:i]+s[0]+string[i:])
                res.append(string+s[0])
            return res
            
#其他
#回溯法：
#回溯法其实就是对一个树形图的深度遍历dfs
#我们在每次进行回溯的时候需要对每个点保存两个变量
#1、path:局部变量，记录了包含了当前节点的路径（包含了当前节点）
#2、res:全局变量，记录满足条件的所有路径
#把问题转换成树形图，问题将很清晰明了，相当于直接对树进行DFS， 这里每个节点相当于到该节点时的路径
class Solution:
    def permutation(self, S: str) -> List[str]:
        if S == '':return []
        res = []
        path = ''
        def backtrack(S, path, res):
            if S == '':
                res.append(path)
                return 

            for i in range(len(S)):
                cur = S[i]
                backtrack(S[:i] + S[i+1:], path + cur, res)
                
        backtrack(S, path, res)

        return res



