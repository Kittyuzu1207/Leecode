#字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

#My:遍历找转换点判断
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1)==0 and len(s2)==0:
            return True
        for i in range(len(s1)):
            if s1[i:]+s1[:i]==s2:
                return True
            
        return False
        
#其他题解
#直接把两个s1拼起来判断，s2是否在里面
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1)==len(s2) and s2 in s1+s1
