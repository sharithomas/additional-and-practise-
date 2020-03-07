# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:46:18 2020

@author: SHARI
"""

#date 29/02/2020

# 1.error and exception handling


#The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("an exception occurred")
    
# many exception,
    
#a+1 is make error, ie, print went something wrong
try:
    a=input()
    print(a+1)
except NameError:
    print("variable x is not defined")
except:
    print("went something wrong")

#variable x is not defined NameError
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("went something wrong")


#else , if  no errors then try and else will execute
try:
    print("hello")
except:
    print("error occurred")
else:
    print("nothing wrong")
    
#finally will always execute with try and except
try:
    print("hello")
except:
    print("error")
else:
    print("try except block over")
    
#try to open and close afile that is not writable
try:
    f=open(text.txt)
    f.write("hello")
except:
    print("went something wrong when writing to the file")
finally:
    f.close
    
# raise an error and stop the program if x less than 0
x=-1
if x<0:
    raise Exception(" sorry no numbers below 0")
    
#raise a type error if data is not an integer
a="hello"
if not type(a) is int:
    raise TypeError("data is not integer")

# lecture portion
 
# try , else,finally will execute
try: 
    a=2
    b=3
    c=a+b
    print(c)
except:
    print("error occurred")
else:
    print("no error")
finally:
    print("always running")
    
 
# except,finally will execute
try:
    a=2
    b="hello"
    c=a+b
    print(c)
except:
    print("error occurred")
else:
    print("no error")
finally:
    print("always running")
    
# try to read and write a file
# throw IO error
try:
    f=open('testfile','r')
    f.write("hello")
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("i couldnt open this file in read mode")
else:
    print("written successfully")
    f.close
  
# print written succefully
try:
    f=open('testfile','w')
    f.write("hello")
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("i couldnt open this file in write mode")
else:
    print("written successfully")
    f.close()

# except will execute   
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()


# only try and finally without except and else    
try:
    f = open("testfile", "w")
    f.write("Test write statement")
    f.close()
finally:
    print("Always execute finally code blocks")
    
    

    
def provide_int():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")

    finally:
        print("Finally, I executed!")
    #print(val)
    
provide_int()


def provide_int():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")
        val = int(input("Try again-Please enter an integer: "))
    finally:
        print("Finally, I executed!")
    print(val)
    
provide_int()


def provide_int():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print('u entered',val)
            break
        finally:
            print("Finally, I executed!")
        print(val)
        
provide_int()


#recursion
def factorial_recursive(number):
    if number==1:
        return 1
    else:
        return number*factorial_recursive(number-1)

factorial_recursive(5)