#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


"""The characteristics of a Python tuple are:

1.Tuples are ordered, indexed collections of data. Similar to string indices, the first value in the tuple will have the index [0], the second value [1], and so on. 
2.Tuples can store duplicate values.
3.Once data is assigned to a tuple, the values cannot be changed."""


# In[6]:


##Creation of tuples
tup = (1,2,3,4,5,66,7,6,5,54,54)


# In[10]:


tup


# In[8]:


##Tuple is immutable if the value is assigned to a tuple the value can not be changed
tup[2] = 6


# In[ ]:





# ANS2

# In[11]:


""" tuple has two method in python 
1.index
2.count"""


# In[13]:


tup1 =(1,2,65,4,5,65)
##1.index method:- this method is used to find occurence of the index of a value which is inside of the tuple
tup1.index(5)


# In[17]:


##2.Count method:-Python count() method counts the occurrence of an element in the tuple. It returns the occurrence of the the element passed during call.
tup1.count(2)


# ANS3
# 

# In[20]:


"""set collection datatypes in python do not allow duplicate items to store."""
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
set1  = set(List)
print(set1)


# ANS4

# In[25]:


"""Difference between union() and update() method
1.union():-union method is used to Return the union of sets as a new set."""


# In[35]:


set2  = {1,2,3,4,5}
set3 =  {2,3,4,5,6,7,8}
set2.union(set3)


# In[39]:


## 2.update():-it is used to return set set2 with elements added from set3.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


# In[ ]:





# ANS5

# In[40]:


"""Distionary: Disctionary is a data stracture that is used to store the key value pair.
and which is ordered changeable and do not allow duplicates."""

dict = {"key1":"Banana","key2":"Aplle","key":"cherry"}


# In[41]:


dict


# ANS6 

# In[43]:


## Netsted Disctionary:- yes we can  create disctionary inside the distionary that is known is as nested disctionary
disct = {"key1":{1,2,3,4,5,6},"key2":{2,3,4,5,6,7},"key3":{6,7,8,9,7,6,5}}


# In[44]:


disct


# ANS7

# In[71]:


dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}


# In[46]:


dict1


# In[76]:


dict1.setdefault("topics", ['Python', 'Machine Learning','Deep Learning'])


# In[77]:


dict1


# In[ ]:





# ANS8 

# In[78]:


## The main view objects of dictionary in python are keys, values and items. They provide a non-constant view of the dictionary’s entries
dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}


# In[79]:


dict1


# In[80]:


##keys
dict1.keys()


# In[81]:


dict1.values()


# In[82]:


dict1.items()


# In[ ]:




