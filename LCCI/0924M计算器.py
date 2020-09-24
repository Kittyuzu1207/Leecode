#给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
#表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分

#法1：使用栈处理
class Solution:
    def calculate(self, s: str) -> int:
        s += '+'        # 为了最后一个字符能被处理掉，一个小trick
        stack=[]
        ops2 = {'*': lambda x,y: x*y, '/': lambda x,y: int(x / y)}
        op,num='+',0  # 保存上一个操作符：如果上一个操作符是+-的话，按照正负直接放到stack中；如果是*/，运算之后再放
        for char in s:
            if char==' ':
                continue
            elif char.isdigit():
                num = num*10 + int(char)    # 累加数字到last
            else: #是运算符
                if op in ops2:
                    stack[-1] = ops2[op](stack[-1], num)
                if op == '-': num = -num
                    stack.append(num)
                    
                op=char
                num=0
         return sum(stack)



#法2：
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        s = deque(s)
        num = 0
        sign = "+"
        res = []
        for i in range(n):
            char = s.popleft()
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num = self.calculate(s)
            if (not char.isdigit() and char != " ") or not s:
                if sign == "+":
                    res.append(num)
                if sign == "-":
                    res.append(-num)
                if sign == "*":
                    res.append(res.pop() * num)
                if sign == "/":
                    res.append(int(res.pop() / num))
                num = 0
                sign = char
            if char == ")":
                break
        return sum(res)

