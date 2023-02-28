#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[2]:


"""Multithreading is a threading technique in Python programming to run multiple threads concurrently by
rapidly switching between threads with a CPU help

There are two main modules of multithreading used to handle threads in Python.

The thread module
The threading module"""


# ANS2

# In[4]:


"""the threading module is a high-level implementation of multithreading used to deploy an application in Python. 
To use multithreading, we need to import the threading module in Python Program.

threading.activeCount() − Returns the number of thread objects that are active.

threading.currentThread() − Returns the number of thread objects in the caller's thread control.

threading.enumerate() − Returns a list of all thread objects that are currently active."""


# ANS3

# In[6]:


"""import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print "Starting " + self.name
      print_time(self.name, 5, self.counter)
      print "Exiting " + self.name

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print "%s: %s" % (threadName, time.ctime(time.time()))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"""


# ANS4

# In[7]:


"""A thread is also called a lightweight process. Threads provide a way to improve application performance through parallelism.
Threads represent a software approach to improving performance of operating system by reducing the overhead thread is 
equivalent to a classical process.

Advantages:

Thread switching does not require Kernel mode privileges.
User level thread can run on any operating system.
Scheduling can be application specific in the user level thread.
User level threads are fast to create and manage.

Disadvantages:

In a typical operating system, most system calls are blocking.
Multithreaded application cannot take advantage of multiprocessing."""


# ANS5

# In[8]:


"""Race condition:-A race condition occurs when two threads try to access a shared variable simultaneously.

The first thread reads the value from the shared variable. The second thread also reads the value from the same shared variable.

Deadlocks:
    
The use of locks is an optimal solution to avoid race condition problems, but sometimes, especially if used 
outside of the construct with, they can create some problems.

We have already said that in this case it will be necessary to manage the locks with the acquire() and release() methods,
and once the lock has been acquired by a thread, all the other threads will have to wait for its release before 
proceeding further. This, if not well managed, can lead to deadlocks. That is, if for some reason the thread with the 
lock will never release it, the program will remain locked."""


# In[ ]:




