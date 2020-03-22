#编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。
#我：好像不太对
#既然题目提到：不得使用if-else或其他比较运算符，那么我们也尽可能回避abs、max这些函数，因为其内部可能调用比较了运算符。

#class Solution:
#    def maximum(self, a: int, b: int) -> int:
#        return max([a,b])

#其他题解
#思路：本质是平均值法
#max(a, b) = ((a + b) + abs(a - b)) / 2

#为了回避abs，利用位运算实现绝对值功能。
#<< : 左移运算符，num << 1,相当于num乘以2,表示加0
#>> : 右移运算符，num >> 1,相当于num除以2,表示减位
#^ 二进制异或运算
#int类型在内存中以补码的形式存储

#原码：计算机中一种对数字的二进制定点表示方法。原码表示法在数值前面前面有一位符号位（即最高位为符号位），正数该位为0，负数该位为1（0有两种表示：+0和-0），其
#余位表示数值的大小。
#反码：正数的反码与其原码相同；负数的反码是对其原码逐位取反，但符号位除外。
#补码：正数和+0的补码是其原码；负数则先计算其反码，然后反码加上1
class Solution:
    def maximum(self, a: int, b: int) -> int:
        k=(a-b)&(2**33)
        k=k>>33
        return k*b+a*(k^1)

#1.先看return语句，如果k==0，return值为a；如果k==1，return值为b.也就是说，如果a>b，我应该令k=0，否则令k=1.现在的问题是如何确定k的值呢？
#2.然后看第一和第二行。需要先了解int类型的存储方式，这个网上搜得到。理解以后，继续看：因为a和b均为int，也就是在[-2^{32},2^{32}-1]的区间内，可以确定a-b在
#(-2^{33},2^{33}-1)的区间内。
#2.1 如果a-b<0，那么a-b的左起33位必为1（负数的符号位为1），因此2^{33}和a-b进行一个与操作得到2^{33}，记录在k中。k右移33位得到1.
#2.2 否则a-b>0，那么a-b的左起33位必为0。此时k的值为0.
