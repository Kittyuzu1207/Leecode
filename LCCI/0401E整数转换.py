#整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B
#e.g. 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
# 输出：2

#输入：A = 1，B = 2
#输出：2

#又是位运算。。。。，不会

#法1：即求A与B异或的值中1的个数, 通过n&(n - 1)可以去掉一个数的二进制表示的最右边的一位1.（最后的一个1）
#注意：Python3 注意其对于负数的存储方式和 c++/c/java 不一样
#Python3 中的整型是补码形式存储的
#Python3 中 bin 一个负数（十进制表示），输出的是它的原码的二进制表示加上个负号
#所以你为了获得负数（十进制表示）的补码，需要手动将其和十六进制数 0xffffffff 进行按位与操作，
#得到结果是个十六进制数，再交给 bin() 进行输出，得到的才是你想要的补码表示。

#也可直接异或运算的结果和 0xffffffff 进行与运算，忽略符号位 

class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        tmp=(A^B) & 0xffffffff
        count=0
        while tmp!=0:
            tmp=tmp&(tmp-1)
            count+=1
        return count
