# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:32:26 2020

@author: SHARI
"""

#Python Functions 

#1.creating a function without arguments
def my_function():
    print("my first function")
my_function() #function call

#2. function with arguments
def my_function(string):
    print("this is my "+string+" function")
my_function("first")
my_function("second")

#3. function with 2 arguments
def my_function(fname,lname):
    print(fname+" "+lname)
    
my_function('shari','thomas')

 #4. This function expects 2 arguments, and gets 1 arguments:
def my_function(fname,lname):
    print(fname+" "+lname)
    
my_function('shari') # makes error 

#5. Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in 
#the function definition.This way the function will receive a tuple of arguments, and can access the items accordingly
def sum_fun(*numbers):
    sum_result=0
    for i in numbers:
        sum_result=sum_result+i
    return sum_result   
sum1=sum_fun(1,2,3,4,5,6)
print("sum= ",sum1)


def sum_fun(*args):
    for i in range(len(args)):
        print(args[i])   
sum1=sum_fun(1,2,3,4,5,6)

def sum_fun(*numbers):
    for i in range(len(numbers)):
        print(numbers[i])    
sum1=sum_fun(1,2,3,4,5,6)


list1=[1,2,3,4,5,6]
def sum_fun(*list1):
    for i in range(len(list1)):
        print(list1[i])    
sum1=sum_fun(list1)# pass a list to a function

    
def add_1(a,b):
    return(a+b,b-a) #return multiple values as tuple
f=add_1(5,6) 
print(f)


#5. key word arguments
# You can also send arguments with the key = value syntax. here order doesnot matter
def my_function(child3, child2, child1): 
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#6.Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
# ** before the parameter name in the function definition.
def my_function(**name):
    print(name["fname"]+" " +name["lname"])
    
my_function(fname="shari", lname="thomas")

#7.Default Parameter Value
#If we call the function without argument, it uses the default value:
def my_function(country ="India"):
  print("I am from " + country)

my_function("Sweden")
my_function()
my_function("Brazil")

#8.The pass Statement
#function definitions cannot be empty, but if you for some reason have
#a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass
myfunction()

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)