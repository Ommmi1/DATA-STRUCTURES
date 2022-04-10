class ArrayDeque:
    def __init__(self,size):
        self.items = []
        self.size=size
        self.data=[0 for i in  range(self.size)]
        self.top=0
        self.front = 0
        self.rear = 0
        self.count=0


    def InsertFront(self, value):
        self.data[self.front]=value
        self.front = (self.front+1)%self.size
        return "The Queue is {}".format(self.data)

    def InsertRear(self,value):
        self.items.append(value)

    def GetFront(self):
        return "The peek value is {}".format(self.data[self.top-1])

    def GetRear(self):
        return self.items[0]

obj=ArrayDeque(4)
print(obj.InsertFront(4))
print(obj.InsertFront(3))
print(obj.InsertFront(2))
print(obj.InsertRear(4))
print(obj.GetFront())
print(obj.GetRear())

