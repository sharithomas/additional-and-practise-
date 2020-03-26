# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:55:31 2020

@author: SHARI
"""

#1.comments
#this is single line comments
print("this is single line comment")
'''hai this is multiple line comments
its end here'''

#2.variables in python

#mutliple assignment a=2 and b=3
a,b=2,3

#plus and concatenation operation 
x=10
y=2
print(x+y) # addition of 2 integers 

a="hello"
b="world"
print(a+b) #string concatenation

print(x+a) #type error int+str

#3.number typr conversion
x=20
int1=int(x)
float1=float(x)
complex1=complex(x)
y=2
int2=x+y
float2=int1+float1
complex2=float1+complex1

#4.mathematical functions
#abs(x)- returns absolute value of x
abs(-4) #4
abs(100.33) #100.33
abs(-20.788)#20.788

#ceil(x)-This method returns smallest integer not less than x.
import math
math.ceil(3.14) #4
math.ceil(-3.14) #-3

#cmp(x,y)- returns the sign of the difference of two numbers : -1 if x < y, 0 if x == y, or 1 if x > y.
cmp(80, 100) #-1
cmp(80,80) #0
cmp(100,80)#1

#exp(x)- e^x will return
math.exp(1)

#fabs(x)- returns the absolute value of x in floating point format.
math.fabs(-4)
math.fabs(5)

#floor(x)-the largest integer not greater than x.
math.floor(3.14) #3
math.floor(-3.14) #-4

#log(x)- natural logaritham of x,x>0
math.log(10)

#log10(x)- returns base-10 logarithm of x for x > 0
math.log10(10) #1.0

#max()- returns the largest of its arguments
max(80, 100, 1000) #1000

#min()- returns the smallest of its arguments
min(-20, 100, 400) #-20

#modf() returns the fractional and integer parts of x in a two-item tuple. 
#Both parts have the same sign as x. The integer part is returned as a float.
math.modf(-100.210) #(-0.20999999999999375, -100.0)
math.modf(100.210) #(0.20999999999999375, 100.0)

# pow() returns x to the power of y. If the third argument (z) is given, it returns x to the power of y modulus z, i.e. pow(x, y) % z.
pow(2,3) #8
pow(2,3,5) #2**3=8%5=3

#sqrt() -returns the square root of x for x > 0.
math.sqrt(4) #2.0

# round(x,n) -returns x rounded to n digits from the decimal point
round(21.0978,2) #21.1
round(80.23456, 2)#80.23
round(80.23756, 2) #80.24

#######################
#5.random module
####################33
#seed()- 	Initialize the random number generator
import random
random.seed(10)
print(random.random())

#getstate()- Return the current state of the random generator
import random
print(random.getstate())

#setstate()- Capture and restore the state of the random number generator:
import random
#print a random number:
print(random.random())
#capture the state:
state = random.getstate()
#print another random number:
print(random.random())
#restore the state:
random.setstate(state)
#and the next random number should be the same as when you captured the state:
print(random.random())

#randrange()-Returns a random integer number between the given range 
print(random.randrange(3, 9))

#randint()	-Returns a random number between the given range both 3 and 9 inlucded
print(random.randint(3,9))

#choice()- Return a random element from a list:
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

#choices()-Returns a list with a random selection from the given sequence
#eg:Return a list with 14 items.The list should contain a randomly selection of the values from a specified list,
 #and there should be 10 times higher possibility to select "apple" than the other two:weights- weightagesk=size of list     
 mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, weights = [10, 1, 1], k = 14))

#shuffle()	Takes a sequence and returns the sequence in a random order
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

#sample()- method returns a list with a randomly selection of a specified number of items from a sequnce.
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))

#random()- Returns a random float number between 0 and 1
print(random.random())

#uniform()-Returns a random float number between two given parameters
random.uniform(2,5)

#triangular()	Returns a random float number between two given parameters, you can also set a mode parameter 
#to specify the midpoint between the two other parameters
print(random.triangular(20, 60, 30))

##########################################3
#6.Operators
######################################3
#Arithmertic operators
a = 21
b = 10
c = 0
print(a+b)
print(a-b)
print(a * b)
print( a / b)
print(a % b)

a = 2
b = 3
print(a**b)

a = 10
b = 5
print(a//b) 

############################3
#comparison operators
#########################
a = 21
b = 10
c = 0
a==b
a!=b
a<b
a>b
a<=b
a>=b

#################################
#assignment operators
##################################
a,b=2,4
a+=2
a-=1
a*=1
a/=3
a%=2
a=4
a//=2

#################################
#bitwise operator
#################################
a = 60 #(0011 1100)
b = 13 #(0000 1101)
a&b #12
a|b #61
~a   #-128+64+2+1=-61(NOT)
a^b #49(XOR)
a>>2 #(shift right)
a<<2 #(shift left)

###########################
#logical operator
###########################
a=True
b=False
(a and b)
a or b
not(a and b)
not(a or b)

################################
#Membership operator
############################
a=2
b=8
list1=[1,2,3,4]
a in list1
b not in list1
b in list1

##################################
#Identity operators
###########################
a = 20
b = 20
a is b
a is not b

######################
#address of variables
###################
a=20
b=10
id(a)
id(b)
c=b+10
id(c) 
id(a)==id(c)
print(hex(id(a)))

a=[1,2,3] #shallow copy- reflect in orginal and in its copy
b=a
id(b)
id(a)
a[0]=5
id(a)
id(b)

a=[1,2,3] #deep copy- keeps diffrent copy with different address location
b=a.copy()
id(b)
id(a)
a[0]=6
id(a)
id(b)

######################3
#None- The None keyword is used to define a null value, or no value at all.
#None is not the same as 0, False, or an empty string. None is a datatype of its own (NoneType) and only None can be None.
x=None
print(x)
print(type(x))

a=None
if a:
    print("None ")
else:
    print("Not None type")