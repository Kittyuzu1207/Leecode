#编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
#My: 超出时间限制
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #直接用py的set方法判断是否是变位词，不对，set会把出现多次的字母只算一次
        #先排序再比较
        res=[]
        for s in strs:
            flag=False
            for i in range(len(res)):
                if sorted(res[i][0])==sorted(s):
                    res[i].append(s)
                    flag=True
                    break
            if flag==False:
                res.append([s])
        return res
  
#其他
#俺思路是对的，但别用list存，用dict存，就避免每一次遍历了
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = []
        for word in strs:
            tmp.append(''.join(sorted(word)))
        dic = {}
        ans = []
        for i in range(len(tmp)):
            if tmp[i] not in dic:
                ans.append([strs[i]])
                dic[tmp[i]] = len(ans) - 1
            else:
                ans[dic[tmp[i]]].append(strs[i])
        return ans

