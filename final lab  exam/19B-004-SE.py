"""TASK 1"""
def WordSpell(file, spell):
    infile=open(file)
    content=infile.readlines()
    #USE LIST TO INSERT THE REQUIRED WORDS
    final_list = []
    #ITERATING OVER WORDS
    for words in content:
        #STORING ALPHABETS FROM WORD AND CONVERTING STRING TO LOWER
        word = ''.join(char for char in words.strip('\n') if char.lower())
        """STARTSWITH IS A BUILTIN FUNCTION AND WE 
        USE THIS TO FIND THE STARTING WORD"""
        if word.startswith(spell):
            #ADD THE ORIGINAL WORD TO THE LIST
            final_list.append(words.strip('\n'))
    #RETURN THE FILTERED WORDS
    return final_list
print(WordSpell('Words.txt', 'pre'))
    

"""TASK 2"""
class JukeNode(object):
    def __init__(self, mysong):
    # you can add further functions / attributes
        ## mysong of the node
        self.mysong = mysong
        ## next pointer
        self.next = None
        ## previous pointer
        self.previous=None


class Mysong(JukeNode):
    # you can add further functions / attributes
    def __init__(self, title, artist):
        mysong = [title, artist]
        self.title = title
        self.artist = artist
        self.times_played = 0
        JukeNode.__init__(self, mysong)



class JukeBox:
    def __init__(self):
        #initializing the head with None
        #initialize lists to store playlist and favorites
        self.playlist_head = None
        self.favt_head = None

    """After calling this
    function this will insert the song"""
    def insert(self, new_node):
        #check whether the head is empty or not
        if self.playlist_head:
            #getting to the last node
            last_node = self.playlist_head
            while last_node.next != None:
                last_node = last_node.next

            #assigning the new node to the next pointer of last node
            last_node.next = new_node

        else:
            #head is empty
            #assigning the node to head
            self.playlist_head = new_node

    def delete(self, title):
        current = self.playlist_head
        previous = None
        found = False
        while current and found is False:
            if current.title == title:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            return False

        if previous is None:
            self.playlist_head = current.next

        else:
            previous.next = current.next
        return True

    def display(self, printingStatus=True):
        #variable for iteration
        temp_node = self.playlist_head
        mysong = []
        #iterating until we reach the end of the linked list
        while temp_node != None:
            ## printing the node mysong
            if printingStatus == True:
                print("Playing song : {}".format(temp_node.title))
            mysong.append([temp_node.title, temp_node.artist])

            #returning to the next node
            temp_node = temp_node.next

        return mysong

    def search(self, title):
        # find song in linked list if it dosen't exit o/p song not found
        cur_node = self.playlist_head
        found = False
        ## iterating until we reach the end of the linked list
        while cur_node != None:
            if cur_node.mysong[0] == title:
                found = True
                break
            ## moving to the next node
            cur_node = cur_node.next

        return found

    def update_times_played(self, title):
        # find song and update how many times it has been played
        cur_node = self.playlist_head
        ## iterating until we reach the end of the linked list
        update_favorites = False

        while cur_node != None:
            if cur_node.mysong[0] == title:
                cur_node.times_played += 1

                if cur_node.times_played == 3:
                    update_favorites = True
                break
            ## moving to the next node
            cur_node = cur_node.next
        return update_favorites

    def getSongDetails(self, title):
        cur_node = self.playlist_head
        ## iterating until we reach the end of the linked list
        mysong = []
        while cur_node != None:
            if cur_node.mysong[0] == title:
                mysong = cur_node.mysong
                break
            ## moving to the next node
            cur_node = cur_node.next

        return mysong



class MyJukeBox:
    #initialization
    def __init__(self):
        self.playlist = JukeBox()
        self.favorites = JukeBox()

    """this will insert the new song with title and artist"""
    def InsertSong(self, title, artist):
        newNode = Mysong(title, artist)
        self.playlist.insert(newNode)

    """this will print playlist"""
    def PlayList(self):
        self.playlist.display()

    """this will play songs that are only in favorites"""
    def PlayFav(self):
        self.favorites.display()

    """this will play songs """
    def PlaySong(self, title):
        does_song_exist = self.playlist.search(title)
        if does_song_exist == True:
            print("Playing song : {}".format(title))
            update_favorites = self.playlist.update_times_played(title)
            if update_favorites == True:
                mysong = self.playlist.getSongDetails(title)
                self.AddToFav(mysong[0], mysong[1])
        else:
            print("Song does not exist!")

    """thsis function will song to favorites"""
    def AddToFav(self, title, artist):
        self.favorites.insert(Mysong(title, artist))
        print( " {} ,has been added to favorites".format(title))


    """this function will delete the song of the
    given title"""
    def DeleteSong(self, title):
        delete_1 = self.playlist.delete(title)
        delete_2 = self.favorites.delete(title)

        if delete_1 == True and delete_2 == True:
            print("{} has been deleted".format(title))

        elif delete_1 == True:
            print("{} has been deleted from the favorites".format(title))

    """this function will give you
    all favorite songs"""
    def GetFav(self):
        Allfav_title_lst = []
        mysong = self.favorites.display(False)
        for song in mysong:
            Allfav_title_lst.append(song[0])

        return "The final favorite list is: {}".format(Allfav_title_lst)




#DRIVER CODE
Obj = MyJukeBox()
Obj.InsertSong("Radioactive", "Imagine Dragons")
Obj.InsertSong("Girls Like you", "Maroon5")
Obj.InsertSong("Demons", "Imagine Dragons")
Obj.PlaySong("Demons")
Obj.PlaySong("Demons")
Obj.PlaySong("Demons")
Obj.PlaySong("Radioactive")
Obj.PlaySong("Girls Like you")
Obj.PlaySong("Girls Like you")
Obj.PlaySong("Girls Like you")
print(Obj.GetFav())
Obj.DeleteSong("Girls Like you")
Obj.PlayFav()




"""TASK 3"""
#IMPORTING QEUEUE
from queue import Queue
class BankQueue(object):
    #THIS IS PARENT CLASS
    #ASSIGN QEUEUE WITH THE SIZE 10
    #initializing 4 queue for different programs
    q1 = Queue(maxsize=10)
    q2 = Queue(maxsize=10)
    q3 = Queue(maxsize=10)
    q4 = Queue(maxsize=10)

    def __init__(self, typeID, size):
        #INITIALIZE WITH TYPE/SIZE
        self.type = typeID
        self.size = size

#THIS WILL INSERT THE CUSTOMER IN THE LINE
    def EnqueueCustomer(self, time):
        #WE USE 4 LINES BECAUSE THERE ARE 4 TYPES OF QUESUEU
        if self.type == '1':
            self.q1.put(time)
        elif self.type == '2':
            self.q2.put(time)
        elif self.type == '3':
            self.q3.put(time)
        else:
            self.q4.put(time)

#THIS FUNCTION WILL REMOVE CUSTOMER FROM THE LOINE
    def DequeueCustomer(self):
        #WE USE 4 LINES BECAUSE THERE ARE 4 TYPES OF QUESUEU

        if self.type == '1':
            return self.q1.get()
        elif self.type == '2':
            return self.q2.get()
        elif self.type == '3':
            return self.q3.get()
        else:
            return self.q4.get()

    def IsFull(self):
        #WE USE 4 LINES BECAUSE THERE ARE 4 TYPES OF QUESUEU
        if self.type == '1':
            return self.q1.full()
        elif self.type == '2':
            return self.q2.full()
        elif self.type == '3':
            return self.q3.full()
        else:
            return self.q4.full()

    def IsEmpty(self):
        #WE USE 4 LINES BECAUSE THERE ARE 4 TYPES OF QUESUEU
        if self.type == '1':
            return self.q1.empty()
        elif self.type == '2':
            return self.q2.empty()
        elif self.type == '3':
            return self.q3.empty()
        else:
            return self.q4.empty()


    def size_of_Queue(self):
        #WE USE 4 LINES BECAUSE THERE ARE 4 TYPES OF QUESUEU
        if self.type == '1':
            return self.q1.qsize()
        elif self.type == '2':
            return self.q2.qsize()
        elif self.type == '3':
            return self.q3.qsize()
        else:
            return self.q4.qsize()

    def Sum_for_Queue(self):
        stR =0
        #WE USE 4 LINES BECAUSE THERE ARE 4 TYPES OF QUESUEU
        for i in range(0,10):
            if self.type == '1':
                stR =stR + self.type.q1[i]
                return stR
            elif self.type == '2':
                stR =stR + self.type.q2[i]
                return stR
            elif self.type == '3':
                stR =stR + self.type.q3[i]
                return stR
            else:
                stR =stR + self.type.q4[i]
                return stR

class BankSimulation(BankQueue):
    Lst = []
    Final = []
    def __init__(self, filename):
        self.filename = filename
        BankQueue.__init__(self,type,size)


    def Process(self):
        infile = open(self.filename, 'r')
        content = infile.read().split()
        for i in range(0, len(content)):
            if i % 2 == 0:
                self.Lst.append(content[i])
            else:
                self.Final.append(content[i])
        for i in range(420):
            if BankQueue.IsFull(self):
                return "Queue is currenty Full"
            else:
                BankQueue.EnqueueCustomer(self,self.Final)

    def CustomersServed(self):
        lst = []
        for i in range(0,4):
            lst.append(BankQueue.size_of_Queue(self))
        return lst

    def AverageTime(self):
        lst= []
        for i in range(0,4):
            lst.append(BankQueue.Sum_for_Queue(self)/BankQueue.size_of_Queue(self))
        return lst
 
    def NotServed(self):
        lst = []
        if BankQueue.IsFull(self):
            lst.append(self.Final)
        return lst


#DRIVER CODE
if __name__=='main':
    Obj = BankSimulation("customers.txt")
    print(Obj.Process())
    print(Obj.CustomersServed())
    print(Obj.AverageTime())
    print(Obj.NotServed())


"""TASK 4"""
from datetime import date
def SortEmpire(file):
    current_date = date.today()
    f = open(file)
    infile=f.readlines()
    # ARRAY TO STORE ALL YEARS UPTIL NOW AND USE COUNTING SORT TO SORT IN O(N)
    items = [] 
    for i in range(current_date.year):
        items.append([])
    for item in infile: 
        item = item.strip()
        #SPLITING THE DATE AND NAME WITH A COMMA DUE TO FILE OPTIOn
        data = item.split(", ")
        #PUT ITEM IN THE PERFECT POSITION IN OUR LIST
        items[int(data[1])].append(item)
    #ADD ALL ELEMENTS FROM THE ITEMS TO OUR ANSWER
    answer = []
    for item in items:
        if(len(item)>0):
            for x in item:
                answer.append(x)
    return answer
print(SortEmpire("emperors.txt"))
