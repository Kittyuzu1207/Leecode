#请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。
#我：不符合min操作是O(1)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]


    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

#其他解法：双栈法
#使用一个主栈模拟入栈出栈的操作，然而，为了使 getMingetMin 函数实现 O(1)O(1) 的时间复杂度，我们可以使用另一个栈来实现。
#我们可以将这个栈称为最小栈，每当入栈的数小于等于栈顶元素时，随主栈都进行一次 pushpush 操作；
#当出栈的数与最小栈的栈顶元素相等时，最小栈也随主栈进行一次 poppop 操作。
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


