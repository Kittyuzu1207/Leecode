#给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

#返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。
#若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。


#审题：再强调一下题目要求的是边都为0的正方形，一开始没仔细看题就做错了，所以我们并不关心内部的元素是0还是1
#法1：1）开辟两个数组，分别记录当前位置向左有多少个连续的0以及当前位置向上有多少个连续的0
#（2）从遍历每个位置(i, j)，那么两个数组记录的数字就是当前点作为正方形右下角节点所能提供的右边的边和下边的边的长度，显然要取两个值的最小值作为可能的正方形的最大值，然后再求得剩下两条边是否符合条件。
#剪枝：如果当前验证的边的长度已经小于当前记录的最大的正方形的边长，那么剩下的更小的变长的正方形无需验证

class Solution(object):
    def findSquare(self, matrix):
        """ 
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l = len(matrix)
        dp_row = [[0] * l for _ in range(l)] # 记录从当前位置向左有几个连续的0 
        dp_col = [[0] * l for _ in range(l)] # 记录从当前位置向上有几个连续的0
        # dp数组初始化
        for i in range(l):
            for j in range(l):
                if matrix[i][j] == 0:
                    dp_row[i][j] = dp_row[i][j - 1] + 1
                    dp_col[i][j] = dp_col[i - 1][j] + 1
        # from pprint import pprint
        # pprint(matrix)
        # pprint(dp_row)
        # pprint(dp_col)
        # 进行筛选
        res = []
        for i in range(l - 1, -1, -1):
            for j in range(l - 1, -1, -1):
                for m in range(min(dp_row[i][j], dp_col[i][j]), 0, -1):
                    if res != [] and m < res[2]:
                        break
                    x = i - m + 1
                    y = j - m + 1
                    if dp_col[i][y] >= m and dp_row[x][j] >= m:
                        if res == [] or x < res[0] or y < res[1]:
                            res = [x, y, m]
        return res


#法2：类似于CNN卷积
    def findSquare_2(self, matrix):
        """ 实现找到最大的边为全0的方阵，看做卷积运算，但是会超时
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        import numpy as np
        l = len(matrix)
        matrix = np.array(matrix)
        # 将0/1反转
        matrix = (~(matrix.astype(np.bool))).astype(np.int)
        for ks in range(l, 0, -1):
            # 构造卷积核
            kernel = np.array([[0] * ks for _ in range(ks)])
            kernel[0, :] = 1
            kernel[-1, :] = 1
            kernel[:, 0] = 1
            kernel[:, -1] = 1
            # 进行卷积
            for i in range(l - ks + 1):
                for j in range(l - ks + 1):
                    res = np.sum(matrix[i:i + ks, j:j + ks] * kernel)
                    if ks == 1 and res == 1 or ks != 1 and res == 4 * ks - 4:
                            return [i, j, ks]
        return []

    def findSquare_3(self, matrix):
        """ 看错题目，这个是实现找到最大的全0方阵
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [[]]:
            return []
        l = len(matrix)
        dp = [[0] * l for _ in range(l)]
        res = []
        for i in range(l):
            for j in range(l):
                if matrix[i][j] == 0:
                    tmp = dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    if res == [] or tmp > res[2]:
                        res = [i - tmp + 1, j - tmp + 1, tmp]
        return res

