#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[13]:


"""class:-Classes are user-defined data types that act as the blueprint for individual objects, attributes and methods.
Objects:-Objects are instances of a class created with specifically defined data.
Objects can correspond to real-world objects or an abstract entity. """


##Example:-
    
class Employee:
    def __init__(self,emp_name,emp_addhar_number,emp_address):
        self.emp_name =emp_name
        self.emp_addhar_number = emp_addhar_number
        self.emp_address = emp_address
        
    def return_emp_details(self):
        return self.emp_name,self.emp_addhar_number,self.emp_address
    
details = Employee("Raj",213243216545,"Noida UP")
details.emp_addhar_number
details.emp_address
details.emp_name
details.return_emp_details()


# ANS2

# In[18]:


"""1.Encapsulation: This refers to the concept of bundling data and methods that operate on that data within a single unit or object. 

2 Abstraction: Abstraction is the process of identifying the essential characteristics of an object or system, and ignoring or hiding the irrelevant details. 

3 Inheritance: Inheritance is the process by which one class inherits the properties and methods of another class. 

4 Polymorphism: Polymorphism refers to the ability of objects to take on multiple forms or behaviors. In OOP, polymorphism is achieved through method overriding and method overloading. """


# ANS3

# In[19]:


"""__init__:-In object-oriented programming (OOP), the __init__() function is a special method that is automatically called 
when an object of a class is created. It is used to initialize the object's attributes or properties with values
passed in as arguments when the object is created."""



class Rectangle:
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
        
    def Area(self):
        return self.breath*self.length
    
area = Rectangle(5,6)


# In[20]:


area.Area()


# ANS4

# In[27]:


"""the self keyword is used to refer to the instance of a class that is being operated on.
It is a reference to the current object or instance of a class, 
and is used to access its attributes and methods."""

##Example:-
    

class car:
    def __init__(self,make,model,year):
        self.make= make
        self.model= model
        self.year = year
        
    def get_details_car(self):
        return self.make,self.model,self.year
    
    
details = car("Toyota","Carmy",2022)
details.make
details.model
details.year
details.get_details_car()


# ANS5

# In[28]:


"""Inheritence:-Inheritance is a mechanism in object-oriented programming that allows a class to inherit properties 
and behavior from another class. 


There are four types of inheritance in OOP:"""
   ## 1.Single inheritance:
    
    
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog("Rufus")
print(my_dog.name)  
print(my_dog.speak()) 


# In[29]:


##2.Multiple inheritance: 

class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")

my_c = C()
my_c.method_a() 
my_c.method_b()  
my_c.method_c()  


# In[30]:


##3.Hierarchical inheritance:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

my_dog = Dog("Rufus")
my_cat = Cat("Socks")
print(my_dog.name)  
print(my_dog.speak()) 
print(my_cat.name)  
print(my_cat.speak())  





# In[ ]:




