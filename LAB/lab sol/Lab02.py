class Array:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.data = [0 for i in range(self.row * self.col)]
        
    def Location(self,i,j):
        l = i * self.col + j
        return l
    
    def SetValue(self,i,j,v):
        l = self.Location(i,j)
        self.data[l] = v
        
    def GetValue(self,i,j):
        l = self.Location(i,j)
        return self.data[l]
    
    def SubValues(self,arr1,arr2):
        
        result = Array(self.row,self.col)
        for i in range(self.row):
            for j in range(self.col):
                result.SetValue(i,j,arr1.GetValue(i,j)-arr2.GetValue(i,j))
        return result
    
    def Print(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.GetValue(i,j),end = " ")
            print('\n')
    

row = 3
col = 3        
arr1 = Array(row,col)
for i in range(row):
    for j in range(col):
        arr1.SetValue(i,j,i+j)
arr2 = Array(row,col)
for i in range(row):
    for j in range(col):
        arr2.SetValue(i,j,i*j)
print("----- Array 1 ------")
arr1.Print()
print("----- Array 2 ------")
arr2.Print()
res = arr1.SubValues(arr1,arr2)
print("----- Result ------")
res.Print()

