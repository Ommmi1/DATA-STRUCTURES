# MUHAMMAD OMER SIDDIQUI 19B-004-se
# DSA LAB 05


#TASK 1
class Stack:
#INITIALIZATION

    def __init__(self,size):
        self.size=size
        self.data=[0 for i in range(size)]
        self.top=0

    def IsEmpty(self):
        if self.top==0:
            return "Is Stack empty ?{}".format(True)
        else:
            return "Is Stack empty ?{}".format(False)

    
    def IsFull(self):
        if self.top==self.size:
            return "Is Stack full ?{}".format(True)
        else:
            return "Is Stack full ?{}".format(False)
            
        
    def Push(self,item):
        if self.IsFull() == True:
            raise "Stack Overflow"
        self.data[self.top]=item
        self.top = self.top+1
        
    def Peek(self):
        return "The peek value is {}".format(self.data[self.top-1])

    def Pop(self):
        if self.IsEmpty() == True:
            raise "Stack Underflow"
        self.top = self.top - 1
        var = self.data[self.top]
        return "Pop value is {}".format(var)

    def count(self):
        return "The size of the Stack is {}".format(self.top)
    
    def Print(self):
        for i in range(self.top):
            print("value: {}".format(self.data[i]))

#DRIVER CODE
# obj=Stack(5)
# obj.Push(6)
# obj.Push(6)
# obj.Push(6)
# obj.Push(6)
# obj.Push(6)
# obj.Print()
# print(obj.Pop())
# print(obj.Peek())
# print(obj.count())
# print(obj.IsFull())
# print(obj.IsEmpty())

#TASK 2       
class Queue:
#INITIALIZATION
    def __init__(self,size):
        self.size=size
        self.data=[0 for i in  range(size)]
        self.top=0
        self.front = 0
        self.rear = 0
        self.count=0

    def IsEmpty(self):
        if self.top==0:
            return "Is Queue empty ?{}".format(True)
        else:
            return "Is Queue empty ?{}".format(False)

    
    def IsFull(self):
        if self.top==self.size:
            return "Is Queue full ?{}".format(True)
        else:
            return "Is Queue full ?{}".format(False)

    def Enqueue(self,value):
        self.data[self.front]=value
        self.front = (self.front+1)%self.size
        return "The Queue is {}".format(self.data)
    
    
    def Dequeue(self):
        self.data[self.rear] = 0
        self.rear = (self.rear+1)%self.size
        var=self.data[self.rear]
        return "The Dequeue is {}".format(var)

    def Count(self):
        return "The size is {}".format(self.count)
    
    def Print(self):
        for i in range(self.count):
            print(self.data[i])

        
#DRIVER CODE
# object=Queue(5)
# object.Enqueue(5)
# object.Enqueue(6)
# object.Enqueue(2)
# object.Enqueue(3)
# print(object.Enqueue(7))
# print(object.Dequeue())
# print(object.Dequeue())
# print(object.Dequeue())
# print(object.Enqueue(10))
# print(object.Print())
# print(object.IsFull())
# print(object.IsEmpty())




#OUTPUT
# value: 6
# value: 6
# value: 6
# value: 6
# value: 6
# Pop value is 6
# The peek value is 6
# The size of the Stack is 4
# Is Stack full ?False
# Is Stack empty ?False
# The Queue is [5, 6, 2, 3, 7]
# The Dequeue is 6
# The Dequeue is 2
# The Dequeue is 3
# The Queue is [10, 0, 0, 3, 7]
# None
# Is Queue full ?False
# Is Queue empty ?True