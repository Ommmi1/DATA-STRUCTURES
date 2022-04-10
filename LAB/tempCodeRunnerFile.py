def shrink(self,value):
        self.create_new_size = len(self.array)-1
        self.newarray = [None for i in range(self.create_new_size)]
        flag=False
        if len(self.array)==0:
            print("Array is empty!")
        else:
            for i in range(len(self.array)):
                try:
                    if self.array[i]!=value and flag == False:
                        self.newarray[i]=self.array[i]
                    elif flag == True or self.array[i]==value:
                        self.newarray[i]=self.array[i+1]
                        flag = True
                    else:
                        flag=True
                except:
                    pass
            self.array=self.newarray
            self.newarray=None