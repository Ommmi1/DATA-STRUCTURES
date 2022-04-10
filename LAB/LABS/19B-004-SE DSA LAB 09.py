#MUHAMMAD OMER SIDDIQUI
#19B-004-SE
#DSA LAB 09
#importing lab 5 and calling stack and queue
# import Lab05
# from Lab05 import Stack
# from Lab05 import Queue
#also added these two classes
# class Stack:
#     def __init__(self,size):
#         self.size = size
#         self.data = [0 for i in range(size)]
#         self.top = 0
        
#     def IsEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False
    
#     def Push(self,item):
#         if self.IsFull() == True:
#             raise "Stack Overflow"
#         self.data[self.top] = item
#         self.top = self.top + 1
        
#     def Pop(self):
#         if self.IsEmpty() == True:
#             raise "Stack Underflow"
#         self.top = self.top - 1
#         x = self.data[self.top]
#         return x
    
#     def IsFull(self):
#         if self.top == self.size:
#             return True
#         else:
#             return False
    
#     def Count(self):
#         return self.top
    
#     def Print(self):
#         for i in range(self.top):
#             print(self.data[i])
# class Queue:
#     def __init__(self,size):
#         self.data = [0 for i in range(size)]
#         self.f = 0 
#         self.r = 0
#         self.size = size
#         self.count = 0
        
#     def IsEmpty(self):
#         if self.f == self.r:
#             return True
#         else:
#             return False
        
#     def Enqueue(self,item):
#         if self.IsFull() == True:
#             raise "Queue is Full"
#         self.data[self.r] = item
#         self.r = (self.r + 1) % self.size
#         self.count = self.count + 1
    
#     def IsFull(self):
#         if self.count == self.size:
#             return True
#         else:
#             return False
    
#     def Dequeue(self):
#         if self.IsEmpty() == True:
#             raise "Queue is Empty"
#         x = self.data[self.f]
#         self.f = (self.f + 1) % self.size
#         self.count = self.count - 1
#         return x
    
#     def Count(self):
#         return self.count
    
#     def Print(self):
#         for i in range(self.count):
#             print(self.data[i])
class Graph:
    #Initialization
    def __init__(self,vertex):
        self.vertex = vertex
        #for 2d array
        self.adj = [[0 for i in range(vertex)] for j in range(self.vertex)]
        self.neighbours = []
        self.visited = []
        
    def AddEdge(self,source,destination):
        self.adj[source][destination] = 1
        self.adj[destination][source] = 1
    
    def GetNeighbours(self,v):
        for i in range(len(self.adj[v])):
            if self.adj[v][i] == 1:
                self.neighbours.append(i)
        return self.neighbours
    
    #Depth First Search
    def DFS(self,source):
        neighbors = []
        #Calling stack class for depth first search
        s = Stack(self.vertex)
        #pushing value in stack
        s.Push(source)
        self.visited.append(source)
        
        while not s.IsEmpty():
            x = s.Pop()
            print("Visited {}".format(x))
            
            neighbors = self.GetNeighbours(x)
            for i in neighbors:
                if i not in self.visited:
                    s.Push(i)
                    self.visited.append(i)
    
    # Breadth first search
    def BFS(self,source):
        neighbors = []
        #Calling qeueue class for breadth first search
        q = Queue(self.vertex)
        #pushing value in queue
        q.Enqueue(source)
        self.visited.append(source)
        
        while not q.IsEmpty():
            x = q.Dequeue()
            print("Visited {}".format(x))
            
            neighbors = self.GetNeighbours(x)
            for i in neighbors:
                if i not in self.visited:
                    q.Enqueue(i)
                    self.visited.append(i)

    def PrintMatrix(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.adj[i][j],end=" ")
            print()


#Driver Code           
object = Graph(5)
object.AddEdge(0,1)
object.AddEdge(0,2)
object.AddEdge(1,2)
object.AddEdge(1,3)
object.AddEdge(2,3)
object.AddEdge(2,4)
object.AddEdge(3,4)

object.PrintMatrix()
print("Depth First Search")
object.DFS(1)
print("Breath First Search")
object.BFS(3)