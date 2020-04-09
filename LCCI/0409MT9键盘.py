#在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。
#每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。
#你会得到一张含有有效单词的列表。映射如下图所示：

#My:简单粗暴遍历
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        num=list(num)
        num=[int(n)-2 for n in num]
        key=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],
        ['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        res=[]
        for word in words:
            flag=True
            for i in range(len(word)):
                if word[i] not in key[num[i]]:
                    flag=False
                    break
            if flag:
                res.append(word)
        return res

#其他
#建字典，将单词转化为数字组合再与num作比较
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        dict={'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
        ans=[]
        for word in words:
            temp=''
            for char in word:
                temp+=dict[char]
            if temp==num:
                ans.append(word)
        return ans

