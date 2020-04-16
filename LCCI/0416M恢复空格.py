#哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
#像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
#在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
#假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

#分词的原理？匹配？
#My:我实现的最小匹配，答案不太对
#为了避免先匹配短字符把长字符的部分匹配走了，对seg按长度排序
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        #从左到右用字典匹配？
        seg=[]
        #最小匹配？最大匹配？
        i=0
        j=0
        while i <len(sentence):
            j=i
            while j <len(sentence):
                if sentence[i:j+1] in dictionary:
                    seg.append(sentence[i:j+1])
                    i=j
                    break
                else:
                    j+=1
            i+=1
        seg.sort(key = lambda i:len(i),reverse=True) 
        print(seg)
        for s in seg:
            sentence=sentence.replace(s,'')
            print(sentence)
        return len(sentence)

#其他：
#1.动态规划，略暴力
#创建一个数组dp[]用来记录结果。句子从前往后看，其中dp[0]=0表示句子是空字符串时没有未识别的字符，dp[i]表示句子前i个字符中最少的未识别字符数。
#然后来找状态转移方程。对于前i个字符，即句子字符串的[0,i)，它可能是由最前面的[0,j)子字符串加上一个字典匹配的单词得到，
#也就是dp[i]=dp[j], j<i；也可能没找到字典中的单词，可以用它前i-1个字符的结果加上一个没有匹配到的第i个字符，即dp[i]=dp[i-1]+1。
#要注意的是，即使前面存在匹配的单词，也不能保证哪一种剩下的字符最少，所以每轮都要比较一次最小值。
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dp=[0]*(len(sentence)+1)
        for i in range(1,len(sentence)+1):
            dp[i] = dp[i-1]+1  #先假设当前字符作为单词不在字典中
            for j in range(i):
                if sentence[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[len(sentence)]
        
#2.优化1
#上述代码套了两层循环，缺点就是对于每一个i，它前面的子字符串都被找了个遍，这其中包括一些根本不可能在字典中出现的单词。需要找一个方法提前结束。
#一种方法是记录字典中每个单词最后一个字符，如果想匹配的字符串的最后一个字母都不在字典里，就没必要再看这个字符串了；
#此外，即使字符串最后一个字母在词典里，也不用挨个去找[j,i)子字符串是否匹配，即不需要让j从0到i遍历一遍，只要看对应长度的子串在不在词典里即可。
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
         #最后一个字符，这样的单词长度有哪些
         map=dict()
         for s in dictionary:
             if s[-1] not in map.keys():
                map[s[-1]]=[len(s)]
             else:
                map[s[-1]].append(len(s))
         n=len(sentence)
         dp=[0]*(n+1)
         for i in range(1,n+1):
            dp[i]=dp[i-1]+1
            c=sentence[i-1]
            if c in map.keys():
                lens=map[c]
                for l in lens:
                    if i>=l and sentence[i-l:i] in dictionary:
                        dp[i] = min(dp[i], dp[i-l])
                
         return dp[n]

#3.优化2 ：Trie字典树
#见图0416M字符匹配 
#该树包含的单词集合为{“at”, “bee”, “ben”, “bt”, “q”}。每一个节点保存一个字符，因为题目说只包含小写字母，所以一个节点最多可以有26个子节点
#每次查找单词都从空白的根节点开始，比如查找单词"cat"，第一个字符'c'就不存在，直接返回false；
#查找单词"bee"，根节点下有b，b的子节点有e，下面还有e所以查到了。但是如果查找单词"be",
#同样的方法'b'和'e'都存在，但是字典里没有"be"这个单词，所以在树里还需要一个boolean变量表示当前节点是不是一个单词的结尾，如图绿色表示。
#如果往字典中插入一个"be"单词，此时b节点下的e节点也应该标绿，此时再查找"be"，在e节点发现它是个单词，所以返回true.
#使用字典树可利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较。
class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.fail = None
        self.tail = 0
        self.children = {}

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.count = 0
        self.words = words
        for word in words:
            self.insert(word)
        self.ac_automation()

    def insert(self, sequence):
        self.count += 1
        cur_node = self.root
        for item in sequence:
            if item not in cur_node.children:
                child = TrieNode(value=item)
                cur_node.children[item] = child
                cur_node = child
            else:
                cur_node = cur_node.children[item]
        cur_node.tail = self.count

    def ac_automation(self):
        queue = collections.deque([self.root])
        while queue:
            temp_node = queue.popleft()
            for value in temp_node.children.values():
                if temp_node == self.root:
                    value.fail = self.root
                else:
                    p = temp_node.fail
                    while p:
                        if value.value in p.children:
                            value.fail = p.children[value.value]
                            break
                        p = p.fail
                    if not p:
                        value.fail = self.root
                queue.append(value)

    def search(self, text):
        p = self.root
        rst = collections.defaultdict(list)
        for i in range(len(text)):
            single_char = text[i]
            while single_char not in p.children and p is not self.root:
                p = p.fail
            if single_char in p.children and p is self.root:
                start_index = i
            if single_char in p.children:
                p = p.children[single_char]
            else:
                start_index = i
                p = self.root
            temp = p
            while temp is not self.root:
                if temp.tail:
                    word = self.words[temp.tail - 1]
                    # rst[word].append((i - len(word) + 1, i + 1))
                    rst[i + 1].append(i - len(word) + 1)
                temp = temp.fail
        return rst

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        model = Trie(dictionary).search(sentence)
        n = len(sentence)
        d = [0] * (n + 1)
        for i in range(n + 1):
            d[i] = d[i - 1] + 1
            for j in model[i]:
                d[i] = min(d[i], d[j])
        return d[-1] - 1


#c
'''class Solution {
    /** 自定义一个TrieNode类型。
    * 这里不用建一个变量来存当前节点表示的字符，
    * 因为只要该节点不为null，就说明存在这个字符
    */
    class TrieNode{
        TrieNode[] childs;
        boolean isWord;
        public TrieNode(){
            childs = new TrieNode[26];
            isWord = false;
        }
    }
    TrieNode root;  //空白的根节点，设为全局变量更醒目
    public int respace(String[] dictionary, String sentence){
        root = new TrieNode();
        makeTrie(dictionary);   //创建字典树
        int n = sentence.length();
        int[] dp = new int[n+1];
        //这里从sentence最后一个字符开始
        for(int i=n-1; i>=0; i--){
            dp[i] = n-i;    //初始默认后面全不匹配
            TrieNode node = root;
            for(int j=i; j<n; j++){
                int c = sentence.charAt(j)-'a';               
                if(node.childs[c] == null){
                    //例如"abcde",i=1,j=2 可找出长度关系
                    dp[i] = Math.min(dp[i], j-i+1+dp[j+1]);
                    break;
                }
                if(node.childs[c].isWord){
                    dp[i] = Math.min(dp[i], dp[j+1]);
                } else{
                    dp[i] = Math.min(dp[i], j-i+1+dp[j+1]);
                }
                node = node.childs[c];
            }
        }
        return dp[0];
    }

    public void makeTrie(String[] dictionary){
        for(String str: dictionary){
            TrieNode node = root;
            for(int k=0; k<str.length(); k++){
                int i = str.charAt(k)-'a';
                if(node.childs[i] == null){
                    node.childs[i] = new TrieNode();
                }
                node = node.childs[i];
            }
            node.isWord = true; //单词的结尾
        }
    }
}'''

