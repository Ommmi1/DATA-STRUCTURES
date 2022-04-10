import random
class Sorting:
    #initialization
    def __init__(self,data):
        self.data=data
    def GenerateRandom(self,n):
        #this will generate n numbers between range 1 to 20
        self.data=random.sample(range(1,20), n)
        return "Random generated List is :{}".format(self.data)
    #bubble sort
    def BubbleSort(self):
        length_of_the_list=len(self.data)
#         flag=False
        for i in range(length_of_the_list):
            for j in range(length_of_the_list-i-1):
                if self.data[j]>self.data[j+1]:
                    (self.data[j],self.data[j+1])=(self.data[j+1],self.data[j])
        return "Bubble sorted List is    :{}".format(self.data)
    
    #insertion sort from the algorithm
    def InsertionSort(self):
        for i in range(len(self.data)):
            key=self.data[i]
            j=i-1
            while j>=0 and self.data[j]>key:
                self.data[j+1]=self.data[j]
                j=j-1
            self.data[j+1]=key
        return "Insertion sorted List is    :{}".format(self.data)

    
        #selection sort from the algorithm
    def SelectionSort(self):
        n=len(self.data)
        
        list=[]
        list.append(self.data)
        for i in range(n-1):
            #set current element=minimum
            min=i
            #checking element to be minimum
            for j in range(i+1,i):
                if list[j]<list[min]:
                    min=j
                if min!=i:
                    (list[min], list[i])=(list[i],list[min])
            return "Selection sorted List is    :{}".format(list)

    #Searching value at the index
    def Search(self,value):
        syn=0
        for i in range(len(self.data)):
            if(self.data[i]==value):
                self.data[i]=-1
                return "The searching value is :{0} \nThe index is :{1}".format(value,i)
        if(syn==0):
            return "The {0} value is not in list".format(i)
#printing function to print the sorted final list
    def Print(self):
        return "\nThe final sorted is      :{}".format(self.data)
data=[]
obj=Sorting(data)
print(obj.GenerateRandom(10))
print(obj.BubbleSort())
print(obj.InsertionSort())
print(obj.SelectionSort())
print(obj.Search(5))
print(obj.Print())