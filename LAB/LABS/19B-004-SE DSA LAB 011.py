#MUHAMMAD OMER SIDDIQUI
#19B-004-SE
#DSA LAB 11

class StringOP:
    #initialization
    def __init__(self,data):
        self.data=data


    def StrLength(self):
        length = 0
        for i in self.data:
            length = length + 1
        return "Length of the String is : {}".format(length)

    def StrConcat(self,string1,string2):
        string=' '
        for i in string1:
            string += i
        for i in string2:
            string += i
        return "After Concatenation: {}".format(string)

    def SubString(self,text,start,end):
        count=0
        Str=' '
        for i in text:
            if start <= count < end:
                Str += i
            count += 1
        return "The Sub String is: {}".format(Str)


#THIS FUNCTION SIMPLY INSERT THE TEXT IN 
#THE GIVEN DATA AT A GIVEN POSITION
    def InsertStr(self,data,text,pos):
        length = 0
        String = " "
        for i in data:
            if length==pos:
                String+=text
            length+=1
            String +=i      
        return "After Insertion of String: {}".format(String)



    def DeleteStr(self,data,pos,length):
        #solved by slicing
        return "After Slicing : {}".format(data[:pos] + data[pos+length:])
    
    #NAIVE METHOD BASICALLY SEARCHES 
    # THE PATTERN FROM THE GIVEN DATA
    def Naive(self,Pattern, text): 
        self.m = len(Pattern)#size of the pattern
        self.n = len(text)#size of the text
        for i in range(self.n - self.m + 1): 
            j = 0
            while(j < self.m): 
                if (text[i + j] != Pattern[j]): 
                    break
                j += 1
            if (j == self.m):  
                return "Pattern found at index: {} ".format(i) 



#DRIVER CODE

obj=StringOP('The quiet brown fox jumps over the lazy dog')
data='The quiet brown fox) jumps over the lazy! dog'
print(obj.StrLength())
print(obj.StrConcat('black','blue'))
print(obj.SubString('feel the pain',3,8))
print(obj.DeleteStr('The quiet brown fox jumps over the lazy dog',2,10))
print(obj.InsertStr(data,'you are here!',10))
print(obj.Naive('brown',data))