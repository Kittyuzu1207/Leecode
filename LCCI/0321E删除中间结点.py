#实现一种算法，删除单向链表中间的某个节点（除了第一个和最后一个节点，不一定是中间节点），假定你只能访问该节点。
#输入：单向链表a->b->c->d->e->f中的节点c
#结果：不返回任何数据，但该链表变为a->b->d->e->f

#我的方法：记得删去最后一个多余的
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #node就是要被删除的,记录当前这个和下一个，把后面的往前挪
        p = node
        q = node.next
        while q is not None:
            p.val=q.val
            if q.next is None:
                p.next=None
                break
            p = p.next
            q = q.next

#其他题解
#没有 prev 指针，如何原地删除，
#因为无法改变 prev 的指针，所以当前节点必须保留。
#其实只要把下一个节点的值 copy 到这个节点上， 然后删除下一个节点即可。不用移动后面的了，更简单

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #node就是要被删除的,记录当前这个和下一个，把后面的往前挪
        node.val=node.next.val
        A=node.next
        node.next=node.next.next
        del A
