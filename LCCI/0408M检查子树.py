#检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。
#如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

#My:
#思路：先用树的遍历找到值相等的根结点，再转换为判断两棵树是否相等
#写出来不太对，思路和下面这个是一样的

#其他：
#两重DFS搜索
#第一重：在 t1 中找到 t2 的起点。先判断 t1 当前节点，如果不对就判断 t1 左子树和 t1 右子树。【也就是遍历的思路】
#第二重：从找到的起点开始判断剩下的点，t1 和 t2 同步左右子树搜索。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool: #t1是否包含t2
        if t1==None:
            return False
        if t2==None:
            return True
        return self.dfs(t1, t2) or self.checkSubTree(t1.left , t2) or self.checkSubTree(t1.right, t2)


    #中序遍历:比较两棵树是否相等，root1是否和root2相同
    def dfs(self,root1,root2):
        if root2 is None:
            return True
        elif root1 is None and root2 is not None:
            return False
        elif root1.val!=root2.val:
            return False
        else:
            return self.dfs(root1.left,root2.left) and self.dfs(root1.right,root2.right)

#法二：层次遍历 + DFS
#先是边界输入判断，然后使用层序遍历所有节点，并将每个节点传入辅助函数 check()，以 DFS 的方式递归判断结果。
#只是把外层寻找根节点的步骤换成了层次遍历
class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        
        def check(root, sub) -> bool:
            if not root:
                return False if sub else True
            if (root and not sub) or (root.val != sub.val):
                return False
            return check(root.left, sub.left) and check(root.right, sub.right)

        if not t1: return False
        if not t2: return True

        queue = [t1]
        while queue:
            next_queue = []
            while queue:
                node = queue.pop()
                if check(node, t2): 
                    return True
                if node.left: next_queue += [node.left]
                if node.right: next_queue += [node.right]
            queue = next_queue
        
        return False

