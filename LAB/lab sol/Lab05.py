class Stack:
    def __init__(self,size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.top = 0
        
    def IsEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def Push(self,item):
        if self.IsFull() == True:
            raise "Stack Overflow"
        self.data[self.top] = item
        self.top = self.top + 1
        
    def Pop(self):
        if self.IsEmpty() == True:
            raise "Stack Underflow"
        self.top = self.top - 1
        x = self.data[self.top]
        return x
    
    def IsFull(self):
        if self.top == self.size:
            return True
        else:
            return False
    
    def Count(self):
        return self.top
    
    def Print(self):
        for i in range(self.top):
            print(self.data[i])
# =============================================================================
# s = Stack(5)
# s.Push(1)
# s.Push(2)
# s.Push(3)
# s.Push(4)
# s.Push(5)
# #s.Print()
# #print(s.Count())
# s.Pop()
# s.Pop()
#s.Print()

# s.Print()
# s.Pop()
# s.Print()
# #print(s.Count())
# 
# =============================================================================
class Queue:
    def __init__(self,size):
        self.data = [0 for i in range(size)]
        self.f = 0 
        self.r = 0
        self.size = size
        self.count = 0
        
    def IsEmpty(self):
        if self.f == self.r:
            return True
        else:
            return False
        
    def Enqueue(self,item):
        if self.IsFull() == True:
            raise "Queue is Full"
        self.data[self.r] = item
        self.r = (self.r + 1) % self.size
        self.count = self.count + 1
    
    def IsFull(self):
        if self.count == self.size:
            return True
        else:
            return False
    
    def Dequeue(self):
        if self.IsEmpty() == True:
            raise "Queue is Empty"
        x = self.data[self.f]
        self.f = (self.f + 1) % self.size
        self.count = self.count - 1
        return x
    
    def Count(self):
        return self.count
    
    def Print(self):
        for i in range(self.count):
            print(self.data[i])

# =============================================================================
# q = Queue(5)
# q.Enqueue(1)
# q.Enqueue(2)
# q.Enqueue(3)
# q.Print()
# q.Dequeue()
# print("--After Dequeue--")
# q.Print()
# =============================================================================
            


