#QUESTION #1
#LAB 02
class Array:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [0 for i in range(rows*cols)]

    def Location(self,i, j):
        l = i * self.rows + j
        return l

    def SetValue(self, i, j, v):
        l=self.Location(i,j)
        self.data[l]=v


    def GetValue(self, i, j):
        l=self.Location(i,j)
        return self.data[l]
    def PrintValues(self):
        for  i in range(self.rows):
            for j in range(self.cols):
                print(self.GetValue(i,j),end=' ')
            print('\n')
    def SubValues(self , array1, array2):
        for i in range(self.rows):
                for j in range(self.cols):
                    value = array1.GetValue(i,j)- array2.GetValue(i,j)
                    self.SetValue(i,j,value)            


    def MultValues(self,array1, array2):
        for i in range(array1.rows) :
            for j in range(array2.cols):
                for k in range(array2.cols):
                    result = self.GetValue(i,j)
                    result += array1.GetValue(i,k) * array2.GetValue(k,j)
                    self.SetValue(i,j,result)

    def Transpose(self):
        obj = Array(3,3)
        for i in range(self.rows):
            for j in range(self.cols):
                v = self.GetValue(i, j)
                obj.SetValue(j, i, v)
        return obj.PrintValues()
                
rows=3
cols=3
       
arr1=Array(rows,cols)
arr1.SetValue(0,0,1)
arr1.SetValue(0,1,2)
arr1.SetValue(0,2,3)
arr1.SetValue(1,0,4)
arr1.SetValue(1,1,7)
arr1.SetValue(1,2,9)
arr1.SetValue(2,0,8)
arr1.SetValue(2,1,6)
arr1.SetValue(2,2,2)
a1 = Array(2,2)
a2 = Array(2,2)
a5 = a1.Transpose()
arr1.PrintValues()
for i in range(rows):
    for j in range(cols):
        arr1.SetValue(i,j,i+j)

#Question 2

#TASK 1
import numpy as np
array1 = np.array([[1,2,3,4],[5,6,7,8]], dtype=np.int64)
print(array1)

#TASK 2
x = np.ones((3,4),dtype=np.int64)
print(x)
#task 3
y = np.zeros((2,3,4),dtype=np.int16)
print(y)
#TASK 4
array2 = np.random.random((2,2))
print(array2)
#TASK 5
array3 = np.full((3,3),7)
print(array3)

#TASK 6
array4 = np.identity(3,dtype=np.int64)
print(array4)

#TASK 7
add = np.add(x,y)
print(add)

#TASK 8
diff = np.subtract(x,y)
print(diff)

#TASK 9
mult = np.multiply(x,y)
print(mult)

#TASK 10
div = np.divide(y,x)
print(div)

#TASK 11
rem = np.remainder(y,x)
print(rem)

#TASK 12
result = np.array_equal(x,y)
print(result)
