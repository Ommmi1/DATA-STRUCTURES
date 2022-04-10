#MUHAMMAD OMER SIDDIQUI
#19B-004-SE
#DSA LAB 10

class Vertex:
    #INITIALIZATION
    def __init__(self,value):
        self.value=value
        self.dist=float("inf")
        self.pi=value 
        self.visited=False

class PriorityQueue:
    def __init__(self):
        self.list=[]
    
    def Is_Empty(self):
        if self.list==[]:
            return True
        return False
   
    def Enqueue(self,v):
        self.list.append(v)

    def DeQueue(self):
        x=self.list[0]
        self.list.remove(0)
        return x
       
    def Extract_min(self):
        minloc=self.__Findmin()
        y=self.list[minloc]
        self.list.pop(minloc)
        return y
    
    def __Findmin(self):
        minloc= self.list[0]
        loc=0
       
        for i in range(len(self.list)):
            if self.list[i].dist<minloc.dist:
                minloc=self.list[i]
                loc=i
        return loc




class DGraph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.matrix=[[0 for i in range(vertex)]for j in range(vertex)]

    def Add_Directed_Edges(self,src,dest,weight):
        self.matrix[src][dest]=weight
       
    def Get_Directed_neighbour(self,source):
        neg=[]
        for i in range(self.vertex):
            if self.matrix[source][i]>0:
                neg.append(i)
        return neg


    def Dijkstra_Shortest_Path(self,source):
        cost=[]
        q=PriorityQueue()
        for i in range(self.vertex):
            cost.append(Vertex(i))
        for i in range(self.vertex):
            cost[i].dist=float("inf")
        cost[source].dist=0
       
        for i in range(self.vertex):
            q.Enqueue(cost[i])
        while not q.Is_Empty():
            z=q.Extract_min()
            self.visited=True
            print("visited {}".format(z.value))
           
            neighbours=self.Get_Directed_neighbour(z.value)
           
            for i in neighbours:
                if cost[i].visited ==False and cost[i].dist>z.dist+self.matrix[z.value][i]:
                    cost[i].dist=z.dist+self.matrix[z.value][i]
                    cost[i].pred=z.value
        for j in cost:
            print(j.value,j.dist,j.pi)



#DRIVER CODE
obj=DGraph(4)
obj.Add_Directed_Edges(0,1,5)
obj.Add_Directed_Edges(0,2,20)
obj.Add_Directed_Edges(0,3,4)
obj.Add_Directed_Edges(1,2,6)
obj.Add_Directed_Edges(1,3,25)
obj.Add_Directed_Edges(2,3,7)
obj.Add_Directed_Edges(3,0,30)
obj.Dijkstra_Shortest_Path(3)