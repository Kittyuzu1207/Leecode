#插入。给定两个32位的整数N与M，以及表示比特位置的i与j。
#编写一种方法，将M插入N，使得M从N的第j位开始，到第i位结束。
#假定从j位到i位足以容纳M，也即若M = 10 011，那么j和i之间至少可容纳5个位。
#例如，不可能出现j = 3和i = 2的情况，因为第3位和第2位之间放不下M。

#位运算，不会

#先用0覆盖i-j之间bit位置，再将M左移i位合并
#首先，用0覆盖i-j之间你得先得到(j - i +1)bit长度的0且32位其他位都以为1，用2^{j - i + 1} - 1可以得到(j - i + 1)bit长度的1，
#再将其位反即可获得(j - i +1)bit长度的0（这里使用Python需要注意一下，Python的整数长度不是32，且大部分计算语言整数的首位都是表示正负，
#位反会变为负数，如0b1100100(100), -0b1100101(~100)，这里我使用0xFFFFFFFF掩码进行异或操作进行位反）
#最后再将N上位置覆盖为0，再与M合并

例如N=11001100 M=1001 i=2 j=5
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        temp = (1 << (j - i +1)) - 1   #tmp=1111
        mask = 0xFFFFFFFF
        temp = mask ^ (temp << i)      #=11000011
        M <<= i                        #M=00100100
        return (N & temp) | M          #=11000000 | 00100100=11100100


