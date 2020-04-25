#下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。

#My:不会，又是位运算





#法1：位运算+字符串trick
class Solution:
    def findClosedNumbers(self, num):
        """
        较小数：找到 尽可能低位的 模式串'10' 翻转；若全为1则不存在更小数
        较大数：找到 尽可能低位的 模式串'01' 翻转，若全为1则加一位1，第二位1变0
        """
        b = str(bin(num))[2:]
        if not '0' in b:
            return [int('0b10'+b[1:], 2), -1]

        b = '0' + b
        smaller, bigger = None, None
        for i in range(len(b)-1, -1, -1):
            if b[i:i+2] == '10':
                tmp = b[i+2:]
                tmp = '1' * tmp.count('1') + '0' * tmp.count('0')
                smaller = b[:i] + '01' + tmp
                break
        for i in range(len(b)-1, -1, -1):
            if b[i:i+2] == '01':
                tmp = b[i+2:]
                tmp = '0' * tmp.count('0') + '1' * tmp.count('1')
                bigger = b[:i] + '10' + tmp
                break
        return [int(bigger, 2), int(smaller, 2)]

#不使用字符串的trick
#findLarger
#从低位到高位找, 如果找到01这个模式, 就可以构造了.如果找不到,那么需要分情况考虑下,下面数字都是二进制
#1 -> 10 # 未找到01, 返回1*2
#100 -> 1000 # 未找到01, 返回 100 * 2
#111 -> 1011 # 未找到01, 返回1011
#101 -> 110 # 找到01, 01->10
#1011100 -> 1100011 # 找到01, 01变成10, 在低位填充先0后1

#findSmaller
#从低位到高位找, 如果找到10这个模式,就可以构造了,如果没有这个模式,返回-1. 如下
#1 -> -1 # 未找到10
#10 -> 01 # 找到10, 返回01
#1011 -> 0111 # 找到10, 返回0111

class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:

        def findLarger(n):
            num_digits = num_zeros = num_ones = 0
            find_01 = False
            while n:
                num_digits += 1
                if n & 1:
                    num_ones += 1
                else:
                    num_zeros += 1
                    if num_ones:
                        n >>= 1
                        find_01 = True
                        break
                n >>= 1
            if find_01:
                n <<= 1
                n += 1
                for i in range(num_zeros):
                    n <<= 1
                for i in range(num_ones - 1):
                    n <<= 1
                    n += 1
                return n
            else:
                if num_ones == 1:
                    return 1 << num_digits
                else:
                    res = 2
                    for i in range(num_ones - 1):
                        res <<= 1
                        res += 1
                    return res

        def findSmaller(n):
            num_digits = num_ones = num_zeros = 0
            find_10 = False
            while n:
                num_digits += 1
                if not n & 1:
                    num_zeros += 1
                else:
                    num_ones += 1
                    if num_zeros:
                        find_10 = True
                        n >>= 1
                        break
                n >>= 1
            if find_10:
                n <<= 1
                for i in range(num_ones):
                    n <<= 1
                    n += 1
                for i in range(num_zeros - 1):
                    n <<= 1
                return n
            else:
                return -1

        return [findLarger(num), findSmaller(num)]


