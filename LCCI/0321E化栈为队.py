#实现一个MyQueue类，该类用两个栈来实现一个队列。
#e.g.
#MyQueue queue = new MyQueue();
#queue.push(1);
#queue.push(2);
#queue.peek();  // 返回 1
#queue.pop();   // 返回 1
#queue.empty(); // 返回 false

#用list当栈，list.append相当于push，list.pop相当于pop
#一个输入栈，一个工具栈拿来倒腾
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=list() #输入栈
        self.s2=list() #工具栈

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.s1):
            self.s2.append(self.s1.pop())
        e=self.s2.pop()
        while len(self.s2):
            self.s1.append(self.s2.pop())
        return e

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.s1):
            self.s2.append(self.s1.pop())
        e=self.s2.pop()
        self.s1.append(e)
        while len(self.s2):
            self.s1.append(self.s2.pop())
        return e

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
