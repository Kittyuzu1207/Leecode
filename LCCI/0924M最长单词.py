#给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。
#若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。

#可能不止一个单词来组成。。。
#递归判断一个单词是否为其他单词的组合
class Solution:
    def longestWord(self, words: List[str]) -> str:
        def f(word):
            for i in range(len(word)):
                left = word[:i]
                right = word[i:]
                if left in words:  # 如果单词的左边是组合中的一个单词，则继续看右边
                    if right in words:
                        return True
                    elif f(right):  # 如果单词的右边是其他单词的组合，则返回 ture。否则继续寻找下一种划分。
                        return True
                    else:
                        continue
                else:
                    continue  # 如果单词的左边不是组合中的一个单词，则进行下一种划分。
            return False  # 如果不存在任何正确的划分，返回 false。
        res = ''
        for word in words:
            if f(word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = min(res, word)
        return res
        
