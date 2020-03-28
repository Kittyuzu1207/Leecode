#二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。
#实现一个方法，把二叉搜索树转换为单向链表，要求值的顺序保持不变，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
#返回转换后的单向链表的头节点。

#e.g. 
#输入： [4,2,5,1,3,null,6,0]
#输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]

#My:超出时间限制
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        
        
#题解
#法1：非递归思路：中序遍历，注意使用一个哨兵节点来处理记录最左节点的麻烦
class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        from collections import deque
        if root:
            stack=deque()
            cur=root
            head=TreeNode(-1)  #哨兵结点,记录第一个结点
            prev=head
            while cur or stack:   #把比中间结点小的结点（左子树）用栈处理，再连中间结点，再移到右子树继续处理
                while cur:
                    stack.append(cur) #大的先入栈，小的在栈顶
                    cur=cur.left
                cur=stack.pop()
                cur.left=None
                prev.right=cur
                prev=cur
                cur=cur.right
            return head.right
            
    
       
#法2：返回当前root变成单向链表后的头节点和为节点
#思路：三段处理，然后接起来。将root的左右节点处理完后，root左节点处理后单向链表的尾节点的右节点指向root，root的左节点置空，
#同时把root的右节点指向右节点处理后单向链表的头节点。
class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[0]
    def helper(self,root):  #返回处理后的链表的head和tail
        if not root:
            return None,None
        if not root.left and not root.right:
            return root,root
        lh=rt=root
        if root.left:
            lh,lt=self.helper(root.left)
            lt.right=root
            root.left=None
        if root.right:
            rh,rt=self.helper(root.right)
            root.right=rh
        return lh,rt


