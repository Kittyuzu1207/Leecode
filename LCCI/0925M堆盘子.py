#堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。
#请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。
#此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 
#进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。

#当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1.


#用二维数组解决
class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.array = []

    def push(self, val: int) -> None:
        # 处理边界情况：cap == 0 不让push
        if self.cap == 0:
            return

        if not self.array or len(self.array[-1]) >= self.cap:
            self.array.append([val])
        else:
            self.array[-1].append(val)

    def pop(self) -> int:
        val = -1
        if self.array and self.array[-1]:
            val = self.array[-1].pop()
            if not self.array[-1]: self.array.pop()
        return val

    def popAt(self, index: int) -> int:
        val = -1
        if len(self.array) >= index + 1:
            val = self.array[index].pop()
            if not self.array[index]: self.array.pop(index)
        return val



# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)

