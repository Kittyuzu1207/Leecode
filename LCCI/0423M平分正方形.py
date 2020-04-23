#给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。
#每个正方形的数据square包含3个数值，正方形的左下顶点坐标[X,Y] = [square[0],square[1]]，
#以及正方形的边长square[2]。所求直线穿过两个正方形会形成4个交点，
#请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点）。
#2个端点坐标[X1,Y1]和[X2,Y2]的返回格式为{X1,Y1,X2,Y2}，要求若X1 != X2，需保证X1 < X2，否则需保证Y1 <= Y2。

#若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。


#根据斜率判断与上下或是左右边相交
class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        get_x = lambda y: (y - b) / k
        get_y = lambda x: k * x + b
        
        (x1, y1, l1), (x2, y2, l2) = square1, square2
        c1 = (x1 + l1 / 2, y1 + l1 / 2)
        c2 = (x2 + l2 / 2, y2 + l2 / 2)
        dy, dx = c2[1] - c1[1], c2[0] - c1[0]
        points = []
        if dx == 0:
            points = [(c1[0], y1), (c1[0], y1 + l1), (c1[0], y2), (c1[0], y2 + l2)]
        else:
            k = dy / dx
            b = c1[1] - c1[0] * k
            if -1 <= k <= 1:
                points = [(x1, get_y(x1)), (x1 + l1, get_y(x1 + l1)), 
                          (x2, get_y(x2)), (x2 + l2, get_y(x2 + l2))]
            else:
                points = [(get_x(y1), y1), (get_x(y1 + l1), y1 + l1),
                          (get_x(y2), y2), (get_x(y2 + l2), y2 + l2)]
        points = sorted(points)
        return [*points[0], *points[-1]]
            
