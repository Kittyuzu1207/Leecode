#给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        #本质就是判断组成两个字符串的字母是不是一样的
        return sorted(list(s1))==sorted(list(s2))
