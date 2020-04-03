# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:29:42 2020

@author: SHARI
"""

#sets
#unordered(random order) and unindexed(cannot access the elements of a set using the indexes )
#1.creating sets
########################################
my_set={"hai","python",1,2,3.4,'hello'}
print(my_set)
type(my_set)

set1=set() #empty set
print(set1)
type(set1)

set1=set(["hai","python",1,2,3.4,'hello']) #converting alist into a set
print(set1)
type(set1)
len(set1)

set1=set({2,6,8,9,10})
set1=set([2,6,8,9,10])
print(set1)
type(set1)

#2. methods of set
###########################################
#2.a) add()-	Adds an element to the set and If the element already exists, the add() method does not add the element.
fruits={"apple","orange","plum"}
fruits.add("banana")
print(fruits)

fruits={"apple","orange","plum"}
fruits.add("plum")
print(fruits)

#2.b)clear()- Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#2.c)copy()- Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
fruits_copy= fruits.copy()
print(fruits_copy)

#2.d)difference()-Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #x-y
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x) #y-x
print(z)

#2.e) difference_update()- Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) # x =x-y
print(x)

#2.f)discard()- Remove the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") #Remove "banana" from the set
print(fruits)

#2.g) intersection()- Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)#  x&y , Return a set that contains the items that exist in both set x, and set y
print(z)


x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
w={"s","c","f"}
result = x.intersection(y, z,w)
print(result)

#2.h) intersection_update()-  Removes the items in this set that are not present in other, specified set(s) ,method removes the unwanted items from the original set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#2.i) isdisjoint()- Returns whether two sets have a intersection or not, true- if intersection null and false- if intersection not null
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft","apple"}
print(x.isdisjoint(y)) 

#2.j) issubset()- Returns whether another set contains this set or not
x={1,2,3,4,5}
y={1,3}
print(y.issubset(x))

#2.k) issuperset()- Returns whether this set contains another set or not
x={1,2,3,4,5}
y={1,3}
print(x.issuperset(y))

#2.l) pop()- Remove a random item from the set
x={1,2,3,4,5}
x.pop()

#2.m) remove()- Removes the specified element
x={1,2,3,4,5}
x.remove(1) # removes 1 from set

#2.n) symmetric_difference()- Return a set that contains all items from both sets, except items that are present in both sets:
#x-y U y-x
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
x ^ y
(x-y)|(y-x)
print(z)

#2.o)symmetric_difference_update()- Return and update set with all items from both sets, except items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#2.p) union()- 	Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.union(y) #x|y 

#2.q) update()- Update the set with the union of this set and others
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

######################################
#membership operators
x = {"apple", "banana", "cherry"}
"apple" in x
"apple" not in x

##########################################
#sets vs frozensets - sets are mutable but frozensets are immutable
# sets have add, remove, discard, pop but frozensets dont have that.
set1 = {'a','b','c','d',1,2,3,False}
set1.add(7)

set2 =frozenset([1,2,3,4,5,6,7,8])
type(set2)
set2[0]
set2.add(7)
set2.remove(5)

set3 =frozenset([1,2,3,4,5,6,7])
a=set2-set3
print(a)
type(a)

#########################################################3
###############################################################
#Dictionary
# unordered , a dictionary has a key: value pair , separated by a colon (:), enclosed in curly braces {}

#creating dictionaries
my_dict={} #empty dictionary
print(my_dict)

my_dict={1:"apple",2:"orange"} #
print(my_dict)

my_dict={1:"apple",'a':"orange",2:[10,20,30]}
print(my_dict)

my_dict=dict({1 : 'apple',2 : 'orange'})
print(my_dict)

my_dict=dict([(1,'apple'),(2 ,'orange')])
print(my_dict)




dict1={}
dict1['A'] = 'AA'
dict1['B'] = 'BB'
print(dict1)
dict2 = { }
dict2['A'] = (1,2,3)
dict2['A'] = 2
dict2['B'] = 'BB'
dict2

############################################3
#dictionary comprehension
my_dict=dict({1 : 'apple',2 : 'orange',3:'banana'})
dict1={k:v for k,v in my_dict.items() }
print(dict1)

dict3=dict([  ('x',2) , ('y',20), ('z',40)  ])
type(dict3.items())
dict3.keys()
dict3.values()

for i in (range(0,10)):
    print(i)

for i in enumerate (range(10,20)):
    print(i)
    
for i,k in enumerate (range(10,20)):
    print(i,k)

{k:v for k,v in enumerate(range(10,20))}

{k:v*10 for k,v in enumerate(range(0,10))}

{k:v*10 for k,v in dict3.items() if k=='x'}
{k:v*10 for k,v in dict3.items() if k!='x'}

dict2={'A': 2, 'B': 'BB'}

{k:v*10 for k,v in dict2.items() if k!='A' and k!='B'}

{k:v*10 for k,v in dict2.items() if k!='A' if k!='B'}

{k:(v*10 if k!='A' else v*20) for k,v in dict2.items()}

{k:v for k,v in dict2.items()}

{k:(v*10 if k!='A' else v*20) for k,v in dict2.items()}

#########################################################
#Acesssing items
#1. can access the items of a dictionary by referring to its key name
thisdict = { "brand": "Ford", "model": "Mustang","year": 1964 }
print(thisdict["model"])
#2. get()- Get the value of a  key
thisdict = { "brand": "Ford", "model": "Mustang","year": 1964 }
print(thisdict.get("brand"))

#######################################
#changing values
my_dict={'name':'jack','age':27}
print(my_dict)

my_dict['age']=29 #upadte value
print(my_dict)

my_dict['address']='bangalore' #add item
print(my_dict)

#################################################
#loop through dictionary
my_dict={'name':'jack','age':27}

 # print all keys one by one
for x in my_dict:
    print(x) 
    
for x in my_dict.keys():
    print(x)
# print all values one by one
for x in my_dict:
    print(my_dict[x]) # print all values

for x in my_dict.values():
    print(x)

# print all items of dictionary one by one 
for x in my_dict.items():
    print(x)
    
for x,y in my_dict.items():
    print(x,y)

######################################################
#check if key exists using keyword 'in'
my_dict={'name':'jack','age':27}
bool_value="age" in my_dict
print(bool_value)
if 'name' in my_dict:
    print("yes, name key is exist in my_dict")

##########################################3
#len()- returns number of items in dictionary
my_dict={'name':'jack','age':27}
print(len(my_dict))

###############################################
#removing items
#1.pop()- method removes the item with the specified key name
my_dict = {"brand": "Ford", "model": "Mustang", "year":2000}
my_dict.pop("model")
print(my_dict)

#2.popitem() method removes the last inserted item
my_dict = {"brand": "Ford", "model": "Mustang", "year":2000}
my_dict['place']='bangalore'
print(my_dict)
print(my_dict.popitem())
print(my_dict)

#3.del keyword removes the item with the specified key name
my_dict = {"brand": "Ford", "model": "Mustang", "year":2000}
del my_dict['year']
print(my_dict)
del my_dict

#4.clear()- method empties the dictionary
my_dict = {"brand": "Ford", "model": "Mustang", "year":2000}
my_dict.clear()
print(my_dict)

######################################################
#copy a dictionary
#shallow copy - changes made in my_dict will reflect in new_dict also
my_dict = {"brand": "Ford", "model": "Mustang", "year":2000}
new_dict=my_dict
my_dict['year']=2005
print(my_dict)
print(new_dict)

#deep copy-changes made in my_dict will not make any changes in  new_dict
my_dict = {"brand": "Ford", "model": "Mustang", "year":2000}
new_dict=my_dict.copy()
my_dict['year']=2005
print(my_dict)
print(new_dict)

#Another way to make a copy is to use the built-in method dict().
my_dict = {"brand": "Ford", "model": "Mustang", "year":2000}
new_dict=dict(my_dict )
my_dict['year']=2005
print(my_dict)
print(new_dict)

###################################################
#Nested dictionaries
myfamily = { "child1" : {"name" : "Emil", "year" : 2004}, "child2" : { "name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus",
    "year" : 2011} }
print(myfamily)
print(myfamily.keys())
print(myfamily.values())

child1 = {"name" : "Emil", "year" : 2004}
child2 =  { "name" : "Tobias","year" : 2007}
child3 =  {"name" : "Linus", "year" : 2011}
myfamily= {"child1": child1,"child2" : child2, "child3": child3}
print(myfamily)

#fromkeys() - method returns a dictionary with the specified keys and the specified value.
x = ('key1', 'key2', 'key3')
y=0
this_dict=dict.fromkeys(x,y) #create dictionary with 3 keys, all with the value 0:
print(this_dict)

x = ('key1', 'key2', 'key3')
this_dict=dict.fromkeys(x) #create dictionary with 3 keys, all with the value None
print(this_dict)

#The setdefault()- method returns the value of the item with the specified key. If the key does not exist, insert the key,
# with the specified value, see example below
car = { "brand": "Ford",  "model": "Mustang", "year": 1964 }
x = car.setdefault("model", "Bronco")
print(x)

x = car.setdefault("place","bangalore")
print(x)

#update() method inserts the specified items to the dictionary.
car = { "brand": "Ford", "model": "Mustang", "year": 1964 }
car.update({"color": "blue"})
car.update({"brand": "tata"})
print(car)