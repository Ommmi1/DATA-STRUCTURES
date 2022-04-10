#19B-004-SE
#1
#=========================

def CoconutSearch(array,loc,e):
    l=0
    r=loc+1
    while l<=r:
        m=(l+r)//2
        if e<array[m]:
            r=m-1
        elif e>array[m]:
            l=m+1
        else:
            return m
    return -1

array = [1,2,3,4,5]
print(CoconutSearch(array,0, 2))
print(CoconutSearch(array,0, 6))


#================================
#2
def leftRotate(arr, d,n): 
    for i in range(d): 
        leftRotatebyOne(arr,n) 
  
def leftRotatebyOne(arr,n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp 
          
def printArray(arr, n): 
    for i in range(n): 
        print ("% d"% arr[i], end =" ")
arr = [1,2,3,4,5]
leftRotate(arr, 2, 5) 
printArray(arr, 5)



#==========================
#3
class DStack:
       # size = number of elements 
    def __init__(self, size):
        self.size = size
        self.s = [0 for i in range(size)]
        self.top = 0


       # s = 1 or 2 

    def IsFull(self):
        if self.top==self.size:
            return "Is Stack full ?{}".format(True)
        else:
            return "Is Stack full ?{}".format(False)

    def IsEmpty(self, s):
        if self.top == -1:
            return True
        else:
            return False

       # s = 1 or 2
    def Push(self, s, value):
        if self.IsFull() == True:
            raise "Stack Overflow"
        self.s[self.top] = value
        self.top = self.top + 1

       # stack = 1 or 2 
    def Pop(self, s):
        if self.IsEmpty(s) == True:
            raise "Stack Underflow"
        self.top = self.top - 1
        x = self.s[self.top]
        return x

       # s = 1 or 2 
    def Peek(self, s):
        return "The peek value is {}".format(self.s[self.top-1])


       # s = 1 or 2       

    def Count(self, s):
        return self.top

ds = DStack(10)
ds.Push(1,10) #push 10 in stack 1
ds.Push(2,20) #push 20 in stack 2
ds.Push(1,30) #push 30 in stack 1
print(ds.Pop(1)) #pop from stack 1
print(ds.Peek(2)) # peek from stack 2


#===================
#4
class Deque:
    def __init__(self,size):
        self.size=size
        self.data=[0 for i in  range(size)]
        self.top=0
        self.front = 0
        self.rear = 0
        self.count=0


    def InsertFront(self,value):
        self.data[self.front]=value
        self.front = (self.front+1)%self.size
        return "The Queue is {}".format(self.data)
    
    
    def DeleteFront(self):
        self.data[self.rear] = 0
        self.rear = (self.rear+1)%self.size
        var=self.data[self.rear]
        return "The Dequeue is {}".format(var)

    def GetFront(self):
        return "The size is {}".format(self.count)
    
    def Print(self):
        for i in range(self.count):
            print(self.data[i])


#============================
#5
class DNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre=None

class DList:
    def __init__(self):
          self.head = None
          self.tail = None

    def Insert(self,item,value):
        new = DNode(value)
        temp = self.head
        
        while(temp):
            if temp.value == item:
                new.next = temp.next
                temp.next = new
                break

    def IsSorted(self):
        sorting = [self.head[index] <= self.head[index+1] for index in range(len(self.head)-1)]
        issorted=all(sorting)
        if issorted==True:
            return True
        else:
            return False
        return issorted

    def DeleteDuplicates(self,value):
        temp=self.head
        a=temp.next
        b=a.next
        while b.next!= None:
            if a.value==value:
                b.pre=a.pre
                temp.next=a.next
                a= None
                break
                
            else:
                temp =temp.next
                a=a.next
                b=b.next

obj=DList()
obj.Insert(1,1)
obj.Insert(1,2)
obj.Insert(1,3)
obj.Insert(1,4)






