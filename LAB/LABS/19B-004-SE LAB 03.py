#MUHAMMAD OMER SIDDIQUI
#19B-004-SE
#DSA LAB 03
#C

class List:
    final_list=[]
    def __init__(self):
        pass
    def InsertAtFirst(self,value):
        self.final_list.insert(0,value)

    def InsertAtEnd(self,value):  
        self.final_list.append(value)


    def BinarySearch(self,value):
        l=0
        r=len(self.final_list)-1
        while l<=r:
            m=(l+r)//2
            if self.final_list[m]<value:
                l=m+1
            elif self.final_list[m]>value:
                r=m-1
            else:
                return m
        return -1
    def LinearSearch(self,value):
        for i in range(len(self.final_list)):
            if self.final_list[i]==value :
                return i
        return -1

    def DeleteFromFirst(self):
        self.final_list=self.final_list[1:]
    def DeleteFromEnd(self):
        self.final_list=self.final_list[:-1]
    def IsSorted(self):
        sorting = [self.final_list[index] <= self.final_list[index+1] for index in range(len(self.final_list)-1)]
        issorted=all(sorting)
        if issorted==True:
            return True
        else:
            return False
        return issorted
    def Search(self,value):
        if self.IsSorted==True:
            return self.BinarySearch(value)

        else :
            return self.LinearSearch(value)
        
    def Print(self):
        print(self.final_list)

obj=List()
obj.InsertAtFirst(5)
obj.InsertAtFirst(4)
obj.InsertAtFirst(3)
obj.InsertAtFirst(2)
obj.InsertAtFirst(16)
obj.InsertAtEnd(9)
obj.InsertAtEnd(10)
obj.InsertAtEnd(11)
obj.Print()
# obj.DeleteFromFirst()
# obj.DeleteFromEnd

print(obj.IsSorted())
print(obj.Search(11))


#A
def LinearSearch(data,value):
    result=0
    for i in data:
        if i==value :
            return result
        result+=1
        if result== len(data):
            return -1
        return data[-1]
print(LinearSearch([1,6,3,4,5,6],5))


#B
def BinarySearch(List,n,Value):
    l=0
    r=n-1
    while l<=r:
        m=(l+r)//2
        if Value<List[m]:
            r=m-1
        elif Value>List[m]:
            l=m+1
        else:
            return m
    return -1
List=[1,2,3,4,5,6,7,8,9]
x=len(List)
print("The length of the list is: ",x)
print(BinarySearch(List,x,6))

