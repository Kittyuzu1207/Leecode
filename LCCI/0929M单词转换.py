#给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
#编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

#e.g. 
'''
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]
'''

#难点：如能想到用word[:i] + '*' + word[i + 1:]为键存储各个形式的单词转换形式，这道题你已经成功了一半。---->通配符 这样就能把只差一位的词并在一起

#那另一半是哪儿呢？用字典存储每个时刻以某个单词结尾的转换序列


#和机器人找路径的题类似，本质还是找路径->dfs
#法1：DFS
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # DFS
        hashmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hashmap[word[:i] + '*' + word[i + 1:]].append(word)
        stack = [beginWord]
        w_dict = {beginWord: [beginWord]}
        while stack:
            word = stack.pop()
            if word == endWord:
                return w_dict[word]
            for i in range(len(word)):
                if word[:i] + '*' + word[i + 1:] in hashmap:
                    for tmp in hashmap[word[:i] + '*' + word[i + 1:]]:
                        if tmp not in w_dict:
                            w_dict[tmp] = w_dict[word] + [tmp]
                            stack.append(tmp)
        return []


#法2：BFS
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # BFS
        hashmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hashmap[word[:i] + '*' + word[i + 1:]].append(word)
        queue = collections.deque([beginWord])
        w_dict = {beginWord: [beginWord]}
        while queue:
            word = queue.popleft()
            if word == endWord:
                return w_dict[word]
            for i in range(len(word)):
                if word[:i] + '*' + word[i + 1:] in hashmap:
                    for tmp in hashmap[word[:i] + '*' + word[i + 1:]]:
                        if tmp not in w_dict:
                            w_dict[tmp] = w_dict[word] + [tmp]
                            queue.append(tmp)
        return []



