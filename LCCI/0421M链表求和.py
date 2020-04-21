#给定两个用链表表示的整数，每个节点包含一个数位。
#这些数位是反向存放的，也就是个位排在链表首部。
#编写函数对这两个整数求和，并用链表形式返回结果。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#My:
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #倒着放的可以直接遍历，注意进位
        l3=ListNode(-1)
        flag=False  #默认不进位
        p=l1
        q=l2
        k=l3
        while ( p or q ) or flag:
            if p is None and q is None:
                k.next=ListNode(1)
                break
            if p is None: #补齐
                p=ListNode(0)
            if q is None:
                q=ListNode(0)
            k.next=ListNode(-1)
            k=k.next
            t=p.val+q.val
            if flag:
                k.val=(t+1)%10
                if t+1>=10:
                    flag=True
                else:
                    flag=False #下一步不用进位
            else:
                k.val=t%10
                if t>=10:
                    flag=True
                else:
                    flag=False
            p=p.next
            q=q.next
        return l3.next

#其他:
#右对齐补0
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2: return l1 or l2
    stack1, stack2 = [l1], [l2]
    carry, prev = 0, None
    while stack1[-1].next:
        stack1.append(stack1[-1].next)
    while stack2[-1].next:
        stack2.append(stack2[-1].next)
    while stack1 or stack2 or carry:
        carry += (stack1.pop().val if stack1 else 0) + (stack2.pop().val if stack2 else 0)
        head = ListNode(carry % 10)
        carry //= 10
        head.next = prev
        prev = head
    return head

