#编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
#我的方法：先把相同值的挪在一起，再按照排序列表的方式删-->超出时间限制:遍历了太多次，链表太长就爆炸
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        #排序列表：如果下一个和当前这个一样，删除下一个，直到最后一个
        if head is None or head.next is None:
            return head
        head=self.sort(head)
        p = head
        q = head.next
        while q is not None:
            if p.val==q.val:
                p.next=q.next
                del q
                q=p.next
            else:
                p=p.next
                q=q.next
        return head
    def sort(self,head):
        #未排序列表：先把相同值的挪在一起？
        if head is None:
            return head
        p=head
        while p.next is not None:
            q=p.next
            if p.val==q.val:
                p=p.next
                q=q.next
            else:
                while q is not None and q.next is not None:
                    k=q
                    q=q.next
                    if p.val==q.val: #插入和删除，而不是交换值，不然会打乱总体顺序
                        tmp=ListNode(q.val)
                        tmp.next=p.next
                        p.next=tmp
                        k.next=q.next
                        del q
                        q=k.next             
                p=p.next
        return head

##题解
#法1：借助了set,不存在则放入，存在则删除
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head == None:
            return
        A = set()
        A.add(head.val)
        prev, p = head, head.next
        while p:
            if p.val in A:
                prev.next = p.next
                del p
                p = prev.next
            else:
                A.add(p.val)
                prev = p
                p = p.next       
        return head
 
 #法2：暴力解法
 #类似于我的那个两层循环
