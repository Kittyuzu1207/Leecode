#给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
#回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
#回文串不一定是字典当中的单词。

#My
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #最多有一个字母出现次数为奇数，其余都为偶数
        dic={}
        for w in list(s):
            if w in dic:
                dic[w]+=1
            else:
                dic[w]=1
        count=0
        for w in set(s):
            if dic[w] % 2==1:
                count+=1
            if count>1:
                return False
        return True
        
#其他
#用collections.Counter统计
