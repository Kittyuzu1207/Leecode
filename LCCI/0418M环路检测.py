#给定一个有环链表，实现一个算法返回环路的开头节点。
#有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。

#My:双指针
#判断链表有环：快慢指针相遇
#何时相遇：快指针会离慢指针越来越远；后来，经过环路后，快指针会开始 追赶 慢指针，假设这时两者相距 k步，
#那么每经过一个单位时间，快指针就离慢指针近了一步，因此该时刻起两者经过 k 个单位时间之后相遇
#如何找到环路起点：设相遇点为 nodenode，相遇点与环路起点的距离 k = head与环路起点的距离 k。
#用一个指针指向 head，另一个指针指点 node，以同样的速度移动 k步之后，两者会指向环路起点。
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next: #开始走位
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 相遇
                break
            
        # 若无相会处，则无环路
        if not fast or not fast.next:
            return None
        # 若两者以相同的速度移动，则必然在环路起始处相遇
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

#法2：用hash表存储遍历过的结点
