#设计一个方法，找出任意指定单词在一本书中的出现频率。
#你的实现应该支持如下操作：
#WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
#get(word)查询指定单词在数中出现的频率

#My:用python的collections.Counter
class WordsFrequency:

    def __init__(self, book: List[str]):
        from collections import Counter as CR 
        self.cr=CR()
        self.cr.update(book)
        self.cr=dict(self.cr)

    def get(self, word: str) -> int:
        if word not in self.cr:
            return 0
        return self.cr[word]
        
#其他
#建立字典自己数
def __init__(self, book: List[str]):
    word_freq = {}
    for i in book:
        if i in word_freq:
            word_freq[i] += 1
        else:
            word_freq[i] = 1
    self.word_freq = word_freq

def get(self, word: str) -> int:
    if word in self.word_freq:
        return self.word_freq[word]
    else:
        return 0

