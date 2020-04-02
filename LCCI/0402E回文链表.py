#编写一个函数，检查输入的链表是否是回文的。

#My:米有思路

#法1：反转链表后与原链表比较
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        r=self.reverse(head).next
        p=head
        while p and r:
            if p.val==r.val:
                p=p.next
                r=r.next
            else:
                return False
        return True
    def reverse(self,head):
        #用头插法
        sub = head
        head2 = ListNode(0)
        # 头插法逆置链表
        while sub:
            q = ListNode(sub.val)
            t = head2.next
            head2.next = q
            head2.next.next = t
            sub = sub.next
        return head2

#法2：遍历读进list后逆置比较 
def isPalindrome2(self, head: ListNode) -> bool:
      l = []
      sub = head
      while sub:
          l.append(sub.val)
          sub = sub.next
      return l == l[::-1]

#法3：改成双向链表 【时间o(n),空间o(1)】
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '回文表示翻转相同, 添加prev属性'
        p1 = None
        p2 = head
        while p2:
            p2.prev = p1
            p1, p2 = p2, p2.next

        p2 = p1
        p1 = head
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.prev
        
        return True

#法4：：快慢指针找中点，反转后半部分或者前半部分【时间o(n),空间o(1)】
##fast指针和slow指针都从head开始，fast每次前进两步，slow每次前进一步
#从slow停止的位置开始，反转链表的后半部分，得到表尾tail
#head和tail分别从链表两端向中间移动，每移动一步比较一次是否相同
#当链表长度为偶数时，前半部分和后半部分等长，因此当tail为空时即表示比较完毕
#当链表长度为奇数时，后半部分比前半部分长一个节点，由于前半部分的最后一个节点仍指向slow停止的位置，
#因此在tail->next为空时，head == tail，因此也可以将tail为空视为终止条件
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        def reverse(head = slow):
            prev, curr = None, head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        tail = reverse()
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True


