#!/usr/bin/env python
# coding: utf-8

# ANS1
# 

# In[4]:


##Function:- def keyword is used to define the function in python


def find_odd_number_list(k):
    n =[]
    for i in k:
        if i%2!=0:
            n.append(i)
    return n

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

find_odd_number_list(list1)


# ANS2

# In[13]:


##*args:-it is used to store the n numbers of arguments inside the function
def n_numbers_args(*args):
    return args

n_numbers_args(1,2,3,4,[1,2,3,4],True,False,"Python","Java","C++")

""" **kwargs:-it is used to store the elements in the form of key value pair inside the function and it also creates the
disctnories to store the elements"""

def key_value_pair(**kwargs):
    return kwargs

key_value_pair(a=2,b=3,c=5)


# ANS3

# In[12]:


"""Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method. It uses the next() method for iteration.

1.__iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
2.__next__(): The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over. 
This method raises a StopIteration to signal the end of the iteration."""

list= [2, 4, 6, 8, 10, 12, 14, 16,18, 20]

def reutrn_element(a):
    l = []
    for i in a:
        if i ==reutrn_element[a]:
            l.append(i)
            
    return l
reutrn_element(list)


# ANS4 

# In[16]:


"""In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values,
but we don't want to store all of them in memory at once."""

##yield keyword:-the yield keyword is used to produce a value from the generator.

def print_values(n):
    for i in range(n):
        yield i 
       
for i in print_values(10):
    print(i)


# ANS5

# In[1]:


def Prime_Number(n):
    for i in n:
        next(n)
        if i ==n:
            break

n=1000
for i in Prime_Number(n):
    print(i)


# In[ ]:





# In[ ]:




