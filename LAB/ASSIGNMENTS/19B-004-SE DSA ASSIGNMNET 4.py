#MUHAMMAD OMER SIDDIQUI
#19B-004-SE
#A
#DSA ASSIGNMENT 4

class SharedData:  
    #Initialization
    def __init__(self):
        self.Vis=5
        v="Nust Islamabad"
        w="UIT Karachi"
        x="UET Lahore"
        y="BZU Multan"
        z="Faislabad Uni"
        self.Vis_org=[v,w,x,y,z]
        self.graph=None


    def build_graph(self):
        #Assiging names to variale to make the graph understandable
        v="Nust Islamabad"
        w="UIT Karachi"
        x="UET Lahore"
        y="BZU Multan"
        z="Faislabad Uni"
        #creating required grpah with weights 1 and returning it
        self.graph={v:{w:1,y:1}, w:{x:1},x:{w:1,y:1,z:1},y:{z:1,x:1,v:1},z:{y:1,x:1}}


    def calculate_cost(self, root, j): 
        Path_len = 1
        if root[j] == -1 : #Base Case : If j is source 
            print (j) 
            return 0 # when root[-1] then path length = 0     
        l = self.calculate_cost(root , root[j])
        #incerement path length 
        Path_len = l + Path_len
        # print node only if its less than original node length. 
        # i.e do not print any new node that has been added later 
        if self.Vis_org.index(j) < len(self.Vis_org) :  
            print(j)
        return Path_len 


    def minimum_cost_path(self,university, destiny):
            # Mark all the vertices as not visit 
            # Initialize root[] and visit[] 
            v="Nust Islamabad"
            w="UIT Karachi"
            x="UET Lahore"
            y="BZU Multan"
            z="Faislabad Uni"
            visit ={v:False,w:False,x:False,y:False,z:False}
            root ={i:-1 for i in visit}
            # Create a queue for BFS 
            queue=[]
            # Mark the source node as visit and enqueue it 
            queue.append(university)
            visit[university] = True
            while queue :
                # Dequeue a vertex from queue  
                s = queue.pop(0)
                # if s = destiny then print the path and return 
                if s == destiny: 
                    return self.calculate_cost(root, s)
                # Get all adjacent vertices of the dequeued vertex s 
                # If a adjacent has not been visit, then mark it 
                # visit and enqueue it 
                for i in self.graph[s]: 
                    if visit[i] == False: 
                        queue.append(i) 
                        visit[i] = True
                        root[i] = s 

          
# Driver function call to print 
# the shortest path 
object=SharedData()
print("The cost-efficient path b/w UIT Karachi & NUST Islamabad is: ",object.build_graph())
path=object.minimum_cost_path("UIT Karachi","Nust Islamabad" )
print("The cost along this path is:",path)