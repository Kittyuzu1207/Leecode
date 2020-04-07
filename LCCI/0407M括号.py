#括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。
#说明：解集不能包含重复的子集。
#例如，给出 n = 3，生成结果为：

#[
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
#]

#My: 用递归解决
#执行用时 :32 ms, 在所有 Python3 提交中击败了98.39%的用户
#内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #用递归，在n-1对括号的基础上添加，使其合法
        return self.helper(n)
    def helper(self,n):
        if n==0:
            return []
        elif n==1:
            return ['()']
        else:
            res=[]
            tmp=self.helper(n-1)
            for bra in tmp:
                for i in range(len(bra)+1):
                    res.append(bra[:i]+'()'+bra[i:])
            res=list(set(res))
        return res
    
    
#其他题解：
#优化俺的迭代：
#f(n)比f(n-1)多一组括号。多出来的一组在哪里呢？
#我们把f(n-1)拆成f(a)和f(n-1-a)的两类的组合。其中a可以是0到n-1的任何一个.
#由于左面部分(f(a))由括号框起来的部分各不相同，所以最终结果不会有重复，不需要去重
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans =[]
        if n <=0:
            return [""]
        for i in range(0,n):
            for a in self.generateParenthesis(i):
                for b in self.generateParenthesis(n-1-i):
                    ans.append("("+a+")"+b) 
        return ans

#回溯法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        re = []
        state = ''
         def dsp(state, p, q):       #p,q分别表示(和)还剩的个数，有个隐含条件：就是(在组合时候比)用的多或相等
            if p > q:               #非法，剪枝
                return 
            if q == 0:              #)用完之时
                re.append(state)
            
            if p > 0:
                dsp(state+'(', p-1, q)
            if q > 0:
                dsp(state+')', p, q-1)

        dsp(state, n, n)
        return re



