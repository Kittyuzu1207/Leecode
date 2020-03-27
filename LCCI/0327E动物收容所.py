#动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。
#在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。
#换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。

#my
class AnimalShelf:

    def __init__(self):
        #先进先出：队列
        self.dog=[]
        self.cat=[]
        self.ani=[]

    def enqueue(self, animal: List[int]) -> None:
        if animal[1]==0:
            self.cat.append(animal)
        else:
            self.dog.append(animal)
        self.ani.append(animal)

    def dequeueAny(self) -> List[int]:
        if len(self.ani)==0:
            return [-1,-1]
        out=self.ani[0]
        self.ani=self.ani[1:]
        if out[1]==0:
            self.cat=self.cat[1:]
        else:
            self.dog=self.dog[1:]
        return out

    def dequeueDog(self) -> List[int]:
        if len(self.dog)==0:
            return [-1,-1]
        out=self.dog[0]
        self.ani.remove(out)
        self.dog=self.dog[1:]
        return out

    def dequeueCat(self) -> List[int]:
        if len(self.cat)==0:
            return [-1,-1]
        out=self.cat[0]
        self.ani.remove(out)
        self.cat=self.cat[1:]
        return out

#other 只用一个栈
class AnimalShelf:

    def __init__(self):
        self.elem = []

    def enqueue(self, animal: List[int]) -> None:
        self.elem.insert(0, animal)

    def dequeueAny(self) -> List[int]:
        ret = [-1,-1]
        if self.elem:
            ret = self.elem.pop()
        return ret

    def dequeueDog(self) -> List[int]:
        i = len(self.elem)-1
        ret = [-1,-1]
        while i>=0:
            if self.elem[i][1] == 1:
                ret = self.elem[i]
                del self.elem[i]
                break
            i -= 1    
        return ret

    def dequeueCat(self) -> List[int]:
        i = len(self.elem)-1
        ret = [-1,-1]
        while i>=0:
            if self.elem[i][1] == 0:
                ret =  self.elem[i]
                del self.elem[i]
                break
            i -= 1
        return ret




