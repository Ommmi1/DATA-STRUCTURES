import random

class Sorting:
    data = []
    def __init__(self):
        pass
    def GenerateRandom(self,n):
       
        x = random.sample(range(0,100),n)
        self.data = x
        
    def BubbleSort(self):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i] < self.data[j]:
                    temp = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = temp
        return self.data
    
    def InsertionSort(self):
        for i in range(1,len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >=0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                j = j - 1
            self.data[j+1] = key
        
        return self.data
    def Print(self):
        print(self.data)
        
obj = Sorting()
obj.GenerateRandom(10)
obj.Print()
obj.InsertionSort()
obj.Print()