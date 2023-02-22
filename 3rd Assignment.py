#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[21]:


players = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

sorted_players = sorted(players, key=lambda x: x[1], reverse=True)

print(sorted_players)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ANS2

# In[4]:


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(map(lambda x:x**2,l))


# In[ ]:





# In[ ]:





# ANS3
# 

# In[5]:


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple(map(lambda x:str(x),l))


# ANS4

# In[8]:


from functools import  reduce
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
reduce(lambda x,y:x*y,list1)


# In[ ]:





# In[ ]:





# In[ ]:





# ANS5

# In[14]:


list2 = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x:x%2==0 and x%3==0,list1))


# In[2]:





# ANS6 

# In[19]:




list2 = ['python', 'php', 'aba', 'radar', 'level']


# In[20]:




palindromes = list(filter(lambda x: x == x[::-1], list2))

print(palindromes)


# ANS7

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ANS8 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




