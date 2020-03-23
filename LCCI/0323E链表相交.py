#链表相交
#给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，
#而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。
#e.g.输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
#输出：Reference of the node with value = 8
#输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
#从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

#法1：双指针法
#通过双指针法找出较长链表与较短链表的长度差，再让较长列表从头前进长度差个节点即可。
#对于任意两个链表l1和l2，假设l1比l2长，那么两个链表同时向前，当l2到达结尾时，l1剩余的长度就是l1比l2长的部分。
#此时再从l1的head开始，把l1比l2长的部分消除掉，然后开始进行比较。
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = headA
        l2 = headB

        while l1 and l2:                  # l1和l2同时前进
            l1 = l1.next
            l2 = l2.next
        
        while l1:                         # 如果l1比l2长
            headA = headA.next            # 从headA中去掉长的部分
            l1 = l1.next
        
        while l2:                         # 如果l长
            headB = headB.next            # 从headB中去掉长的部分
            l2 = l2.next
        
        while headA != headB:             # 进行比较
            headA = headA.next
            headB = headB.next
        
        return headA
        
        
#法2：更简洁 但是链表长了会超时
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p=headA
        q=headB
        while p!=q:
            p=p.next if p else headA
            q=q.next if q else headB
        return p

        
