def LinearSearch(data,value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

data = [1,2,3,4,5,6,7,8]
x = LinearSearch(data,3)
print(x)

def BinarySearch(data,n,value):
    l = 0
    r = n-1
    while l <= r:
        m = (l+r)//2
        if data[m] < value:
            l = m+1
        elif data[m] > value:
            r = m-1
        else:
            return m
    return -1

class List:
    data = []
    def __init__(self):
        pass
    def InsertAtFirst(self,value):
        self.data.insert(0,value)
    def InsertAtEnd(self,value):
        self.data.insert(-1,value)
    def DeleteAtFirst(self):
        x = self.data[0]
        self.data = self.data[1:-1]
        return x
    def DeleteAtEnd(self):
        x = self.data[-1]
        self.data = self.data[0:-1]
        return x
    def LinearSearch(self,value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1
    def BinarySearch(self,n,value):
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if self.data[m] < value:
                l = m+1
            elif self.data[m] > value:
                r = m-1
            else:
                return m
        return -1
    def IsSorted(self):
        n = len(self.data)
        for i in range(n-1):
            if self.data[i] > self.data[i+1]:
                return False
            return True
    def Search(self,value):
        if self.IsSorted() == True:
            return self.BinarySearch(len(self.data),value)
        else:
            return self.LinearSearch(value)
    def Print(self):
        print(self.data)
    
        
    
obj = List()
obj.InsertAtFirst(1)
obj.InsertAtFirst(2)
obj.InsertAtFirst(3)
obj.InsertAtEnd(4)
obj.InsertAtEnd(5)
obj.InsertAtEnd(6)
obj.Print()
print(obj.DeleteAtEnd())
obj.Print()


