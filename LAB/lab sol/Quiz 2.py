class Matrix:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.data = [0 for i in range(row*col)]
        
    def Location(self,i,j):
        l = i * self.col + j
        return l
    
    def SetValue(self,i,j,v):
        l = self.Location(i,j)
        self.data[l] = v
    
    def GetValue(self,i,j):
        l = self.Location(i,j)
        return self.data[l]
    
    def GetLeftDiagonal(self):
        y = []
        for i in range(self.row):
            x = self.GetValue(i,i)
            y.append(x)
        return y
    
    def SumLeftDiagonal(self):
        sum = 0
        y = self.GetLeftDiagonal()
        for i in range(len(y)):
            sum+=y[i]
        return sum
    
    def GetRightDiagonal(self):
        y = []
        for i in range(self.row):
            x = self.GetValue(i,self.row-1-i)
            y.append(x)
        return y
    
    def SumRightDiagonal(self):
        sum = 0
        y = self.GetRightDiagonal()
        for i in range(len(y)):
            sum+=y[i]
        return sum
    
    def MaxValue(self,array1):
        x = array1.GetValue(0,0)
        for i in range(array1.row-1):
            for j in range(array1.col-1):
                y = array1.GetValue(i+1,j+1)
                if x < y:
                    x = y
        return x
                
    
    def MinValue(self,array1):
        x = array1.GetValue(0,0)
        for i in range(array1.row-1):
            for j in range(array1.col-1):
                y = array1.GetValue(i+1,j+1)
                if x > y:
                    x = y
        return x
    
    def Replace(self,value):
        y = self.GetLeftDiagonal()
        for i in range(len(y)):
            y[i] = value
    
        return y
    
    def SearchValue(self,value):
        for i in range(self.row):
            for j in range(self.col):
                x = self.GetValue(i,j)
                if x == value:
                    return self.Location(i,j)
        return -1
    
        
    def Print(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.GetValue(i,j), end = " ")
            print('\n')
    
row = 3
col = 3
obj = Matrix(row,col)
for i in range(row):
    for j in range(col):
        obj.SetValue(i,j,i+j)
obj.Print()
#print(obj.GetRightDiagonal())
#print(obj.MaxValue(obj))
#print(obj.MinValue(obj))
#print(obj.Replace(2))
print(obj.SearchValue(5))