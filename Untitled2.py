#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[2]:


"""1.Scatter Plot: A scatter plot is used to display the relationship between two continuous variables. It's ideal for showing the correlation between variables.

2.Line Plot: A line plot is a graph that displays information as a series of data points connected by straight lines. It is ideal for representing time-series data, showing how the data changes over time.

3.Histogram: A histogram is a graphical representation of the distribution of numerical data. It's ideal for visualizing the shape of the distribution and helps in identifying any outliers in the data.

4.Bar Plot: A bar plot displays data with rectangular bars with heights or lengths proportional to the values they represent. It's ideal for displaying data that is categorical, showing the frequency of each category.

5.Heatmap: A heatmap is a graphical representation of data in which values are represented as colors. It's ideal for showing patterns in large datasets, such as identifying clusters or correlations between variables"""



# ANS2

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns

fmri = sns.load_dataset('fmri')
sns.lineplot(x='timepoint',y='signal',hue='event',style='region',data=fmri)
plt.show()


# ANS3

# In[4]:


import seaborn as sns
titanic_data = sns.load_dataset('titanic')

sns.boxplot(x='pclass', y='age', data=titanic_data)
sns.boxplot(x='pclass', y='fare', data=titanic_data)


# In[ ]:





# ANS4

# In[7]:


import seaborn as sns
diamonds_data = sns.load_dataset('diamonds')
sns.histplot(data=diamonds_data, x='price', hue='cut', multiple='stack', kde=False)


# ANS5

# In[13]:


import seaborn as sns
iris = sns.load_dataset('iris')
sns.pairplot(iris)


# ANS6

# In[18]:


import seaborn as sns
flights_data = sns.load_dataset('flights')
flights_data = flights_data.pivot('month', 'year', 'passengers')
sns.heatmap(flights_data, cmap='YlGnBu')


# In[ ]:





# In[ ]:




