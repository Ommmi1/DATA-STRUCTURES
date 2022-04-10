# implement the hash-table using Linear Probing
# you may add further functions if required
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # return the hash value for 'v'
    # See page #121 of Open Data Structure book
    # for implementation of a hash function
    # OR see https://www.cs.hmc.edu/~geoff/classes/hmc.cs070.200101/homework10/hashfuncs.html
    def __hashed(self, k):
        hash = 0
        for char in str(k):
            hash += ord(char)
        return hash % self.size

    # returns value for the key 'k'
    # returns none if it doesn't exist
    # should run in O(1)
    def hashfunction(self,k,size):
        return k%size
    def Get(self, k):
        startslot = self.hashfunction(k,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == k:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
            if position == startslot:
                stop = True
        return data
    def _get_hash(self, k):
        hash = 0
        for char in str(k):
            hash += ord(char)
        return hash % self.size
    # store value 'v' for the key 'k'
    # if 'k' already in the table then overwrite
    # returns: old value of 'k'
    # should run in O(1)
    def Put(self, k, v):
        hashvalue = self.hashfunction(k,len(self.slots))
        data=None
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = k
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == k:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != k:
                nextslot = self.rehash(nextslot,len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot]=k
                self.data[nextslot]=data
            else:
                self.data[nextslot] = data

    # remove 'k' from the table if exists
    # returns: current value for the key 'k'
    # should run in O(1)
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    def Remove(self, k):
        key_hash = self._get_hash(k)
        if self.slots[key_hash] is None:
            return False
            for i in range (0, len(self.slots[key_hash])):
                if self.slots[key_hash][i][0] == k:
                    self.slots[key_hash].pop(i)
                    return True
            return False
    # returns all keys as a list
    def Keys(self):
        return self.slots

    # returns all values as a list
    def Values(self):
        return self.data

    # returns a list containing key value pairs as
    # tuples i.e. [(k,v)]
    def Entries(self):
        lst=[]
        while len(self.slots)>=len(lst):
            for i in self.slots:
                lst.append(i)
                for j in self.data:
                    lst.append(j)  
                    return lst        
            

    # returns the number of elements 
    def Size(self):
        return len(self.data)

    # returns True if the table is empty
    # otherwise returns false    
    def IsEmpty(self):
        if len(self.data)==0:
            return True
        else:
            return False
    # resize the array when the array 
    def ReSize(self,capacity):
        old = []
        for bucket in self.data:
            if bucket is not None:
                for items in bucket:
                    old.append(items)
        self.data = capacity*[None]
        self.slots = 0
        for items in old:
            [k] = v
# A wrapper for HashTable class to implement
# logic for frequency 
# you may add further functions if required
class FrequencyTable:
    # constructor
    def __init__(self):
        self.hashtable = HashTable()

    # add e in the table and set counter to 1
    # if already exists then add the counter
    # returns the value of counter after adding
    # should run in O(1)
    def Add(self, e):
        pass

    # if the counter of e is greater
    # then 1 then reduce by 1
    # otherwise remove the element
    # returns the current value of counter
    # should run in O(1)
    def Remove(self, e):
        pass

    # returns the total number of elements/locations
    def Count(self):
        pass

    # returns a list of tuples where first value
    # shows the element and second value shows frequency
    # [(1,2),(3,4)] shows two elements 1 and 3 with
    # frequency 2 and 4, respectivelly 
    def Frequency(self):
        pass

# Driving code to load data from files and process
# ********************************************
# YOU ARE NOT REQUIRED TO CHANGE THIS CLASS **
# ********************************************
class FrequencyUtility:
    # constructor
    def __init__(self, entrancefile, exitfile):
        self.entrance = entrancefile
        self.exit = exitfile
        # table to store data
        self.freqTable = FrequencyTable()

    # process the data and returns freuence table
    def Process(self):
        self.__ProcessEntrance()
        self.__ProcessExit()
        return self.freqTable.Frequency()

    # private method to process enterance data
    def __ProcessEntrance(self):
        f = open(self.entrance, "r")
        allLines = f.read().split('\n')
        f.close()

        for aLine in allLines:
            if len(aLine)>0:
                self.freqTable.Add(int(aLine))

    # private method to process exit data
    def __ProcessExit(self):
        f = open(self.exit, "r")
        allLines = f.read().split('\n')
        f.close()

        for aLine in allLines:
            if len(aLine)>0:
                self.freqTable.Remove(int(aLine))
            
        
        
def Test():
    d = FrequencyUtility("entrance.txt","exit.txt")
    print(d.Process())
print(Test())