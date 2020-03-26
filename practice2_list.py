# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:26:05 2020

@author: SHARI
"""

#List
#mutable, ordered and changeable. Allows duplicate members.
#####################
#1.constrcting list

list1=[1,2,3,"apple",(11,12),[111,112],{10,20}]
for i in list1:
    print(i)
    
list2=list((1,2,3,"apple",(11,12),[111,112],{10,20}))

list3=[x for x in range(1,10) if x%2==0]

list1+[4,5]

#2.List Methods
#Len() - return length of list
print(len(list1))

#append()- To add an item to the end of the list, use the append() method:
list1.append((4,5)) #now length=length+1

#insert()- To add an item at the specified index, use the insert() method:
list1.insert(0,"orange") #now length=length+1

#remove()- method removes the specified item:
list1.remove("orange")  #now length=length-1

#pop() -method removes the specified index, (or the last item if index is not specified):
list1.pop() #now removes last item since index not specified and returns the deleted item, and  length=length-1
list1.pop(0) # removes item from 0th index , length=length-1

#del keyword removes the specified index:
del list1[0] #delete item from 0th index but never returns deleted item
del list1 #delete complete list

#copy()- deep copy and shallow copy
list2=list1 #shallow copy
list2=list1.copy() #deep copy
list3=list(list1) #deep copy
id(list1)
id(list2)
id(list3)

#join two lists
#method1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1+list2

#method2- using append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for i in list2:
    list1.append(i)

#method3- extend()-which purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)

#count()-Returns the number of elements with the specified value
list1=[1,2,3,4,1,2,3]
list1.count(1) #2,number of elemnets with value 1

#index()-Returns the index of the first element with the specified value
list1=[1,2,3,4,1,2,3]
list1.index(1) #0,first index of 1

#reverse()-Reverses the order of the list
list1=[1,2,3,4,5,6]
list1.reverse()

#sort()-Sorts the list
list1=[3,5,4,1,7,8,2,9]
list1.sort()
#clear()- empties the list
list2.clear() # makes empty list

#min()
min(list1)

#max()
max(list1)