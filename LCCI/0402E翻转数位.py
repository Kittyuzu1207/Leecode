#给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
#输入: num = 1775(11011101111)
#输出: 8
#输入: num = 7(0111)
#输出: 4

#不会...又要位运算

#法1：又要双指针
#pre表示上一个连续1的长度+1
#cur表示当前连续1的长度
#结果即为最大的pre+cur
#注意循环结束时需要再次更新res, 因为有可能最高位是1

class Solution:
    def reverseBits(self, num: int) -> int:
        pre, cur =0, 0
        res = 1
        for i in range(32):
            if num & (1<<i):            #1向前移动i位,其实就是取二进制的倒数第i位数
                cur+=1
            else:
                res=max(res, pre+cur)
                pre = cur +1
                cur = 0
        res=max(res, pre+cur)
        return res



