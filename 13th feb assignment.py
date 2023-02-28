#!/usr/bin/env python
# coding: utf-8

# ANS2

# In[1]:



# import inspect module
import inspect
  
# our treeClass function
def treeClass(cls, ind = 0):
    
      # print name of the class
    print ('-' * ind, cls.__name__)
      
    # iterating through subclasses
    for i in cls.__subclasses__():
        treeClass(i, ind + 3)
  
print("Hierarchy for Built-in exceptions is : ")
  
# inspect.getmro() Return a tuple 
# of class  cls’s base classes.
  
# building a tree hierarchy 
inspect.getclasstree(inspect.getmro(BaseException))
  
# function call
treeClass(BaseException)


# ANS3

# In[3]:


"""The ArithmeticError Exception is the base class for all errors associated with arithmetic operation.
ArithmeticError
--> ZeroDivisionError
--> OverflowError
--> FloatingPointError


1 - Handling ZeroDivisionError
try:
    1/0
except ArithmeticError as e:
    print(f"{e}, {e.__class__}")
    
2 - Handling OverflowError
j = 5.0

try:
    for i in range(1, 1000):
        j = j**i
except ArithmeticError as e:
    print(f"{e}, {e.__class__}")"""


# ANS4

# In[5]:


"""LookupError Exception is the Base class for errors raised when something can’t be found.
The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid:
IndexError, KeyError.

import sys
try:
foo = [a, s, d, f, g]
print foo[5]
except IndexError as e:
print e
print sys.exc_type


1. keyError:Keyerror mthod is used to handle the keyError exception which is not found by the key
    try :
    d = {1: [3,4,5,6] , "key" :"sudh"}
    d["key10"]
except KeyError as e : 
    print(e)
    
2. IndexError: IndexError method is used to handle thelist Index out of range
    
    try :
    l = [1,2,3,3]
    l[10]
except IndexError as e :
    print(e)"""
    


# ANS5

# In[7]:


"""1.moduleNotFoundError: ModulenotFounderror occures when the path of the module is not correct 
try :
    import sudh
except ImportError as e : 
    print(e)"""
    
    


# ANS6:

# In[ ]:


"""#use always a specific exception
try :
    10/0
except Exception as e :
    print(e)
    
    
try :
    10/0
except ZeroDivisionError as e :
    print(e)
    
#print always a valid msg
try :
    10/0
except ZeroDivisionError as e :
    print("this is my zero dedision error i am handling " , e)

#always try to log 
import logging
logging.basicConfig(filename = "error.log" , level = logging.ERROR)
try :
    10/0
except ZeroDivisionError as e :
    logging.error("this is my zero dedision error i am handling {} ".format( e))"""

