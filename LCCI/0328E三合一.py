#三合一。描述如何只用一个数组来实现三个栈。
#你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。
#构造函数会传入一个stackSize参数，代表每个栈的大小。

#My
#划分为三段，用"_" 占位，通过索引完成相关操作，复杂
class TripleInOne:

    def __init__(self, stackSize: int):
        self.stackSize=stackSize
        self.stacks=['_']*3*stackSize

    def push(self, stackNum: int, value: int) -> None:
        #栈满了
        if '_' not in self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize]:
            return
        else:
            index=self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize].index('_')
            self.stacks[stackNum*self.stackSize+index]=value

    def pop(self, stackNum: int) -> int:
        #满栈
        if '_' not in self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize]:
            tmp=self.stacks[(stackNum+1)*self.stackSize-1]
            self.stacks[(stackNum+1)*self.stackSize-1]='_'
            return tmp
        index=self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize].index('_')
        if index==0:
            return -1
        else:
            tmp=self.stacks[stackNum*self.stackSize+index-1]
            self.stacks[stackNum*self.stackSize+index-1]='_'
            return tmp

    def peek(self, stackNum: int) -> int:
        if '_' not in self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize]:
            tmp=self.stacks[(stackNum+1)*self.stackSize-1]
            return tmp
        index=self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize].index('_')
        if index==0:
            return -1
        else:
            return self.stacks[stackNum*self.stackSize+index-1]

    def isEmpty(self, stackNum: int) -> bool:
        if '_' not in self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize]:
            return False
        index=self.stacks[stackNum*self.stackSize:(stackNum+1)*self.stackSize].index('_')
        if index==0:
            return True
        else:
            return False

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)


#其他题解
#用最后4个元素存下容量，以及各个栈的栈顶坐标
#每个栈的元素是隔三个存的
#~按位取反  ~n=-(n+1)

class TripleInOne:

    def __init__(self, stackSize: int):
        self.d = [0] * stackSize * 3 + [stackSize * 3, 2, 1, 0]

    def push(self, stackNum: int, value: int) -> None:
        if self.d[~stackNum] < self.d[~3]:
            self.d[self.d[~stackNum]] = value
            self.d[~stackNum] += 3

    def pop(self, stackNum: int) -> int:
        if self.d[~stackNum] >= 3:
            self.d[~stackNum] -= 3
            return self.d[self.d[~stackNum]]
        return -1

    def peek(self, stackNum: int) -> int:
        return self.d[~stackNum] < 3 and -1 or self.d[self.d[~stackNum] - 3]

    def isEmpty(self, stackNum: int) -> bool:
        return self.d[~stackNum] < 3

