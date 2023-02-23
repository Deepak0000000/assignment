#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[6]:


class vichle:
    def __init__(self, name_of_vichle, max_speed, average_of_vehicle):
        self.name_of_vichle= name_of_vichle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle
        
    def return_vehicle_class(self):
        return self.average_of_vehicle,self.max_speed,self.name_of_vichle
    
obj = vichle("Kiger",150,55)
obj.return_vehicle_class()


# ANS2

# In[14]:


class vichle:
    def __init__(self, name_of_vichle,seating_capicity_of_person):
        self.name_of_vichle= name_of_vichle
        self.seating_capicity_of_person= seating_capicity_of_person
        
class car(vichle):
    def seating_capicity(self):
        return self.name_of_vichle,self.seating_capicity_of_person
    
obj = car("bike",2)
obj.seating_capicity()
        
        
        


# ANS3

# In[22]:


##MUltiple inheritence:- When one class inherit the property of more then one class is known as multiple ninheritnce

class G_parents:
    def print1(self):
        print("This is the G_parent class")
        
class Parents:
    def print2(self):
        print("This is the parents class")
        
class son(G_parents,Parents):
    def print3(self):
        print("This is the child class")
        
obj = son()
obj.print3()
obj.print1()
obj.print2()
        


# ANS4

# In[23]:


##A getter method returns the value of a private attribute while a setter method sets the value of a private attribute.

class Person:
    def __init__(self, name, age):
        self._name = name  # private attribute
        self._age = age    # private attribute
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self._age = age
person = Person("Alice", 25)
print(person.get_name())  
person.set_name("Bob")
print(person.get_name())  

print(person.get_age())  
person.set_age(30)
print(person.get_age())   
person.set_age(-1)        


# ANS5

# In[32]:


""" method overriding:-Method overriding is a feature of object-oriented programming where a subclass can
provide a different implementation of a method that is already defined in its superclass"""

class shape:
    def area():
        pass
    

class Rectangle(shape):
    def  __init__(self,length,breath):
        self.length= length
        self.breath = breath
        
    def area(self):
        return self.breath*self.length
    
    
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
        
        
    def area(self):
        return 3.14*self.radius**2
    


obj = Circle(4)
obj.area()
obj1 = Rectangle(2,5)  
obj1.area()


# In[ ]:




