#栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。
#最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。
#该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

#My:简单粗暴法，每次push保证栈有序
#设置辅助栈，若数据栈栈顶元素小于当前push元素，则把数据栈栈顶元素弹出到辅助栈，
#若数据栈栈顶元素大于当前push元素，则把push元素 压入辅助栈，之后把数据栈剩下元素全部压入辅助站。最后，把辅助栈元素全部压回数据栈即可。

class SortedStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
        else:
            h = []
            while self.stack and val>self.stack[-1]:
                h.append(self.stack.pop())
            h.append(val)
            while self.stack:
                h.append(self.stack.pop())
            while h:
                self.stack.append(h.pop())
    def pop(self) -> None:
        if not self.stack:
            return -1
        return self.stack.pop()

    def peek(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack)==0

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()

#法2：堆排实现小顶堆
#题意需要让最小元素位于栈顶，实现小顶堆即可满足
#堆排的精髓在于两个方法：
#swim() 元素上浮
#在有新元素入栈时，通过将该元素与其父元素比较，将该元素上浮至堆合适位置。
#需要上浮节点的索引为 index 时，父节点索引为 (index-1)//2
def swim(self, index):
        while index > 0 and self.stack[index] < self.stack[(index-1)//2]:
            self.stack[index], self.stack[(index-1)//2] = self.stack[(index-1)//2], self.stack[index]
            index = (index-1)//2

#sink() 元素下沉
在将最小元素出栈时，将堆顶元素（索引为 0）与堆尾元素交换，pop出栈。
此时堆顶元素的变动使得整个堆不再符合小顶堆的结果，将该节点与两个子节点比较下沉至堆合适位置。
由于堆的根节点索引从 0 开始，所以左右孩子节点的索引为 2index+1 和 2index+2。
def sink(self, index):
        n = len(self.stack)
        while 2*index+1 < n:
            j = 2*index+1
            if j < n-1 and self.stack[j] > self.stack[j+1]:
                j += 1
            if self.stack[index] <= self.stack[j]:
                break
            self.stack[index], self.stack[j] = self.stack[j], self.stack[index]
            index = j

class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.swim(len(self.stack)-1)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack[0], self.stack[-1] = self.stack[-1], self.stack[0]
        self.stack.pop()
        self.sink(0)

    def peek(self) -> int:
        return self.stack and self.stack[0] or -1

    def isEmpty(self) -> bool:
        return not self.stack

    def sink(self, index):
        n = len(self.stack)
        while 2*index+1 < n:
            j = 2*index+1
            if j < n-1 and self.stack[j] > self.stack[j+1]:
                j += 1
            if self.stack[index] <= self.stack[j]:
                break
            self.stack[index], self.stack[j] = self.stack[j], self.stack[index]
            index = j
    
    def swim(self, index):
        while index > 0 and self.stack[index] < self.stack[(index-1)//2]:
            self.stack[index], self.stack[(index-1)//2] = self.stack[(index-1)//2], self.stack[index]
            index = (index-1)//2


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
