#假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。
#返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。

#My:
#好像要用双指针？基本思路对了，可是写不出来orz
#我写的超出时间限制了,主要还是helper函数时间太久，别人是用字典存储的
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        #双指针
        if self.helper(big,small)==False:
            return []
        p,q=0,0
        l,r=0,0
        min_=float("inf")
        while q<=len(big):
            if self.helper(big[p:q],small):
                p+=1
                if q-p+1<min_:
                    min_=q-p+1
                    l=p-1
                    r=q-1
            else:
                q+=1
        return [l,r]
      
    def helper(self,big,small):#看看small是不是在big里
        for s in set(small):
            if s not in set(big):
                return False
        return True


#滑动窗口法，sliding window
#这道题是很典型的滑动窗口法，假设p, q指针维护了一个左闭右开的窗口，那么p, q指针的移动规则为：
#（1）若当前窗口内的目标元素不足，则移动q指针，直到窗口内的元素包括所有的small元素；
#（2）若当前窗口内的目标元素充足，则移动p指针，直到窗口内的元素不包括所有的small元素（也就是少了最左边的一个）。
class Solution(object):
    def shortestSeq(self, big, small):
        """
        :type big: List[int]
        :type small: List[int]
        :rtype: List[int]
        """
        s_dict = {}
        def get_dict(word, w_dict):
            for ch in word:
                w_dict[ch] = w_dict.get(ch, 0) + 1
        get_dict(small, s_dict)
        t_dict = {}
        need = len(small) # 记录窗口内还需要几个字符
        p, q = 0, 0 # p, q维护了一个左闭右开区间
        res = []
        while q < len(big):
            while q < len(big) and need > 0:
                ch = big[q]
                if ch in s_dict:
                    t_dict[ch] = t_dict.get(ch, 0) + 1
                    if t_dict[ch] <= s_dict[ch]:
                        need -= 1
                q += 1
                # print(p, q, need)
            while p <= q and need == 0:
                ch = big[p]
                if ch in s_dict:
                    t_dict[ch] -= 1
                    if t_dict[ch] < s_dict[ch]:
                        break
                p += 1
            if need == 0 and (res == [] or q - p < res[1] - res[0] + 1):
                res = [p, q - 1]
            p += 1
            need += 1
        return res

