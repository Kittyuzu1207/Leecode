#实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
#我：计算深度，递归判断
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalan(root)

    def isBalan(self,node): #判断某个结点以下是不是平衡
        if node ==None:
            return True
        if self.depth(node.left)-self.depth(node.right)>1 or self.depth(node.right)-self.depth(node.left)>1:
            return False
        if self.isBalan(node.left) and self.isBalan(node.right):
            return True
        return False

    def depth(self,node): #一个结点的高度
        if node ==None:
            return 0
        else:
            return max(1+self.depth(node.left),1+self.depth(node.right))
 
 #其他题解
 #一样的思路，写得更简洁
 class Solution:
    # 计算以当前节点为根的树深度
    def Depth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.Depth(root.left), self.Depth(root.right))
        return 0


    def isBalanced(self, root: TreeNode) -> bool:
        # 空树是AVL
        if not root:
            return True
        # 若左右子树深度超过1，非AVL
        if abs(self.Depth(root.left) - self.Depth(root.right)) > 1:
            return False
        # 递归执行，当出现不满足AVL性质的子树时，执行短路运算立即返回结果
        return self.isBalanced(root.left) and self.isBalanced(root.right)

