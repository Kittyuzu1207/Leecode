#URL化。编写一种方法，将字符串中的空格全部替换为%20。
#假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。
#（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）

#My:直接用字符串的replace功能
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        S=S[:length]
        S=S.replace(' ','%20')
        return S

#其他方法：
#1.遍历替换
#2.将字符串通过split()方法转换成列表；再通过join()结合起来；
