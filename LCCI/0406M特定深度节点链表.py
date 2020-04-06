#给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表
#（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

#My:又想递归了，但调不出来【因为没有存成listnode】
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        return [[tree]]+self.step([tree])


        
    def step(self,nodelist): #返回当前层下面的所有层
        if len(nodelist)==0:
            return 
        else:
            tmp=[]
            for node in nodelist:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if self.step(tmp):
                res=[tmp]+self.step(tmp)
            else:
                res=[tmp]
            return res

#其他：
#二叉树层次遍历,需要借助队列
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        queue=[tree]
        res=[]
        tmp=[]
        while len(queue)>0:
            head=ListNode(-1)  #每一层重新记一个开头结点
            x=head
            l=len(queue)
            for i in range(l):
                t=queue[0]
                queue=queue[1:]
                y=ListNode(t.val)
                x.next=y
                x=x.next
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)
            res.append(head.next)
        return res


#二叉树深度优先遍历DFS
#用深度优先right优先,每次进入深一层的情况,将最右边的node作为
#链表的node加入结果列表中(ans)

#然后由于dfs回溯得到上面的层时,将该节点作为链表的头一个节点也是
#链表的节点,且该节点指向之前的节点head.next = ans[level]
#更新在ans中的链表节点
#主要要right先,反之就是就反了

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = [] #全局变量
        def dfs(node,level):
            if node is None:
                return
            else:
                if len(ans)==level: #证明是这一层第一个加入的结点（最右）
                    ans.append(ListNode(node.val))
                else:
                    head=ListNode(node.val)
                    head.next=ans[level]
                    ans[level]=head
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        dfs(tree,0)
        return ans
