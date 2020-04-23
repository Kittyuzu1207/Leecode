#给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。
#输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。

#My:使用index函数，调整起始位置
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        res=[]
        for s in smalls:
            if s in big and s!="":
                start=0
                tmp=[]
                while start<=len(big):
                    try:
                        idx=big.index(s,start)
                        tmp.append(idx)
                        start=idx+1
                    except:
                        break
                res.append(tmp)
            else:
                res.append([])
        return res

#其他：Trie 树搜索
class Solution:
    def multiSearch(self, big, smalls):
        # build trie tree
        trie_tree = {}
        for i, word in enumerate(smalls):
            tree = trie_tree
            for c in word:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]
            tree[-1] = i  # 单词结束标志，同时记录 small 单词索引
        # search
        res = [[] for _ in range(len(smalls))]
        for i in range(len(big)):
            tree = trie_tree
            for j in range(i, len(big)):
                if big[j] not in tree:
                    break
                tree = tree[big[j]]
                if -1 in tree:
                    res[tree[-1]].append(i)
        return res

