# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:58:33 2020

@author: SHARI
"""

#date: 29/02/2020
#Generators

# 1. program to demonstrate working of yield
def simple_generator():
    yield 1
    yield 2
    yield 3


for value in simple_generator():
    print(value)
    
# 2.A Python program to generate squares from 1 to 100 using yield and therefore generator 
def square_number():
    i=1
    while True:
        yield i*i  #next execution resume from this point
        i=i+1
        
for num in square_number():
    if num>100:
        break
    print(num)


# 3. A Python program to demonstrate use of  generator object with next()  


# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 
print(next(x)); # In Python 3, __next__() 
print(next(x)); 
print(next(x)); 

## 4. A simple generator for Fibonacci Numbers 
def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
        
limit=int(input("enter limit"))        
x=fib(limit)
for i in range(0,limit):
    print(next(x))


# iterating over generator  using for loop 
for i in fib(limit):
    print(i)
    
        
#5. A simple Python program to demonstrate working of iterators 

#create a list
list1=list([1,2,3,4])

# get an iterator using iter()
iter1=iter(list1)

## iterate through it using next() 
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1)) #stopIteration error
        
#6.example for generator function
def genfun():
    n=1
    print("first print")
    yield n
    
    n+=1
    print("second print")
    yield n
    
    n+=1
    print("third print")
    yield n
    
a=genfun()
next(a)
next(a)
next(a)

#7.generators can be used inside for loop
def genfun():
    n=1
    print("first print")
    yield n
    
    n+=1
    print("second print")
    yield n
    
    n+=1
    print("third print")
    yield n
    
for i in genfun():
    print(i)
    
#8.example of a generator that reverses a string.
string=input("enter a string")

def gen_string_fun(string):
    str1=string[-1::-1]
    yield str1
    
for i in gen_string_fun(string):
    print(i)
    
##########################################################
#class portion
    
ee=range(0,10)
for i in range(0,10):
    print(i)
    
list1=range(0,10)
type(list1)

id(list1)

list1=list(range(0,10))
type(list1)

#9.# Generator function for the square of numbers (power of 2)
def square_num(limit):
    for i in range(1,limit+1):
        yield i**2

limit=int(input("enter limit"))
for i in square_num(limit):
    print(i)

#without using generators
def square_num(limit):
    for i in range(1,limit+1):
        print (i**2)

limit=int(input("enter limit"))
square_num(limit)   

#without using generators , list
def square_num(limit):
    list1=[]
    for i in range(1,limit+1):
        list1.append(i**2)
    return list1

limit=int(input("enter limit"))
square_num(limit)   

#10.fibannoci series using generators
def fib_num(limit):
    a,b=0,1
    for i in range(0,limit):
        yield a
        a,b=b,a+b

limit=int(input("enter limit"))
for i in fib_num(limit):
    print(i)
    
# fibannoci without generators using list
def fib_num(limit):
    list1=[]
    a,b=0,1
    for i in range(0,limit):
        list1.append(i)
        a,b=b,a+b
    return list1

limit=int(input("enter limit"))
fib_num(limit)
    
    
#Iterate over string
str1=iter("hello")
next(str1)
    

    

        