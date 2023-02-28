#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


"""open function is used to open a file in python 
in python there are many modes to open the file 
EX:
  Mode	Description
r	Open a file for reading. (default)
w	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Open a file for exclusive creation. If the file already exists, the operation fails.
a	Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Open in text mode. (default)
b	Open in binary mode.
+	Open a file for updating (reading and writing)"""
        


# ANS2

# In[2]:


"""close():The close() file Python method can be defined as not closing the file in python which may lead to variability 
    when running your scripts. Hence, implementing the close() file Python method over the opened file in python will 
    help us to save the program resources
    
    f.close()"""


# ANS3

# In[3]:


f  = open("test5.txt","w")


# In[4]:


f.write("I want to become a data scientist")


# In[5]:


f.close()


# In[6]:


data = open("test5.txt",'r')
data.read()


# ANS4

# In[7]:


"""1.readline():Python readline() method will return a line from the file when called.

file = open("filename.txt", "r")
file.readline()

2.readlines():readlines() method will return all the lines in a file in the format of a list where each element is a line in the file

file = open("filename.txt","r")
file.readlines()

3.read():read() method returns the all content of the file
file = open("filename.txt","r")
file.read()


# ANS5

# In[8]:


"""In Python, with statement is used in exception handling to make the code cleaner and much more readable. 
It simplifies the management of common resources like file streams. Observe the following code example on
how the use of with statement makes code cleaner. 

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()
 
# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()
    
# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')"""


# ANS6

# In[ ]:


"""write():
    The write() function will write the content in the file without adding any extra characters.

syntax:
    file_name.write(content) 
    
Example:    
    file = open("Employees.txt", "w")
  
 for i in range(3):
    name = input("Enter the name of the employee: ")
    file.write(name)
    file.write("\n")
     
file.close()
  
print("Data is written into the file.")

writelines() function:
    This function writes the content of a list to a file.
    file_name.writelines(list_of_lines)
Example:
    
file1 = open("Employees.txt", "w")
lst = []
for i in range(3):
    name = input("Enter the name of the employee: ")
    lst.append(name + '\n')
      
file1.writelines(lst)
file1.close()
print("Data is written into the file.") """

