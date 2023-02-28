#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[8]:


"""Exception: Exception is the mechanism to handle the run time errors
Syntax Errors
try :
    10/0
except ZeroDivisionError as e :
    print(e)
Syntax errors are perhaps the most common kind of complaint you get while you are still learning Python. Example:

while True print('Hello world')
File "<stdin>", line 1
while True print('Hello world')"""
                   


# ANS2

# In[12]:


"""If the exception is not handled in python then the below code of the exception will not be excute

try:
    a=10
    a/0
    print("there is the some issue with this code")"""


# ANS3

# In[13]:


"""In python programming language ""except Exception as e:" statement is used to handle the any type of exception that is occured 
at the run time
#print always a valid msg
try :
    10/0
except ZeroDivisionError as e :
    print("this is my zero dedision error i am handling " , e)"""


# ANS4

# In[14]:


a.try:
    a= 10
    a/0
except ZeroDivisionError as e:
    print("I  am handling zero division Error:",e)
else:
    print("Else block will excute only if the try block is excuted without any error")


# In[15]:


try:
    a= 10
    a/5
except ZeroDivisionError as e:
    print("I  am handling zero division Error:",e)
else:
    print("Else block will excute only if the try block is excuted without any error")


# In[17]:


##b.Finally(): finally block will always excute weather the exception is handled or not
try:
    a= 10
    a/0

finally:
    print("Else block will excute only if the try block is excuted without any error")


# In[18]:


class validateage(Exception) : 
    def __init__(self, msg) :
        self.msg = msg
def validate_age(age) : 
    if age < 0 : 
        raise validateage("age should not be lesser then zeor " )
    elif age > 200 : 
        raise validateage("age is too high " )
        
    else :
        print("age is valid") 
try : 
    age = int(input("enter your age"))
    validate_age(age)
except validateage as e : 
    print(e)


# ANS5

# In[20]:


"""custome exception Handling:In Python, we can define custom exceptions by creating a 
new class that is derived from the built-in Exception class.
class validateage(Exception) : 
    def __init__(self, msg) :
        self.msg = msg
def validate_age(age) : 
    if age < 0 : 
        raise validateage("age should not be lesser then zeor " )
    elif age > 200 : 
        raise validateage("age is too high " )
        
    else :
        print("age is valid") 
try : 
    age = int(input("enter your age"))
    validate_age(age)
except validateage as e : 
    print(e)"""


# ANS6

# In[ ]:


class validateage(Exception) : 
    def __init__(self, msg) :
        self.msg = msg
def validate_age(age) : 
    if age < 0 : 
        raise validateage("age should not be lesser then zeor " )
    elif age > 200 : 
        raise validateage("age is too high " )
        
    else :
        print("age is valid") 
try : 
    age = int(input("enter your age"))
    validate_age(age)
except validateage as e : 
    print(e)

