# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
#e.g. 输入： 1->2->3->4->5 和 k = 2
#     输出： 4
#给定的 k 保证是有效的。

#我的方法：占用空间小，这个思路best
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        #目标，让p指向倒数第k个节点，q指向最后一个节点，他俩中间差值是不变的，一起移动
        p = head
        q = head
        for i in range(k-1):
            q = q.next
        while q.next is not None:
            p=p.next
            q=q.next
        return p.val
        
#其他题解：
#1.全局变量+递归：遍历到链表尾部，退栈的时候k-1，当k等于0的时候就是要找的节点。
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        self.k = k
        self.res = 0
        
        def kBack(head):
            if not head:
                return
            kBack(head.next)
            self.k -= 1
            if self.k == 0:
                self.res = head.val

         kBack(head)
          
        return self.res
  
