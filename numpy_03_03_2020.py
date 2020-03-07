# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:56:09 2020

@author: SHARI
"""

# date:03/03/2020

#Numpy
# 1. Python program to demonstrate  basic array characteristics 
import numpy as np 

# creating numpy array
import numpy as np
#rank1
array1=np.array([1,2,3])
print("array with rank 1= ", array1)

#rank2
array1=np.array([1,2,3])
print("array with rank 1= ", array1)


# Creating array object 
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
  
# Printing type of arr object 
print("Array is of type: ", type(arr)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
  
# Printing shape of array 
print("Shape of array: ", arr.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 


## 2. Python program to demonstrate  array creation techniques 
import numpy as np 

# Creating array from list with type float 
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 

# Creating array from tuple 
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b) 

# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4)) 
print ("\nAn array initialized with all zeros:\n", c) 

# Create a constant value array filled with6 of integer type 
d = np.full((3, 3), 6) 

# Create a constant value array of complex type 
d = np.full((3, 3), 6, dtype = 'complex') 
print ("\nAn array initialized with all 6s."
			"Array type is complex:\n", d) 

# Create an array with random values 
e = np.random.random((2, 2)) 
print ("\nA random array:\n", e) 

# Create a sequence of integers 
# from 0 to 30 with steps of 5 
f = np.arange(0, 30, 5) 
print ("\nA sequential array with steps of 5:\n", f) 

# Create a sequence of 10 values in range 0 to 5 
g = np.linspace(0, 5, 10) 
print ("\nA sequential array with 10 values between"
										"0 and 5:\n", g) 

# Reshaping 3X4 array to 2X2X3 array 
arr = np.array([[1, 2, 3, 4], 
				[5, 2, 4, 2], 
				[1, 2, 0, 1]]) 
print(arr.shape)
newarr = arr.reshape(2, 2, 3) 

print ("\nOriginal array:\n", arr) 
print ("Reshaped array:\n", newarr) 

# Flatten array 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
flarr = arr.flatten() 

print ("\nOriginal array:\n", arr) 
print ("Fattened array:\n", flarr) 

#3.# Python program to demonstrate indexing in numpy 
import numpy as np 

# An exemplar array 
arr = np.array([[-1, 2, 0, 4], 
				[4, -0.5, 6, 0], 
				[2.6, 0, 7, 8], 
				[3, -7, 4, 2.0]]) 
print(arr.shape)
print(arr.ndim)
print(arr.size)
# Slicing array 
temp = arr[:2, ::2] 
print ("Array with first 2 rows and alternate"
					"columns(0 and 2):\n", temp) 

# Integer array indexing example 
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
									"(3, 0):\n", temp) 

# boolean array indexing example 
cond = arr > 0 # cond is a boolean array 
temp = arr[cond] 
print ("\nElements greater than 0:\n", temp) 

#4. Python program to demonstrate 
# basic operations on single array 
import numpy as np 

a = np.array([1, 2, 5, 3]) 

# add 1 to every element 
print ("Adding 1 to every element:", a+1) 

# subtract 3 from each element 
print ("Subtracting 3 from each element:", a-3) 

# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 

# square each element 
print ("Squaring each element:", a**2) 

# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 

# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 

print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 

#5.# Python program to demonstrate 
# unary operators in numpy 
import numpy as np 

arr = np.array([[1, 5, 6], 
				[4, 7, 2], 
				[3, 1, 9]]) 

# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", 
					arr.max(axis = 1)) 

# minimum element of array 
print ("Column-wise minimum elements:", 
						arr.min(axis = 0)) 

# sum of array elements 
print ("Sum of all array elements:", 
							arr.sum()) 
print ("Sum of all row elements:", 
							arr.sum(axis=1)) 
print ("Sum of all column elements:", 
							arr.sum(axis=0)) 

# cumulative sum along each row 
print ("Cumulative sum along each row:\n", 
						arr.cumsum(axis = 1)) 

## 5.Python program to demonstrate  binary operators in Numpy 
import numpy as np 

a = np.array([[1, 2], 
			[3, 4]]) 
b = np.array([[4, 3], 
			[2, 1]]) 

# add arrays 
print ("Array sum:\n", a + b) 

# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b) 

# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 

#6Python program to demonstrate 
# universal functions in numpy 
import numpy as np 

# create an array of sine values 
a = np.array([0, np.pi/2, np.pi]) 
print ("Sine values of array elements:", np.sin(a)) 

# exponential values 
a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 

# square root of array values 
print ("Square root of array elements:", np.sqrt(a)) 


#7.# Python program to demonstrate sorting in numpy 
import numpy as np 

a = np.array([[1, 4, 2], 
				[3, 4, 6], 
			[0, -1, 5]]) 

# sorted array 
print ("Array elements in sorted order:\n", 
					np.sort(a, axis = None)) 

# sort array row-wise 
print ("Row-wise sorted array:\n", 
				np.sort(a, axis = 1)) 

# specify sort algorithm 
print ("Column wise sort by applying merge-sort:\n", 
			np.sort(a, axis = 0, kind = 'mergesort')) 

# Example to show sorting of structured array 
# set alias names for dtypes 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 

# Values to be put in array 
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
		('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
			
# Creating array 
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", 
			np.sort(arr, order = 'name')) 
			
print ("Array sorted by grauation year and then cgpa:\n", 
				np.sort(arr, order = ['grad_year', 'cgpa'])) 

# CLASS TOPIC 
import numpy as np
a=np.array([1,2,3,4])
print(a)
a
type(a)
array=np.array(a)
array.ndim # no.of outside square brackets
array.shape 
array.size # no.of elelments
array.dtype #data type of elements

##
data1=np.array([[[[1,2,3,4],[5,6,7,8]],[[12,13,14,15],[16,17,18,19]]],[[[21,22,23,24],[25,26,27,28]],[[31,32,33,34],[35,36,37,38]]]])
data1
data1.ndim
data1.shape
data1.size
data1.dtype

##
data=[[1,2,3,4],
      [5,6,7,8]]
array=np.array(data)

array

array.ndim

array.shape

type(array)

data=[ [[1,2,3,4],
      [5,6,7,8]]  ,

[[1,2,3,4],
      [5,6,7,9]] ]


array=np.array(data)

array

array.ndim

array.shape

type(array)

array.dtype

##
for i in array:
    print(i)
    print("newline")
    
for i in array:
    for j in i:
     print(j)
     print("newline")
     
for i in array: # print each element
    for j in i:
        for k in j:
            print(k)
            print("new line")
            
#for i in array:
#    for j in i:
#        for k in j:
#            for q in k
#            print(q)
#            print("new line")


for i in array.flat: # to  print all elements of array without many for loops
    print(i)
    
list(array.flat) # create a list using flat
tuple(array.flat) # create tuple

for i in np.ravel(array):
    print(i)
 array.flatten
 np.ravel(array)
 
 ##


data=[[1,2,3,True],["hello","world","there","four"]]

array=np.array(data)

array

array.ndim

array.shape


data=[["hello","world","there"],["hello","world","thereeee"]]

array=np.array(data)

array

######################################################################

np.zeros(10)   #1 dimensional array with 10 zeros
np.zeros((2,5)) # 2 rows and 5 columns fill with zeros

np.ones(10)   # #1 dimensional array with 10 ones
np.ones((2,5)) # 2 rows and 5 columns fill with ones

np.full(10,5) #1 dimensional array with 10  elements all with value 5
np.full((10,2),5) # 10 rows and 2 columns all with value 5

np.random.random(10) # fill with random value
np.random.random((3,2))

np.zeros((3,2)).dtype

np.zeros((3,2),dtype="object").dtype # do type casting

k=np.empty((5,2,4))

k=np.empty((5,2,5)) # zero



np.arange(10) # similar to range function 

np.arange(0,20,2)

np.arange(0,10,0.5)


range(0,10,0.5)  # range - float doesnt work

np.array([x/2 for x in range(0,20,1)])



list(range(0,10,1))

np.arange(0,10,3).tolist()   # spec - step size   'n'  , converting to list

np.linspace(0,10,11)  # n --->  step size ?, diving range 0 to 10 by 11 points

#plot graph
from numpy import pi
import matplotlib.pyplot as plt

x= np.linspace(0,2*pi, 50)

f=np.sin(x)
f=np.cos(x)
f=np.exp(x)
plt.plot(x,f)

# change the print options
print(np.arange(10000))

print(np.arange(10000).reshape(100,100))

k=np.arange(10000)
k.shape
npar1=np.arange(10000).reshape(100,100)
npar1=np.arange(10000).reshape(100,1000) #error
npar1=np.arange(10000).reshape(10,1000)
npar1=np.arange(10000).reshape(,1000) #error
npar1=np.arange(10000).reshape(-1,1000) # -ve is considered as remaining elemnts number as dimension. ie 1000x10=10000, so -ve dimension will considered as 10
npar1=np.arange(10000).reshape(10,-1000) # -1000=1000
npar1=np.arange(10000).reshape(-1,-1000)# error cant calculate size 
npar1=np.arange(10000).reshape(10,10,100)
npar1=np.arange(10000).reshape(-1,10,100) #-1 will be 10
npar1=np.arange(10000).reshape(10,-1,100) #-1 will be 10
npar1=np.arange(10000).reshape(-1,-1,100)  #error


##################################################################
#axis parameter
import numpy as np
b = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
b.dtype



np.array([1,2,3])+np.array([4,5,6,7])#error size mismatching
np.array([1,2,3])+np.array([3,6,4])


b.min(axis=2) # collapse row wise
b.min(axis=1) # collapse column wise
b.min(axis=0) # go random like one sheet behind another
b.min()


b.ndim
b.shape


b.sum(axis=None) # total sum

b.sum()

b.sum(axis=0)  # top most dimension sum

b.sum(axis=1) #coulmn sum

b.sum(axis=2) # row sum

b.sum(axis=3) # error axis out of bound




b.min(axis=None)

b.min(axis=0)  # collapse along the top most dimension

b.min(axis=1)  # collapse along the row dimension

b.min(axis=2)  # collapse along the col dimension

########################################################
# methods in numpy
import numpy as np
a = np.array([[1,2,3],
              [1,2,3]])
np.exp(a)
np.sqrt(a)
b=np.add(a,a)
c=np.multiply(a,a)
a.dot(b.reshape(3,2))
d=a.T 
a.reshape(3,2) # never equal to its a.T bcz it follows row or column major
np.transpose(a)

########################################
#Averages and variances
a=np.array([1,2,3,5])
np.median(a)
np.mean(a)
np.average(a)
np.average(a,weights=[5,3,2,1])
np.average(a,weights=[0,0,0,0]) # weights sum zero it cant be normalized

#broadcasting
import numpy as np
a=np.array([[1,2,3,5],[1,2,3,5]])
b=np.array([[1,2,3,5],[1,2,3,5],[1,2,3,5]])
ap=np.array([2])
a+ap
ap1=np.array([[2],[4]])
a+ap1
ap2=np.array([2,5,4,6])
a+ap2
ap3=np.array([[2,5],[4,5]])
ap3.shape
ap3+a #error, broadcast(converting lower dimension to higher dimension to make matching  but mismatching dimension should be 1)

ap4=np.array([2,5])
a+ap4 #error , mismaching dimension is not 1
ap5=np.array([2]) # mismatching dimensions are 1 so it can replicate
ap5+a

a = np.array([[1,2,3,5],[1,2,3,5]])
b = np.array([[1,2,3,5],[1,2,3,5],[1,2,3,5]])
c = np.array([1,2,3,5])
c = np.array([[1],
             [2]])
e = np.array([[1,2],
             [2,6]])
d = np.array([2])
a
w=[1,2,3,4]

a+e # broadcating error
a+b # broadcating error
a+c 
a+2

a+d

a*w
a-w

pro=np.array([5,3,2,1])
w=(np.array([5,3,2,1])/ np.array([5,3,2,1]).sum())*100 #use of broad casting, to find percentage for each elements

pro=np.array([5,3,2,1])
w=(np.array([5,3,2,1])/ np.array([5,3,2,1]).sum())*100 #use of broad casting

pro1=np.array([[5,3,2,1],[4,6,8,12]])
w=(np.array([5,3,2,1])/ np.array([5,3,2,1]).sum())*100 #use of broad casting

pro_c_sum=pro1.sum(axis=1) #column
pro_c_sum.reshape(2,1)
#pro_c_sum.shape
#r=pro_c_sum.T.shape
#np.dot(pro_c_sum.T,pro_c_sum)
#pro1/pro_c_sum

pro_c_sum.reshape(2,1)
vitper=(pro1/pro_c_sum.reshape(2,1))*100

# boolean indexing
import numpy as np
ar = np.arange(10)

ar[[True,False,True,False,True,False,True,False,True,False]]

ar[0]
ar[0:5] 

ar[0:6:2]
ar[0: :2]
ar[0:]
ar[0:  :  ]
ar[::2]

ar[ : :-1]
ar[-3:0:1]
ar[-1:-10:-1]
ar[-1::-1]
ar[0]
ar[0:5]
ar[0:6:2]
#boolean indexing
data=np.random.randn(4,3)
bool1=np.array((True,False,True,False))
bool2=np.array((True,False,True))
data[0:2]
data[0:2,]
data[:,0:2]
data[0:2,0:2]
data[bool1,:]
data[bool1,bool2]

### BOOLEAN INDEXING

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

names

data = np.random.randn(7, 4)

data

bool1=np.array([True,False,True,False,False,False,True])

bool1

data[0:2 , 0:3]

data[ bool1  ,  :   ]

data

#slicing
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[2,0]
arr2d[2][0]
arr2d[[0,1]] # rows
arr2d[,[0,1]] #error
arr2d[:,[0,1]]
arr2d[:,[2,1]]
arr2d[[2,0,1]]
arr2d[[0,1],[1,0]] #(0,1)(1,0)
#############################################3

data = np.array(  [
                  [ 56  , 0   , 4.4 , 68 ],
                  [ 1.2 , 104 , 52  , 8  ],
                  [ 1.8 , 135 , 99  , 0.9], ]
             )



data

data.shape

data.mean(axis=0)

data.std(axis=0)

(data  - data.mean(axis=0))/data.std(axis=0)

###################################################
import numpy as np

data=np.array([[56,0,4,4,68],[1.2,104,52,8],[18,135,99,0.9]])

#z-transformation
#(x-mean)/std.dev

data.mean(axis=0)
data.std(axis=0)

(data-data.mean(axis=0))/data.std(axis=0)

(data-data.mean(axis=1).reshape(3,-1))/data.std(axis=1) .reshape(3,-1) #reshape(3,-1) =reshape(3,1)

###################33
a=np.array([[1,2,3,4],[5,6,7,8]])
a.shape
a.T
np.transpose(a)
a=a.reshape((2,4))
a.reshape((4,-1),order='F') # F-column major,C- row major
a.reshape((4,-1),order='C')
a.reshape(4,-1) # C- major

########################3
