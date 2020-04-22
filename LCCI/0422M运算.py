#请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。
#你的实现应该支持如下操作：
#Operations() 构造函数
#minus(a, b) 减法，返回a - b
#multiply(a, b) 乘法，返回a * b
#divide(a, b) 除法，返回a / b

#My:会超时
class Operations:

    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        #小的那个数需要加多少个1才能加到大那个数
        if a==b:
            return 0
        if a>b:
            res=0
            while a>b:
                b+=1
                res+=1
            return res
        else:
            res=0
            while a<b:
                b+=-1
                res+=-1
            return res

    def multiply(self, a: int, b: int) -> int:
        max_,min_=max(a,b),min(a,b)
        res=0
        for i in range(min_):
            res+=max_
        return res      

    def divide(self, a: int, b: int) -> int:
        #a中有多少个b呗
        res=0
        flag=1
        if a<0 and b<0:
            a=self.minus(0,a)
            b=self.minus(0,b)
        if a>0 and b<0:
            b=self.minus(0,b)
            flag=-1
        if a<0 and b>0:
            a=self.minus(0,a)
            flag=-1
        while a >=b:
            a-=b
            res+=1
        return self.multiply(flag,res)

# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)

#其他：借助str
class Operations:
    def __init__(self):
        pass

    def calSign(self, a, b):
        pos = True
        if a < 0:
            pos = not pos
            a = self.minus(0, a)
        if b < 0:
            pos = not pos
            b = self.minus(0, b)
        return (a, b, pos)

    def minus(self, a: int, b: int) -> int:
        # 不用位运算 - 借助str
        if b < 0:
            b = int(str(b)[1:])
        else:
            b = int('-' + str(b))
        return a + b

    def multiply(self, a: int, b: int) -> int:
        # 不用位运算, 十进制乘法, 需要借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        sb = str(b)
        zerobits = 0
        for c in sb[::-1]:
            n = int(c)
            cur = 0
            for i in range(n):
                cur += a
            cur = int(str(cur) + '0' * zerobits)
            zerobits += 1
            res += cur
        return res if pos else self.minus(0, res)

    def divide(self, a: int, b: int) -> int:
        # 十进制除法, 借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        cur = 0
        for c in str(a):
            cur = self.multiply(10, cur) + int(c)
            cnt = 0
            while cur >= b:
                cur = self.minus(cur, b)
                cnt += 1
            res = self.multiply(10, res) + cnt
        return res if pos else self.minus(0, res)

#使用位运算
class Operations:
    def __init__(self):
        pass

    def calSign(self, a, b):
        pos = True
        if a < 0:
            pos = not pos
            a = self.minus(0, a)
        if b < 0:
            pos = not pos
            b = self.minus(0, b)
        return (a, b, pos)

    def minus(self, a: int, b: int) -> int:
        # 位运算做法 - 取反+1
        return a + ~b + 1

    def multiply(self, a: int, b: int) -> int:
        # 使用位运算的做法 - 二进制乘法, 类似十进制乘法
        a, b, pos = self.calSign(a, b)
        i = 0
        res = 0
        while b > 0:
            if b & 1:
                res += a << i
            i += 1
            b >>= 1
        return res if pos else self.minus(0, res)

        # 也可以递归, 相同思路
        a, b, pos = self.calSign(a, b)

        def multi(a, b):
            if not b:
                return 0
            return multi(a, b >> 1) << 1 + (a if b & 1 else 0)

        res = multi(a, b)
        return res if pos else self.minus(0, res)

    def divide(self, a: int, b: int) -> int:
        # 二进制除法, 使用一个变量保存被除数, 对该变量一直向左移位, 直到其<<1大于a为止, 然后res加上对应的倍数, a减去该变量的值, 直到a<b
        a, b, pos = self.calSign(a, b)
        i = 0
        res = 0
        while a >= b:
            curb = b
            times = 1
            while a >= curb << 1:
                curb <<= 1
                times <<= 1
            res += times
            a = self.minus(a, curb)
        return res if pos else self.minus(0, res)

