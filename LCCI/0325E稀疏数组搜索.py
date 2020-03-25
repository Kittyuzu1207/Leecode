#稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
#我：强行遍历一遍。。。
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i in range(len(words)):
            if words[i]==s:
                return i
        return -1

#其他题解
#用内置函数index
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        return words.index(s) if s in words else -1

#二分查找
#在普通二分查找算法的基础上，增加对空串的特殊处理
#若mid对应的元素为空，则将mid向左或右移动（以向左移动为例）
#若越过边界（mid < left），表明两者中间都是空串，故更新left，进入下个循环
#若未越过边界，则按照通常情况处理
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <=right:
          mid=(left+right)//2
          while not words[mid]:
              mid-=1
          if mid < left: 
              left = (left + right) // 2 + 1
          elif words[mid] < s: 
              left = mid + 1
          elif words[mid] > s: 
              right = mid - 1
          else: 
              return mid
        return -1

