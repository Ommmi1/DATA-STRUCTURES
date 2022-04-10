#MUHAMMAD OMER SIDDIQUI
#19B-004-SE
#DSA LAB 07
#1
def Write(n):
    if n ==1:
        print(n)
    else:
        print(n)
        Write(n-1)

#2
def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial(n-1)

#3
def GCD(a,b):

    if b==0:
        return a
    else:
        return GCD(b,a%b)

#4
def BinarySearch(Lst,low_val,high_val,value):
    if low_val<high_val:
        mid=(high_val+low_val)//2

    if value==Lst[mid]:
        return mid
    elif value<Lst[mid]:
        return BinarySearch(Lst,low_val,mid-1,value)
    else:
        return BinarySearch(Lst,mid+1,high_val,value)



#5
def partitionfunc(lst,left, right):
    pivot=lst[left]
    leftPointer = left
    rightPointer = right-1
    while True:
        while lst[leftPointer] < pivot:
            leftPointer=leftPointer+1
        while rightPointer > 0 and lst[rightPointer] > pivot:
            rightPointer=rightPointer-1
        if leftPointer >= rightPointer:
            break
        else: 
            lst[leftPointer], lst[rightPointer] = lst[rightPointer], lst[leftPointer]
        lst[left], lst[rightPointer] = lst[rightPointer], lst[left]
        return leftPointer
    
def QuickSort(lst,left,right):
    if right-left<=0:
        return
    else:
        pivot = lst[right]
        partition = partitionfunc(left, right, pivot)
        QuickSort(lst,left,partition - 1)
        QuickSort(lst,partition + 1, right)




#DRIVER CODE
# print(Factorial(5))
# print(GCD(8,12))
# List=[1,2,3,4,5]
# BinarySearch(List,0,4,4)
# print(Write(5))
data = [1,2,3,4,5,6,7,8,9,10]
data = [int(x) for x in data]
QuickSort(data, 0, len(data)-1)
print('Ascending Order', data,"\n")
data.reverse()
print('Descending Order', data)



