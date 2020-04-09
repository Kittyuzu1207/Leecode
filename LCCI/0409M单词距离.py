#有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。
#如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

#My:建立单词与位置的字典
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        #遍历一次这个文件，建立单词和位置的字典
        loc={}
        for i in range(len(words)):
            if words[i] not in loc:
                loc[words[i]]=[i]
            else:
                loc[words[i]].append(i)
        #求两个列表中值的最小值
        min_=len(words)
        for a in loc[word1]:
            for b in loc[word2]:
                if abs(b-a)<min_:
                    min_=abs(b-a)
        return min_
 
 
#其他：
#无需存储到字典里，一遍遍历即可
#因为最短的距离只会出现在直接相邻的两个单词之间，所以只需要记录最新出现的单词位置并进行计算
#每一次检测到目标单词就更新一次距离，比较直观
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        w1_idx = -1
        w2_idx = -1
        dis = 200000
        for i in range(len(words)):
            if words[i] == word1:
                w1_idx = i
            if words[i] == word2:
                w2_idx = i
            if w1_idx>=0 and w2_idx>=0:
                tmp_dis = abs(w1_idx - w2_idx)
                if tmp_dis<dis:
                    dis = tmp_dis
        return dis

