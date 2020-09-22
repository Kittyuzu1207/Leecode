#下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）
#输入：num = 2（或者0b10）
#输出：[4, 1] 或者（[0b100, 0b1]）

#法1：位运算
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        mn, mx = 1, 2147483647

        def findLarge(n):
            # 从右开始找到第1个1
            # 然后记录1的个数ones直到再遇到0或到最高位
            # 然后将这个0变成1
            # 然后右边的位数用000...111(ones-1个1)填充
            checkMask = 1
            bits = 0
            while checkMask <= n and checkMask & n == 0:
                checkMask <<= 1
                bits += 1
            ones = 0  # 直接构造出000...111
            while checkMask <= n and checkMask & n != 0:
                ones = (ones << 1) + 1
                checkMask <<= 1
                bits += 1
            # 因为在改变的位已经将1个0转成1了, 所以这里ones要向右移动一位
            ones >>= 1
            # 将0转成1
            n |= checkMask
            # 清除右边的0
            n = (n >> bits) << bits
            # 将右边填充上ones
            n |= ones
            return n if mn <= n <= mx else -1

        def findSmall(n):
            # 从右开始找到第1个0, 记录此过程1的个数ones
            # 然后继续往左找直到再遇到1
            # 然后将这个1变成0, ones也要左移一位(也可以初始化为1)
            # 然后右边的位数用高位ones个1填充, 即构造出111...000, 可以直接基于ones构造
            # 注意如果全为1的话是无解的, 直接返回-1
            checkMask = 1
            bits = 0
            ones = 1
            while checkMask <= n and checkMask & n != 0:
                checkMask <<= 1
                bits += 1
                ones = (ones << 1) + 1
            if checkMask > n:
                # 全部是1
                return -1
            while checkMask <= n and checkMask & n == 0:
                checkMask <<= 1
                bits += 1
                ones <<= 1
            # 因为ones初始化为1, 所以ones需要右移一位
            ones >>= 1
            # 将需要改变的1变成0
            n &= ~checkMask
            # 清除右边的0
            n = (n >> bits) << bits
            # 将右边填充上ones
            n |= ones
            return n if mn <= n <= mx else -1

        return [findLarge(num), findSmall(num)]


#法2：*******用bin().count()
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        left, right = num+1, num-1
        n = bin(num).count('1')
        while(bin(left).count('1')!= n):   left += 1
        while(right > 0 and bin(right).count('1')!= n ):  right -= 1
        right = -1 if right == 0 else right
        
        return left,right
