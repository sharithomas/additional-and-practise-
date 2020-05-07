# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:31:47 2020

@author: SHARI
"""


ee=range(0,10)
for i in range(0,10):
    print(i)
    
list1=range(0,10)

id(list1)

list1=list(range(0,10))


# Generator function for the square of numbers (power of 2)

def gensqr_list(n):
    list1=[]
    for num in range(n):
        list1.append(num**2)
    return(list1)
    
list2=gensqr_list(10)
list2

def gensqr(n):
    for num in range(n):
        yield num**2
        
list3=gensqr(10)
list3

for x in list3:
    print(x)
        
for x in gensqr(10):
    print(x)
    
    
def gen_fibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
        
for num in gen_fibon(10):
    print(num)
    
def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
        
    return output

fibon(10)

for i in fibon(10):
    print(i)
    
    
    
def number_gen():
    for x in range(5):
        yield x
        
# Assign simple_gen 
g = number_gen()

next(g)

print(next(g))


s = 'hello'

#Iterate over string
for let in s:
    print(let)
    
next(s)
list10=range(0,10)
next(list10)

s_iter = iter(s)
next(s_iter)

r_iter=iter(range(0,10))

next(r_iter)