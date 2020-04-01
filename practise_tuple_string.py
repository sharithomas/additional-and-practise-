# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:48:46 2020

@author: SHARI
"""

#Tuple
#A tuple is a collection which is ordered and unchangeable , immutable. In Python tuples are written with round brackets.
##########################################
#1.Creating Tuples

#empty tuple
tuple1=()
print(tuple1)

#tuple with one value
tuple1=('shari',) #single value within parenthesis will consider as string so put comma after value to represent single tuple value
print(tuple1)
type(tuple1)

#tuple with multiple values
tuple1=('hello',1,'hai',2)
print(tuple1)

#nested tuple
tuple1=('hello',('python',1),'hai',('java',2))
print(tuple1)
print(tuple1[-1]) #last tuple
print(tuple1[1][0]) #python

#tuple without parenthesis
tuple1='hello',1,'hai',2
print(tuple1)
type(tuple1)

#repetition in tuple
tuple1=('hai',)*3
print(tuple1)

#################################################
#2.methods in tuple

#We cannot change the elements of a tuple because elements of tuple are immutable.However .

#a) changing elements of tuple
tuple1=(123,3.14,100,200)
tuple2=('abc','xyz')
tuple1[2]=300 # error, tuple doesnot support item assignment
tuple3=tuple1+tuple2 #concatenation of 2 tuples
print(tuple3) 

tuple1=(123,[1,2,3],'abc')
tuple1[1][1]='x' #we can change the elements of nested items that are mutable
print(tuple1)

#b) delete tuple
tuple1=(123,3.14,100,200)
del tuple1[1] #error, tuple is immutable
del tuple1 # delete entire tuple
print(tuple1)

#c)slicing in tuple
tuple1=tuple(range(0,10))
print(tuple1)
tuple1[2:5]
tuple1[:4]
tuple1[4:]
tuple1[4:-1]
tuple1[:]

#######################################################
#3.membership test in tuple
data=(11,22,33,44,55,66,77,88,99)
print(data)

print(22 in data) #true
print(20 in data) #false

print(22 not in data) #false
print(20 not in data) #true

#########################################################
#4.iterating a tuple
data=(11,22,33,44,55,66,77,88,99)
for i in data:
    print(i)

#5.length of a tuple
data=(11,22,33,44,55,66,77,88,99)
print(len(data))

#6.count(x)- returns the number of items of x
data=(11,22,33,44,55,66,77,11,22,33,11,88,99)
data.count(11) # returns 3

#7. index(x)- returns first index location of x
data=(11,22,33,44,55,66,77,11,22,33,11,88,99)
data.index(11) #return 0 
#####################################################
#Built in functions 
#1. all() - retruns true if all items in tuples are true or if tuple 
data=(11,22,33,44,55,66,77,11,22,33,11,88,99) #true
data=() #true
data=(11,22,33,44,55,66,77,11,22,33,11,88,99,0) #false
all(data)

#2.any() - returns true if any value is true and false if tuple is empty
data=(11,0,0,0) #true
data=() #false
any(data)

#max()- returns largest item of tuple
data=(11,22,33,44,55,66,77,11,22,33,11,88,99)
max(data)

#min()- returns minimum item of tuple
data=(11,22,33,44,55,66,77,11,22,33,11,88,99)
min(data)

#sorted()-returns  in sorted order
data=(9,12,34,4,22,78,45,28,3,1,90,78)
type(data)
result=sorted(data)
type(result)

#sum()- returns sum of all items
data=(1,2,3,4,5,6)
sum(data)

#####################################################################################3333
#string
##########################################################
string='shari'
string="shari"
string='''my name is  
shari thomas''' #multiline string
string="""my name is 
        shari thomas"""  #multiline string
print(string)

string="shari thomas"
string[0] #first character
string[-1] #last character

#string opertaions
###################################

#1.len() - function to find length of string
string="hello"
len(string)

#2.slicig
string1='this is test string'
print(string1)
string1[9:]
string1[2:6]
string1[:9]
string1[9:-1]
string1[-1:]
string1[-5:-1]

#3.string concatenation
string1="shari"
string2="thomas"
print(string1+" " +string2)

#immutable 
string1="shari"
string1[4]="y" #string immutable
string="malayalam"
for i in string:
    print(i,"at index",string.index(i), "=",id(i) )
       
#address of string
string1="malayalam"
print(id(string1))

string2=string1 #string2 points to the same address of string1
print(string2)
print(id(string2))

print(id(string1+'is a tough lanuage')) #new string address
string2=string1+'is a tough lanuage' #string2 points to new address 
print(string2)
print(id(string2))

#repetition /replication of string
string1='A'*5
print(string1)
print(string1*2)

#membership operators in string
string="welcome to beginners"
string1="welcome"
string2="python"
print(string1 in string) #true
print(string2 in string) #false

print(string1 not in string) #false
print(string2 not in string) #true

#relational operators
str1="ABC"
str2="aBC"
str3="XYZ"
str4="XYz"
print(str2>str1) #true
print(str3>str4) #false
