#字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
#比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
#你可以假设字符串中只包含大小写英文字母（a至z）。

#My:判断当前是否和上一次字母相同，最后一组无法判断所以要自己添加占位符

class Solution:
    def compressString(self, S: str) -> str:
        #统计次数不行，因为后面可能重新出现a
        tmp=[]
        count=0
        last_c=' '
        S=S+'*' #占位，方便处理最后一组
        for c in list(S):
            if last_c!=c and count!=0:
                tmp.append(last_c)
                tmp.append(str(count))
                count=1
                last_c=c
            else:
                count+=1
                last_c=c
        tmp=''.join(tmp)
        if len(tmp)<len(S[:-1]):
            return tmp
        else:
            return S[:-1]

#其他：思路都一样
#用python的groupby
class Solution:
    def compressString(self, S: str) -> str:
        return min( S, "".join(k + str(len(list(v))) for k, v in itertools.groupby(S)), key=len)
