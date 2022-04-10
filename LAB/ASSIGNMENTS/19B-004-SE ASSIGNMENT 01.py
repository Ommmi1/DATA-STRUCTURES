#!/usr/bin/env python
# coding: utf-8

# # MUHAMMAD OMER SIDDIQUI 
# ## 19B-004-SE
# ## ASSIGNMENT 1
# ## SEC A

# ### Write Python functions for the following programs:
# ### 1.Create a class SharpSearchand write functions in Python whose parameters and return value are given below. 
# #### a.Create a constructor which takes a list as parameter and store in as class member.
# def__init__(self,list):
# //yourcodegoeshere
# Example:
# SharpSearchs=SharpSearch([5,4,7,1,4,9])
# #### b.Write a function SearchFirstwhich takes a parameter valueand returnsthe index of the location of the first occurrence of the value. 
# def SearchFirst(self,n):
# //yourcodegoeshereExample:
# Thefollowingistheoutputifweexecutethebelowgivencode
# SharpSearchs=SharpSearch([5,4,7,1,4,9])
# Print(s.SearchFirst(4))
# Output:
# 1
# #### c.Write a function SearchLastwhich takes a parameter valueand returnsthe index of the location of the last occurrence of the valuedefSearchLast(self,n):
# //yourcodegoeshereExample:
# Thefollowingistheoutputifweexecutethebelowgivencode
# SharpSearchs=SharpSearch([5,4,7,1,4,9])
# Print(s.SearchLast(4))
# Print(s.SearchLast(5))
# Print(s.SearchLast(15))
# Output:
# 4
# 0
# -1
# #### d.Write a function Searchwhich takes a parameter valueand returnsthe index of the location of the value. If this function calls for the first time, then it must returnthe location of the first occurrence of the value. On next call, it returns the next occurrence of the location or -1 if the element not found.
# defSearch(self,n):
# //yourcodegoeshereExample:
# Thefollowingistheoutputifweexecutethebelowgivencode
# SharpSearchs=SharpSearch([5,4,7,1,4,9])
# print(s.Search(4))
# print(s.Search(4))
# print(s.Search(4))
# print(s.Search(4))
# Output:
# 1
# 4
# -1
# -1
# #### e.Write a function SearchAllwhich takes a parameter valueand returnsa list containing indicesof all locationsof the value. It returns an empty listif the value does not exist.
# defSearchAll(self,n):
# //yourcodegoeshereExample:
# Thefollowingistheoutputifweexecutethebelowgivencode
# SharpSearchs=SharpSearch([5,4,7,1,4,9])
# print(s.SearchAll(4))
# Output:[1,4]

# In[33]:


class SharpSearch:
    def __init__(self,lis):
        self.lis=lis
    def SearchFirst(self,n):
        for i in lis:
            if lis[i]==n:
                return i
    def SearchLast(self,n):
        for j in reversed(lis):
            if lis[j]==n:
                return j
    def SearchAll(self,n):
        res=[]
        for i in range(len(lis)):
            if n==lis[i]:
                res.append(i)
        return res
    def Search(self,n):
        value=0
        for j in range(len(lis)):
            if(lis[j]==n):
                lis[j]=-1
                value=1
                return j
        if(value==0):
            return -1
lis=[1,2,3,4,4,4,2,5]
object=SharpSearch(lis)
print("The Index Of the Value from first is :",object.SearchFirst(4))
print("The Index Of the Value from last is :",object.SearchLast(4))
print("The Index Of the Value from last is :",object.SearchLast(5))
print("The Index Of the Value from last is :",object.SearchLast(15))
print("The Indexes Of the Value is :",object.SearchAll(4))
print("The 1st Index Of the Value is :",object.Search(4))
print("The 2nd Index Of the Value is :",object.Search(4))
print("The 3rd Index Of the Value is :",object.Search(4))
print("The 4rth Index Of the Value is :",object.Search(4))

