# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:25:53 2020

@author: SHARI
"""

class Book():
    pass

physics_book=Book()
type(physics_book)

class Books():
    def __init__(self,subject):
        self.subject_attribute=subject
        
my_book=Books(subject="Physics")
my_book.subject_attribute

class Books():
    def __init__(self,subject):
        self.subject=subject
        
physics_book=Books('Physics')
physics_book.subject
physics_book.__init__('Maths')


class Books11():
    def __init__(self):
        print('Books11 class created')
        
        
mybook=Books11()


mybook.__init__()
my_book.subject


class Books():
    def __init__(self,subject,author,year):
        self.subject_attribute=subject
        self.author_attribute=author
        self.year_attribute=year
        
my_book=Books(subject="Physics",author="Shravan",year=1992)
my_book.author_attribute

class Books():
    
    book_type="Technical"
    
    def __init__(self,subject,author,year):
        self.subject_attribute=subject
        self.author_attribute=author
        self.year_attribute=year
            
        
my_book=Books(subject="Physics",author="Shravan",year=1992)
my_book.book_type

class Books():
    #CLASS OBJECT ATTRIBUTE
    book_type="Technical"
    
    def __init__(self,subject,author,year):
        self.subject_attribute=subject
        self.author_attribute=author
        self.year_attribute=year
        
    def contains(self, number):
        print("Book is {} Kinamatics and printed {} times since {} ".format(self.subject_attribute, number,self.year_attribute))
            
    

my_book=Books(subject="Physics",author="Shravan",year=1992)
my_book.contains(100)

class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
        
    def circumefrence(self):
        return(2*self.radius*self.pi)
        
mycircle=Circle()
mycircle.radius
mycircle.circumefrence()

        
mycircle=Circle(2)
mycircle.radius
mycircle.circumefrence()

class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
        
    def circumefrence(self):
        return(2*self.radius*Circle.pi)
        
mycircle=Circle(3)
mycircle.radius
mycircle.circumefrence()


class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
        self.area=self.pi*radius*radius
        
    def circumefrence(self):
        return(2*self.radius*Circle.pi)
        
mycircle=Circle(3)
mycircle.radius
mycircle.area
mycircle.pi
mycircle.circumefrence()


'''
Inheritance
Inheritance is a way to form new classes using 
classes that have already been defined. The newly 
formed classes are called derived classes, the 
classes that we derive from are called base classes.
Important benefits of inheritance are code reuse and 
reduction of complexity of a program. The derived classes 
(descendants) override or extend the functionality of base 
classes (ancestors). Let's see an example by incorporating 
our previous work on the Dog class:
'''


class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("I am in Animal and Eating")
        
        
my_animal=Animal() 
my_animal.whoAmI()
my_animal.eat()


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        
        
mydog = Dog()

mydog.whoAmI()

mydog.eat()


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("I am in Dog")

    def bark(self):
        print("I am in Dog and I do bow bow!")
        
mydog = Dog()

mydog.whoAmI()

mydog.eat()

mydog.bark()

'''
Polymorphism
We've learned that while functions can take in
different arguments, methods belong to the objects 
they act on. In Python, polymorphism refers to the 
way in which different object classes can share 
the same method name, and those methods can be 
called from the same place even though a variety of 
different objects might be passed in. The best way 
to explain this is by example:
'''
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return (self.name+' says bow bow!')
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return (self.name+' says Meow!')
    
puppy = Dog('Puppy')
lizy = Cat('Lizy')

print(puppy.speak())
print(lizy.speak())

for pet in puppy,lizy:
    print(pet.speak())
   
for pet in [puppy,lizy]:
    print(pet.speak())
    
    

    
    
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    
    def speak(self):
        return self.name+' says bow bow!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'

animal=Animal('cat') 
animal.name
print(animal.speak())   

puppy = Dog('Puppy')
lizy = Cat('Lizy')

print(puppy.speak())
print(lizy.speak())


#Special Methods

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
        
        
firstbook=Book('Python','Shravan',500)
firstbook.author

print(firstbook)
str(firstbook)
len(firstbook)

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return " %s is written by author: %s contains pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is removed")
        
firstbook=Book('Python','Shravan',500)
        
print(firstbook)
str(firstbook)
len(firstbook)
del(firstbook)
