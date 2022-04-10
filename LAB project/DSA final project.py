"""DSA FINAL PROJECT ON RESIZABLE ARRAYS USUALLY CAN BE CALLED DYNAMIC ARRAY 
IN COMPUTER SCIENCE, A DYNAMIC ARRAY, GROWABLE ARRAY, RESIZABLE ARRAY, DYNAMIC TABLE,
MUTABLE ARRAY,OR ARRAY LIST IS A RANDOM ACCESS, 
VARIABLE-SIZE LIST DATA STRUCTURE THAT ALLOWS ELEMENTS TO BE ADDED OR REMOVED.
THIS PROJECT IS MADE ACCORDING TO THE GIVEN LINK 
MEMBERS=MUHAMMAD ISMAIL MIAN AND MUHAMMAD OMER SIDDIQUI
GITHUB LINK=https://github.com/omersiddiqui19b004seA/DSA-FINAL-PROJECT """

import ctypes
""" CTYPES IS A FOREIGN FUNCTION LIBRARY FOR PYTHON. 
IT PROVIDES C COMPATIBLE DATA TYPES, AND ALLOWS CALLING 
FUNCTIONS IN DLLS OR SHARED LIBRARIES. 
IT CAN BE USED TO WRAP THESE LIBRARIES IN PURE PYTHON."""
class Resizable_Array:
    """DYNAMIC ARRAY CLASS IT IS MORE SIMILAIAR TO LIST"""
    def __init__(self):
        """INITIALIZATION"""
        self.n=0 #NUMBER OF ELEMENTS
        self.capacity=1 #DEFAULT CAPACITY I.E 1
        self.A=self.make_array(self.capacity)#ACTUAL ARRAY


    def insertAtspecificlocation(self,Value,index):
        """ THIS FUNCTION INSERTS THE ITEM AT ANY SPECIFIED INDEX. """
        if index<0 or index>self.n: 
            print("PLEASE ENTER APPROPRIATE INDEX..") 
            return
          
        if self.n==self.capacity: 
            self._resize(2*self.capacity) 
              
          
        for i in range(self.n-1,index-1,-1): 
            self.A[i+1]=self.A[i] 
              
          
        self.A[index]=Value 
        self.n+=1


    def Insertatend(self, element):
        """ADD ELEMENT AT THE END OF AN ARRAY"""

        if self.n==self.capacity:

            #DOUBLES ITS CAPACITY IF NOT ENOUGH
            self._resize(2*self.capacity)

        self.A[self.n]=element

        #SET SELF.N INDEX TO ELEMENT
        self.n+=1
    
    
    def __len__(self):
        """RETURN NUMBER OF ELEMENTS SORTED IN AN ARRAY"""
        return self.n


    def __getitem__(self, x):
        """RETURN ELEMENT AT INDEX 'x' """
        if not 0<=x<=self.n:
            #CHECK INDEX IF x IS IN ARRAY OR NOT
            return IndexError('x IS OUT OF RANGE')
            #ELSE RETURNS THE VALUE AT THE GIVEN INDEX
        return self.A[x]


    def __str__(self):
        #THIS FUNCTION WILL RETURN THE ARRAY IN THE LIST FORM
        temp=""
        for i in range(self.n):
            #ADDING THE ELEMENTS IN AN ARRAY WITH PROPER LIST PATTERN
            temp=temp + str(self.A[i]) + ","
        temp=temp[:-1]
        #RETURNING THE EXACT ARRAY IN THE LIST FORM
        return "[" + temp + "]"


    def __delitem__(self, index):
        """THSI FUNCTION REMOVES FROM THE GIVEN LOCATION"""
        for i in range(index, self.n-1):
            self.A[i]=self.A[i+1] 
        self.n-=1


    def remove(self, item):
        """THIS FUNCTION REMOVES ITEM FROM A SPECIFIED LOCATION"""
        if self.n==0:
            #CHECK IF ARRAY IS EMPTY
            print("Array is empty, deletion is not Possible") 
            return
                  
        if item<0 or item>=self.n: 
            #CHECK IF INDEX IS IN ARRAY?
            return IndexError("INDEX OUT OF RANGE....DELETION NOT POSSIBLE")         
          
        if item==self.n-1: 
            self.A[item]=0
            self.n-=1
            return

        for i in range(self.n):
            if self.A[i]==item:
                for j in range(i, self.n-1):
                    self.A[j]=self.A[j+1]   
                self.n-=1
                break




    def _resize(self, new_capacity):
        """RESIZE INTERNAL  ARRAY TO NEW CAPACITY"""
        t=self.make_array(new_capacity)# NEW BIGGER ARRAY
        for x in range(self.n):
            #REFERENCE ALL EXISTING VALUES
            t[x]=self.A[x]    
        self.A=t #CALLING NEW BIGGER ARRAY
        self.capacity=new_capacity #RESETTING CAPACITY

        
    def make_array(self,new_capacity):
        """RETURNS NEW ARRAY WITH NEW CAPACITY ARRAY"""
        return (new_capacity * ctypes.py_object)()



#DRIVER CODE
obj=Resizable_Array()
print("THE VALUE SUCCESSFULLY INSERTED AT THE END : {}".format(obj.Insertatend(1)))
print("THE VALUE SUCCESSFULLY INSERTED AT THE END : {}".format(obj.Insertatend(2)))
print("THE VALUE SUCCESSFULLY INSERTED AT THE END : {}".format(obj.Insertatend(3)))
print("Length of an object is : {0}".format(len(obj)))
print("VALUE AT INDEX IS : {0}".format(obj[0]))
print("VALUE AT INDEX IS : {0}".format(obj[1]))
print("VALUE AT INDEX IS : {0}".format(obj[11]))
print("THE VALUE SUCCESSFULLY INSERTED AT THE END : {}".format(obj.Insertatend(4)))
print("THE VALUE SUCCESSFULLY DELETED AT THE END : {}".format(obj.remove(2)))
#del function will also delete the value at the given index
del obj[1]
obj.insertAtspecificlocation(6,3)
print(obj)
