#设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。
#缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。
#它应该支持以下操作： 获取数据 get 和 写入数据 put 。

#获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
#写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
#当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

#My:字典的基本操作
class LRUCache:

    def __init__(self, capacity: int):
        self.data={}
        self.use=[]  #最近使用的记录
        self.max_size=capacity

    def get(self, key: int) -> int:
        if key in self.data.keys():
            self.use.remove(key)
            self.use.append(key)
            return self.data[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.data.keys():
            if len(self.use)+1>self.max_size:
                k=self.use[0]
                del self.data[k]
                self.use.remove(k)
            self.data[key]=value
            self.use.append(key)
        else:
            self.data[key]=value
            self.use.remove(key)
            self.use.append(key)


#其他方法：
#双向链表
class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self._prev = None
        self._next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        # 预设一个头尾节点，后续插入时不要判空的情况
        self.head = Node('h', -1)
        self.tail = Node('t', -1)
        self.head._next = self.tail
        self.tail._prev = self.head
        self.cap = capacity

    def insert_after(self, target, node):
        # 将一个新节点插入到某节点的后面
        node._next = target._next
        node._prev = target

        target._next._prev = node
        target._next = node

    def move_to_head(self, node):
        # 将已存在的节点插入到头结点后面
        node._prev._next = node._next
        node._next._prev = node._prev

        node._next = self.head._next
        node._prev = self.head

        self.head._next = node
        node._next._prev = node
        
    def pop(self):
        # 待删除的节点
        res = self.tail._prev
        res._prev._next = self.tail
        self.tail._prev = res._prev

        res._prev = None
        res._next = None

        return res

    def get(self, key: int) -> int:
        item = self.store.get(key, -1)
        if item != -1:
            self.move_to_head(item)
            return item.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            item = self.store[key]
            item.val = value
            self.move_to_head(item)
            return
        if len(self.store) == self.cap:
            poped = self.pop()
            del self.store[poped.key]
        # 插入新节点
        node = Node(key, value)
        self.insert_after(self.head, node)
        self.store[key] = node

