#编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。
#如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
#分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

#My:不太对
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #遍历链表，比x小的头插，比x大的尾插
        if head is None:
            return head
        pre=ListNode(-1)
        pre.next=head
        p=head.next
        tail=head   #pre->head(tail)
        while p:
            if p.val<x: #头插
                tmp=ListNode(p.val)
                tmp.next=pre.next
                pre.next=tmp
            else:  #尾插
                tmp=ListNode(p.val)
                tail.next=tmp
                tail=tmp
            p=p.next
        return pre.next
        
#其他：
#说明，排了之后的结果不唯一
#法1：双指针
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        i, j = head, head
        while j:
            if j.val < x:   # 如果等于 x 不做处理
                i.val, j.val = j.val, i.val
                i = i.next  #i将定位到大于x的结点，与后面小于x的结点交换
            j = j.next
        return head


#法2：前插法
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 解题思路：小于x的移到最前面, 前插法实现
        # 注意：保持 head 始终是头结点
        if not head:
            return None
        cur = head
        while cur.next:
            if cur.next.val < x:
                temp = cur.next
                cur.next = temp.next
                temp.next = head
                head = temp
            else:
                cur = cur.next
        return head

#法3：双链表
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 双链表实现，小于x的组成一链表，大于x的组成另一链表，然后两链表拼接
        if not head:
            return None
        fnode = ListNode(-1)
        snode = ListNode(-1)
        first = fnode
        second = snode
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
            head = head.next

        first.next = snode.next
        second.next = None

        return fnode.next

