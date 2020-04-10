#设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。
#不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

#My:不要畏难，太棒了，一次通过
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if self.issubtree(p,q):
            return p
        elif self.issubtree(q,p):
            return q
        else:
            #祖先在更高层的结点
            ans=root
            pre=root
            while self.issubtree(ans,p) and self.issubtree(ans,q):
                if self.issubtree(ans.left,p) and self.issubtree(ans.left,q):
                    pre=ans
                    ans=pre.left
                else:
                    pre=ans
                    ans=pre.right
            return pre

    def issubtree(self,p,q):#判断q是否在以p为根的子树里
        if p is None:
            return False
        if p.left==q or p.right==q:
            return True
        return self.issubtree(p.left,q) or self.issubtree(p.right,q)
       
       
#其他题解：
#递归解法--把我的思路再简化
#假设我们从根结点开始，采用 DFS 向下遍历，
#如果当前结点到达叶子结点下的空结点时，返回空；如果当前结点为 p 或 q 时，返回当前结点；
#这样，当我们令 left = self.lowestCommonAncestor(root.left, p, q) 时，如果在左子树中找到了 p 或 q，
#left 会等于 p 或 q，同理，right 也是一样；
#然后我们进行判断：如果 left 为 right 都不为空，则为情况 图1；
#如果 left 和 right 中只有一个不为空，说明这两个结点在子树中，则根节点到达子树再进行寻找。
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left if left else right


