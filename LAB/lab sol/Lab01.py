def EvenList(n):
     lst = []
     for i in range(n):
        y = int(input("Enter the numbers:"))
        if y % 2 == 0:
             lst.append(y)
     return lst
    
n = int(input("Enter the range:"))
x = EvenList(n)
print(x)

def Max(lst):
    
    for i in range(len(lst)):
        y = lst[0]
        if lst[i] > y:
            y = lst[i]
        else:
            pass
    return y

lst = [1,2,3,4,5,6]
x = Max(lst)
print(x)

def Min(lst):
    
    for i in range(len(lst)):
        y = lst[0]
        if lst[i] < y:
            y = lst[i]
        else:
            pass
    return y

lst = [1,2,3,4,5,6]
x = Min(lst)
print(x)

def Last(lst):
    return lst[-1]

lst = [2,4,6]
x = Last(lst)
print(x)

def KElement(lst,k):
    if k > len(lst):
        return None
    return lst[k]

lst = [1,2,3,4,5,6]
k = int(input("Enter the kth index:"))
x = KElement(lst,k)
print(x)

def SecondLast(lst):
    return lst[-2]

lst = [2,4,6]
x = SecondLast(lst)
print(x)

def Reverse(lst):
    return lst[::-1]

lst = [2,4,6]
x = Reverse(lst)
print(x)

def Unique(lst):
    lst2 = []
    
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    
    return lst2

lst = [2,4,4,4,6,7,7,9]
x = Unique(lst)
print(x)

def UserNumbers(lst):
    evenlist=[]
    for i in range(lst):
        y=int(input("Enter Number:"))
        if y % 2 == 0:
            evenlist.append(y)
    return evenlist

def ShowExcitement(lst):
    for i in range(5):
        print(lst, end=' ')
    print('\r')
lst = "A quick brown fox jumps over the lazy dog"
ShowExcitement(lst)


def Greater(n1,n2,n3):
    
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3

n1 = int(input('Enter the first number:'))
n2 = int(input('Enter the second number:'))
n3 = int(input('Enter the third number:'))
x = Greater(n1,n2,n3)
print(x)

def Divide(dividend,divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return(quotient, remainder)
    

dividend = int(input('Enter the dividend:'))
divisor = int(input('Enter the divisor:'))
x = Divide(dividend, divisor)
print(x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Birthday(self):
        self.age = self.age + 1
        return self.age

obj = Person('Asma',28)
y = obj.Birthday()
print(y)


    