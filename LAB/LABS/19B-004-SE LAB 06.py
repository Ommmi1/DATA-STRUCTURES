# MUHAMMAD OMER SIDDIQUI
# 19B-004-SE DSA LAB 06
# =============================================================================
# PART A
class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

# =============================================================================
#PART B
class linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def InsertatFirst(self,value):
        self.value=value
        new_node=Node(self.value)
        x=self.head
        
        #check if list is empty
        
        if x is None:
            self.head=new_node
            self.tail=new_node
        
        else:
            new_node.next=self.head
            self.head=new_node
    
    
    def Head(self):
        return self.head.value
    
    
    def Tail(self):
        return self.tail.value
    
    
    def InsertatEnd(self, value):
        self.value=value
        new_node=Node(self.value)
        x=self.tail
        
        #check if list is empty
        
        if x == None:
            self.head=new_node
            self.tail=new_node
        
        else:
            x.next=new_node
            self.tail=new_node
            new_node.next=None
    
    
    
    def Insertafter(self,item,value):
        new = Node(value)
        temp = self.head
        
        while(temp):
            if temp.value == item:
                new.next = temp.next
                temp.next = new
                break

    def DeleteatFirst(self):
        x=self.head
        
        if x is None:
            raise "List is Empty"
        
        self.head=x.next
    
    
    def DeleteatEnd(self):
        x=self.head
        
        if x is None:
            raise "List is Empty"
        
        while (x.next!=self.tail):
            x=x.next
        self.tail=x
        self.tail.next=None

    
    
    def Deletebyvalue(self,value):
        if self.head is None:
            return "Empty {}".format(None)
        
        else:
            cur  = self.head
            prev = None
            
            while cur.value != value and cur.next is not None:
                prev = cur
                cur = cur.next
        
            if cur.value == value:
        
                if cur == self.head:
        
                    if cur.next is None:
                        self.head = None
        
                    else:
                        self.head = cur.next
        
                else:
        
                    if cur.next is None:
                        prev.next = None
        
                    else:
                        prev.next = cur.next
        
            else:
                return "Empty {}".format(None)
                

    def Print(self):
        x=self.head
        
        #Traverse in linkedlist
        
        while x:
            print(x.value)
            x=x.next

# =============================================================================
#PART C

class Stack:

#INITIALIZATION

    def __init__(self):
        self.head=None
        self.tail=None


    def Push(self,value):
        self.value=value
        new_node=Node(self.value)
        x=self.head
        
        #check if list is empty
        
        if x is None:
            self.head=new_node
            self.tail=new_node
        
        else:
            new_node.next=self.head
            self.head=new_node

    def Pop(self):
        x=self.head
        
        if x is None:
            raise "List is Empty"
        
        while (x.next!=self.tail):
            x=x.next
        
        self.tail=x
        self.tail.next=None

    def Print(self):
        x=self.head
        
        #Traverse in linkedlist
        
        while x:
            print(x.value)
            x=x.next

# =============================================================================
#PART D

class Queue:

#INITIALIZATION
    
    def __init__(self):
        self.head=None
        self.tail=None

    def Enqueue(self,value):
        self.value=value
        new_node=Node(self.value)
        x=self.tail
        
        #check if list is empty
        
        if x == None:
            self.head=new_node
            self.tail=new_node
        
        else:
            x.next=new_node
            self.tail=new_node
            new_node.next=None

   
   
    def Dequeue(self):
        x=self.head
        
        if x is None:
            raise "List is Empty"
        
        self.head=x.next


    def Print(self):
        x=self.head
        
        #Traverse in linkedlist
        
        while x:
            print(x.value)
            x=x.next




# =============================================================================
#DRIVER CODE
#PART B

# L1 = linkedlist()
# L1.InsertatFirst(2)
# L1.InsertatFirst(3)
# L1.InsertatEnd(4)
# L1.Deletebyvalue(3)
# L1.Insertafter(2,5)
# print(L1.Print())
# =============================================================================
#OUTPUT
# 2
# 5
# 4
# None



# =============================================================================
# L1 = linkedlist()
# L1.InsertatFirst(2)
# L1.InsertatFirst(3)
# L1.InsertatFirst(1)
# L1.InsertatEnd(4)
# L1.InsertatEnd(5)
# L1.InsertatEnd(6)
# L1.InsertatEnd(7)
# L1.DeleteatEnd()
# L1.DeleteatEnd()
# L1.DeleteatFirst()
# print(L1.Head())
# L1.Insertafter(2,4)
# L1.Deletebyvalue(5)
# print(L1.Print())
# print(L1.Tail())




# =============================================================================
#OUTPUT
# 2
# 4
# 3
# 4
# None


# =============================================================================
#PART C
# object=Stack()
# object.Push(1)
# object.Push(2)
# object.Push(3)
# object.Push(4)
# object.Pop()
# print(object.Print())




# =============================================================================
#OUTPUT 
# 4
# 3
# 2
# None






# =============================================================================
#PART D
# obj=Queue()
# obj.Enqueue(4)
# obj.Enqueue(3)
# obj.Enqueue(2)
# obj.Enqueue(1)
# obj.Dequeue()
# print(obj.Print())




# =============================================================================
#OUTPUT
# 3
# 2
# 1
# None