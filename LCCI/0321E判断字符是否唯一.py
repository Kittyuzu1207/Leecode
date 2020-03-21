#实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
#我的解法：直接利用python的set

class Solution:
    def isUnique(self, astr: str) -> bool:
        len1=len(astr)
        len2=len(set(list(astr)))
        if len1==len2:
            return True
        else:
            return False
 
#其他解法：不借助其他数据结构
#遍历字符串s的每个字符，判断其后面是否有相同元素
 # for i in range(length):
 #     for j in range(i+1,length):
 #         if astr[j] == astr[i]:
 #             return False
 # return True        

