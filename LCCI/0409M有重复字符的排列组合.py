#有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
#e.g. 输入：S = "qqe"
#输出：["eqq","qeq","qqe"]

#My:直接用回溯法，再去重
class Solution:
    def permutation(self, S: str) -> List[str]:
        
        res=[]
        path=''
        def backtrack(S,path,res):
            if len(S)==0:
                res.append(path)
                return 
            for i in range(len(S)):
                backtrack(S[:i]+S[i+1:],path+S[i],res)
        backtrack(S,path,res)
        return list(set(res))
        
#其他
#递归
#首先确定排列中的首位，然后求剩下的字符所能构成的所有排列，把它们一一接到首位后面即可。
#注意在遍历所有可能的首位时，不要有重复。
class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S) == 0:
            return ['']
        ans = [S[0] + t for t in self.permutation(S[1:])]
        for i in range(1, len(S)):
            if S[i] not in S[:i]:
                t = S[1:i]+S[0]+S[i+1:]
                ans += [S[i] + k for k in self.permutation(t)]
        return ans
#回溯
ans = []
S = sorted(S) #先排序，加快速度

def backtrack(r, s):
     if not len(s):
        ans.append(r)
     else:
        pre = ''
        for i in range(len(s)):
            if s[i] != pre:  #主要是这里的修改，增加了一个判断
                 backtrack(r + s[i], s[:i] + s[i + 1:])
              pre = s[i]

        backtrack('', S)
        return ans

