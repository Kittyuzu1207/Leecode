#设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
#如果指定节点没有对应的“下一个”节点，则返回null。

#My:简单粗暴，先中序遍历读到一个列表里，再定位
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res=[]
        self.midsearch(root,res)
        idx=res.index(p)
        if idx+1<len(res):
            return res[idx+1]
        else:
            return None

    #中序遍历输入到一个列表中去找？
    def midsearch(self,root,res):
        if root is None:
            return
        self.midsearch(root.left,res)
        res.append(root)
        self.midsearch(root.right,res)
        
#其他：
#利用BST二叉搜索树的性质：当前节点val < 当前节点右孩子子树最左侧叶子val < 所属最直接左子树的根节点val < 该根节点的右子树最左侧叶子val
#idea:
#先找到对应节点，并将路径上的节点入栈
#找右孩子的最左叶子，如果为NULL，进入下一步
#找到所属的最小左子树的根节点
def inorderSuccessor(self, root, p):
        if root is None: return None
        def findRightMin(node):
            current = node.right
            if current is None: return None
            while current.left: current = current.left;
            return current

        path = []
        node = root
        while node is not None and node.val != p.val:
            if p.val < node.val:
                path.append(node)
                node = node.left
            else:
                path.append(node)
                node = node.right

        if node is not None:
            # 要么在右子树的最左侧
            # 要么在上方（作为左子树）
            rightMin = findRightMin(node)            
            leaf = node
            while rightMin is None and len(path) > 0:
                top = path.pop();
                if (leaf != top.right):
                    rightMin = top
                leaf = top       
            return rightMin
        return None

