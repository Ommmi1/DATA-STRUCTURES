print("TASK 1")
#task 1
def EvenList(n):
    evenlist=[]
    for i in range(n):
        y=int(input("Enter Number:"))
        if y % 2 == 0:
            evenlist.append(y)
    return evenlist

n=int(input("enter range "))
x=EvenList(n)
print(x)


print("TASK 2")
#task 2
def Max(list): 

    max = list[0] 


    for x in list: 
        if x > max : 
            max = x 
    
    return max


list = [2,4,6,5] 
print("Largest element is:", Max(list))


print("TASK 3")
#task 3
def Min(list): 

    min = list[0] 


    for x in list: 
        if x < min : 
            min = x 
    
    return min


list = [2,4,6,5] 
print("minimum value is:", Min(list))



print("TASK 4")
#task 4
def Last(data):
    last_element=data[-1]
    print(last_element)
Last([1,3,5,6,44])




print("TASK 5")
#task 5
def KElement(data, k):
    if k>len(data):
        print(None)
    print(data[k-1])
KElement([2,4,6],1)



print("TASK 6")
#task 6
def SecondLast(data):
    if(len(data)>1):
        print(data[-2])
SecondLast([2,6,4,14])


print("TASK 7")
#task 7
def Reverse(data):
    newdata = []
    for x in data:
        newdata.insert(0,x)

    print(newdata)
Reverse([2,4,6])


print("TASK 8")
#task 8
def Unique(data):
    newlist = []
    for x in data:
        if x not in newlist:
            newlist.append(x)

    print(newlist)

Unique([2,4,4,6,6])



print("TASK 9")
#task 9
def UserNumbers(data):

    evenlist=[]
    for i in range(data):
        y=int(input("Enter Number:"))
        if y % 2 == 0:
            evenlist.append(y)
    return evenlist


x=UserNumbers(10)
print(x)
print("TASK 9a")
#9a
Last(x)
#9d
print("TASK 9d")
SecondLast(x)

print("TASK 9b")
#9b
Max(x)

#9c
print("TASK 9c")
Min(x)



print("TASK 10")
#task 10
def ShowExcitement(lst):
    for i in range(5):
        print(lst, end=' ')
    print('\r')
lst = "A quick brown fox jumps over the lazy dog"
ShowExcitement(lst)


print("TASK 11")
#task 11
def Greater(n1, n2, n3):
    if n1>n2 and n1>n3:
        return(n1)
    elif n2>n1 and n2>n3:
        return(n2)
    else:
        return(n3)
Greater(1,2,3)


print("TASK 12")
#task 12
def Divide(dividend, divisor):
    q =dividend//divisor # integer division
    r = dividend% divisor
    
    return(q,r)
Divide(10,3)



print("TASK 13")
#task 13
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age=self.age+1
        
Obj=Person("Omer",20)
print(Obj.name)
print(Obj.age+1)








#HOME TASK
print("HOME TASK")

from cmath import sqrt,phase
def PolarCoordinates(z):
    radius = sqrt(pow(z.real,2)+pow(z.imag,2)).real
    phi = phase(complex(z.real,z.imag))

    return "\nradius = {0:.4}\nPhi(Angle) = {1:.4}".format(radius,phi)

print(PolarCoordinates(1+2j))