#配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。
#e.g. 输入：num = 2（或者0b10）  输出 1 (或者 0b01)
#e.g. 输入：num = 3   输出：3

#不太会
#题解
#法1：利用0x55555555 和 0xaaaaaaaa 分别取出奇数位和偶数位
#0x55555555 = 0b0101_0101_0101_0101_0101_0101_0101_0101
#0xaaaaaaaa = 0b1010_1010_1010_1010_1010_1010_1010_1010
#然后位左移奇数位，右移偶数位，
#再把奇数位和偶数位做或运算。
#>>> : 无符号右移,也叫逻辑位移，忽略符号位，空位都以0补齐

#e.g. 1001 1010 
#odd= 0001 0000   0dd<<1=   0010 0000
#even=1000 1010   even>>>1= 0100 0101
#odd | even =0110 0101

class Solution:
    def exchangeBits(self, num: int) -> int:
        odd=num&0x55555555
        even=num&0xaaaaaaaa
        odd=odd<<1
        even=even>>>1
        return odd|even
        
#法2：思路是每次取num的最后一位，通过计数器count右移到相应的位置后，与ans进行或操作。
class Solution:
    def exchangeBits(self, num: int) -> int:
        ans = 0
        count = 0
        while (num > 0) {
            last = (num & 1) #取得num的最后一位
            num >>= 1  #num右移减位
            if (count % 2 == 0)：
                last <<= 1 * (count + 1) #左移count+1 位 
            else：
                last <<= 1 * (count - 1)
            ans |= last
            count++
        }
        return ans

#e.g. num=1001 0101
#last=0000 0001  num=0100 1010 last=0000 0010  ans= 0000 0010
#last=0000 0000  num=0010 0101 last不动  ans=0000 0010
#last=0000 0001  num=0001 0010 last=0000 1000 ans=0000 1010
#last=0000 0000  num=0000 1001 last=0000 0000 ans=0000 1010
#last=0000 0001  num=0000 0100 last=0010 0000 ans=0010 1010
#last=0000 0000  num=0000 0010 last=0000 0000 ans=0010 1010
#last=0000 0000  num=0000 0001 last=0000 0000 ans=0010 1010
#last=0000 0001  num=0000 0000 last=0100 0000 ans=0110 1010
