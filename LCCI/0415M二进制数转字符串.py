#二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。
#如果该数字不在0和1之间，或者无法精确地用32位以内的二进制表示，则打印“ERROR”。

#又是位运算，不会

#1.乘二取整法：十进制小数转二进制小数，应用常规方法乘二取整即可求解
#res初始化为"0."
#在满足位数要求的情况下，当num大于0时，循环
#先将num乘以2，将乘积赋值给num
#取num的个位（0或1），将对应的字符加入res的末尾
#截取num的小数部分，作为num的新值
#最后判断，当num为0时（即res已经精确地表达了num），返回res
#否则，返回"ERROR"

class Solution:
    def printBin(self, num: float) -> str:
        res, i = "0.", 30
        while num > 0 and i:
            num *= 2
            if num >= 1:
                res += '1'
                num -= 1
            else:
                res += '0'
            i -= 1
        return res if not num else "ERROR"
