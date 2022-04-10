class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.Parent = None
    
    def Insert(self,value):
        self.Parent = self.__Insert(self.Parent,value)
    
    def __Insert(self,parent,value):
        if parent is None:
            parent = Node(value)
        else:
            if value > parent.value:
                parent.right = self.__Insert(parent.right,value)
            else:
                parent.left = self.__Insert(parent.left,value)
                
        return parent
    
    def PreOrder(self):
        return self.__PreOrder(self.Parent)
    
    def __PreOrder(self,parent):
        if parent:
            print(parent.value)
            self.__PreOrder(parent.left)
            
            self.__PreOrder(parent.right)
            
    def InOrder(self):
        return self.__InOrder(self.Parent)
    
    def __InOrder(self,parent):
        if parent:
            self.__InOrder(parent.left)
            print(parent.value)
            self.__InOrder(parent.right)
    
    def PostOrder(self):
        return self.__PostOrder(self.Parent)
    
    def __PostOrder(self,parent):
        if parent:
            print(parent.value)
            self.__PostOrder(parent.right)
            
            self.__PostOrder(parent.left)
            
            
    def Height(self):
        return self.__Height(self.Parent)
     
    
    def __Height(self, parent):
        if parent is None:
            return 0
        return 1+max(self.__Height(parent.left), self.__Height(parent.right))
    
    def Findmin(self):
        x = self.__Findmin(self.Parent)
        return x.value
    
    def __Findmin(self,parent):
        while parent.left is not None:
            if parent.left is None:
                break
            parent = parent.left
        return parent
    
    def Findmax(self):
        x = self.__Findmax(self.Parent)
        return x.value
    
    def __Findmax(self,parent):
        while parent.right is not None:
            if parent.right is None:
                break
            parent = parent.right
        return parent
    
    def Successor(self):
        x = self.__Successor(self.Parent)
        return x.value
    
    def __Successor(self,parent):
        return self.__Findmin(parent.right)
    
    def Predeccessor(self):
        x = self.__Predeccessor(self.Parent)
        return x.value
    
    def __Predeccessor(self,parent):
        return self.__Findmax(parent.left)



ob = BST()
ob.Insert(20)
ob.Insert(10)
ob.Insert(30)
ob.Insert(5)
ob.Insert(15)
ob.Insert(25)
ob.Insert(24)
ob.Insert(40)
ob.Insert(50)
ob.Successor()