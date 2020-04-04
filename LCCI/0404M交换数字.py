#编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

#My:python可以直接reverse偷懒
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        return list(reversed(numbers))
        
        
#其他：
#位运算：用异或来解决，
#任何数 a 和本身异或等于 0，即 a ^ a 等于 0，0 和 任何数 a 异或，等于a，即 a ^ 0 等于 a
#这样numbers[0] ^ numbers[1] ^ numbers[0] 就等于 numbers[1]
#numbers[1] ^ numbers[0] ^ numbers[1]就等于numbers[0]

class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        return [numbers[0] ^ numbers[1] ^ numbers[0], numbers[1] ^ numbers[0] ^ numbers[1]] 

