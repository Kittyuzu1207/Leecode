#设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。
#以下是井字游戏的规则：

#玩家轮流将字符放入空位（" "）中。
#第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。
#"X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。
#当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。
#当所有位置非空时，也算为游戏结束。
#如果游戏结束，玩家不允许再放置字符。
#如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；
#如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

#My:暴力遍历检查
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        N=len(board)
        for i in range(N):  #暴力遍历,检查横竖
            if board[i]=='O'*N:
                return 'O'
            if board[i]=='X'*N:
                return 'X'
            if [t[i] for t in board]==['O']*N:
                return 'O'
            if [t[i] for t in board]==['X']*N:
                return 'X'
        t=[board[i][i] for i in range(N)]
        if t==['O']*N:
            return 'O'
        if t==['X']*N:
            return 'X'
        t=[board[i][N-1-i] for i in range(N)]
        if t==['O']*N:
            return 'O'
        if t==['X']*N:
            return 'X'
        for b in board:
            if ' ' in b:
                return 'Pending'
        return 'Draw'
        
        
#其他
#用python的any函数
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        def check(c):
            s = c * n
            return any((
                any(row == s for row in board),
                any(col == s for col in map(''.join, zip(*board))),
                all(board[i][i] == c for i in range(n)),
                all(board[i][n - i - 1] == c for i in range(n))
            ))
        if check('X'):
            return 'X'
        if check('O'):
            return 'O'
        if ' ' in ''.join(board):
            return 'Pending'
        return 'Draw'

