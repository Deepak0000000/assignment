#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


"""Matplotlib is a Python data visualization library that provides a wide variety of plotting options for
data exploration and communication.
Matplotlib allows users to create visualizations in 2D and 3D, including line plots, scatter plots, bar plots,
histograms, and more.

Five plots that can be plotted using the Pyplot module of Matplotlib are:

1.Line plot - a plot of data points connected by straight lines. This is useful for showing trends in data over time or across variables.
2.Scatter plot - a plot of data points in two dimensions with points represented as dots. This is useful for showing relationships between variables and identifying patterns in data.
3.Bar plot - a plot of categorical data with bars representing the frequency or count of each category. This is useful for comparing different categories and identifying trends in data.
4.Histogram - a plot of the frequency distribution of a variable in the form of bars. This is useful for showing the distribution of a variable and identifying the shape of the data.
5.Pie chart - a plot of categorical data where the data is represented as slices of a pie. This is useful for showing the proportion of different categories in a dataset.
"""


# ANS2

# In[2]:


"""
A scatter plot is a type of plot that displays the relationship between two numeric variables.
Each point on the plot represents the values of the two variables for a single observation in the data set.
Scatter plots are useful for identifying patterns, trends, and outliers in data, and for exploring the strength and 
direction of the relationship between two variables.

"""
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))
plt.scatter(x,y)
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()


# ANS3

# In[4]:


""" The subplot() function in Matplotlib is used to create multiple plots within a single figure.
It is particularly useful when you want to compare different data sets or visualize different aspects of
the same data set in a single figure.


"""

import matplotlib.pyplot as plt
import numpy as np

# Define data for the plots
x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])

x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])

x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])

x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])

# Create a figure with four subplots arranged in a 2x2 grid
fig, axs = plt.subplots(nrows=2, ncols=2)

# Plot data on the first subplot
axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('Line Plot 1')

# Plot data on the second subplot
axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('Line Plot 2')

# Plot data on the third subplot
axs[1, 0].plot(x3, y3)
axs[1, 0].set_title('Line Plot 3')

# Plot data on the fourth subplot
axs[1, 1].plot(x4, y4)
axs[1, 1].set_title('Line Plot 4')

# Add overall title to the plot
fig.suptitle('Four Line Plots')

# Adjust spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()


# ANS4

# In[6]:


""" A bar plot, also known as a bar chart, is a type of plot that displays categorical data with rectangular bars. T
he height or length of each bar represents the frequency or proportion of the corresponding category 


"""

import matplotlib.pyplot as plt
import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.bar(company,profit)
plt.show()


# ANS5

# In[12]:


"""A box plot, also known as a box-and-whisker plot, is a type of plot used to display the 
distribution of a numerical variable through their quartiles. The plot consists of a box that 
represents the middle 50% of the data, with a line inside the box that represents the median value."""

import matplotlib.pyplot as plt
import numpy as np
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
data  = [box1,box2]
plt.boxplot(data)
plt.show()


# In[ ]:




