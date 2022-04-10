class Matrix:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.data = [0 for i in range(row*col)]
        
    def Location(self,i,j):
        l = i * self.col + j
        return l
    
    def setvalue(self,i,j,v):
        l = self.Location(i,j)
        self.data[l] = v
    
    def GetValue(self,i,j):
        l = self.Location(i,j)
        return self.data[l]

    def print(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.GetValue(i,j), end = " ")
            print('\n')
    
    def searchdiagonalvalue(self, value):
        list = []
        for i in range(0,len(self.data),4):
            x = self.data[i]
            list.append(x)
        
        if value in list:
            return True
        else:
            return False
    def minimum(self):
        min = sorted(self.data)[0]
        return min

object=Matrix(3,3)
object.setvalue(2,0,6)
object.setvalue(2,1,5)
object.setvalue(2,2,4)
object.setvalue(1,1,1)
object.setvalue(1,2,3)
object.setvalue(1,0,1)
object.setvalue(0,0,3)
object.setvalue(0,2,1)
object.setvalue(0,1,2)

object.print()
object.searchdiagonalvalue(6)
object.minimum()