class Shareddata:  
    def __init__(self):
        self.V=5
        a="Nust Islamabad"
        b="UIT Karachi"
        c="UET Lahore"
        d="BZU Multan"
        e="Faislabad Uni"
        self.V_org=[a,b,c,d,e]
        self.graph=None

    def build_graph(self):
        #Assiging names to variale to make the graph understandable
        a="Nust Islamabad"
        b="UIT Karachi"
        c="UET Lahore"
        d="BZU Multan"
        e="Faislabad Uni"
        #creating required grpah with weights 1 and returning it
        self.graph={a:{b:1,d:1}, b:{c:1},c:{b:1,d:1,e:1},d:{e:1,c:1,a:1},e:{d:1,c:1}} 
        
    def printPath(self, parent, j): 
        Path_len = 1
        if parent[j] == -1 : #Base Case : If j is source 
            print (j) 
            return 0 # when parent[-1] then path length = 0     
        l = self.printPath(parent , parent[j]) 
  
        #incerement path length 
        Path_len = l + Path_len 
  
        # print node only if its less than original node length. 
        # i.e do not print any new node that has been added later 
        if self.V_org.index(j) < len(self.V_org) :  
            print(j)
  
        return Path_len 

    def find_shortest_path(self,source_university, destination_university): 

            # Mark all the vertices as not visited 
            # Initialize parent[] and visited[] 
            a="Nust Islamabad"
            b="UIT Karachi"
            c="UET Lahore"
            d="BZU Multan"
            e="Faislabad Uni"
            visited ={a:False,b:False,c:False,d:False,e:False}
            parent ={i:-1 for i in visited}

            # Create a queue for BFS 
            queue=[] 

            # Mark the source node as visited and enqueue it 
            queue.append(source_university) 
#             print(queue,self.graph)
            visited[source_university] = True

            while queue : 

                # Dequeue a vertex from queue  
                s = queue.pop(0) 

                # if s = destination_university then print the path and return 
                if s == destination_university: 
                    return self.printPath(parent, s) 


                # Get all adjacent vertices of the dequeued vertex s 
                # If a adjacent has not been visited, then mark it 
                # visited and enqueue it 
                for i in self.graph[s]: 
                    if visited[i] == False: 
                        queue.append(i) 
                        visited[i] = True
                        parent[i] = s 
          
# Driver function call to print 
# the shortest path 
g=Shareddata()
g.build_graph()
path=g.find_shortest_path("UIT Karachi","Nust Islamabad" )
print("The cost is ",path)