#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[11]:


"""  The three measures of central tendency are mean, median, and mode.

1.Mean: The mean is the arithmetic average of a dataset and is calculated by summing all values in the dataset and dividing by the number of values. The mean is a useful measure of central tendency for datasets that are normally distributed and have no outliers.

2.Median: The median is the middle value of a dataset and is calculated by arranging the values in ascending order and selecting the middle value. The median is a useful measure of central tendency for datasets that have outliers or are skewed.

3.Mode: The mode is the value that occurs most frequently in a dataset. The mode is a useful measure of central tendency for datasets with categorical or nominal data."""


# ANS2

# In[13]:


"""  The mean is the arithmetic average of a dataset and is calculated by adding up all the values in the dataset
and dividing by the number of values. The mean is sensitive to outliers and extreme values, and can be affected by 
skewed or non-normal distributions.

The median is the middle value in a dataset when the values are arranged in ascending or descending order. 
It is not affected by outliers or extreme values, making it a good measure of central tendency for skewed or
non-normal distributions.

The mode is the value that occurs most frequently in a dataset. It is a useful measure of central tendency for 
datasets with categorical or nominal data, and can also be used for continuous data."""


# ANS3

# In[16]:


list1 = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
import numpy as np
import statistics as stats

np.mean(list1)
np.median(list1)
stats.mode(list1)


# ANS4

# In[17]:


list2  = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
import numpy as np 
np.std(list2)


# ANS5

# In[18]:


"""The range is the difference between the largest and smallest values in a dataset. It provides a simple measure of dispersion but is sensitive to outliers and extreme values.

The variance is a measure of the spread of a dataset relative to the mean. It is calculated by summing the squared difference between each value and the mean, and dividing by the number of values minus one. 
A higher variance indicates a greater spread of data points, while a lower variance indicates a more tightly clustered set of data points.

The standard deviation is the square root of the variance and provides a measure of the dispersion of the data in the same units as the original data.
It is a commonly used measure of dispersion as it is easier to interpret than the variance."""


# ANS6

# In[19]:


"""(i) A B represents the set of elements that are common to both sets A and B. In this case, the common element between A and B is 2 and 6, so:

css
Copy code
A B = {2, 6}
(ii) A ⋃ B represents the set of all elements that are in set A or set B or both. So:

css
Copy code
A ⋃ B = {0, 2, 3, 4, 5, 6, 7, 8, 10}
"""


# ANS7

# In[21]:


""" Skewness is a measure of the asymmetry of a probability distribution or a dataset. 
It is a measure of the extent to which the data is skewed or distorted from a normal or symmetrical distribution.

A distribution or dataset is said to be positively skewed (or skewed to the right)
if the tail on the right side of the distribution is longer or more spread out than the tail on the left side.
In a positively skewed distribution, the mean is generally greater than the median, 
and the mode is the smallest value in the distribution."""


# ANS8

# In[22]:


"""If a dataset is right skewed, then the tail of the distribution will be longer on the right side, 
and the distribution will be pulled towards the right. 
In a right-skewed distribution, the mean will be greater than the median.
This is because the mean is influenced by the extreme values in the tail,
which pull it towards the right, while the median is unaffected by the extreme 
values and remains in the center of the distribution.

So, in summary, if a dataset is right skewed, the median will be less than the mean."""


# ANS9

# In[23]:


""" Covariance and correlation are two measures of the relationship between two variables. 
While they are similar in many ways, they differ in their scale and interpretation.

Covariance is a measure of how two variables vary together. 
It measures the degree to which the two variables move in the same direction, 
with positive covariance indicating that they move together,
negative covariance indicating that they move in opposite directions, 
and zero covariance indicating that they are independent of each other. 
However, the scale of covariance is dependent on the scale of the variables being measured, 
which makes it difficult to compare covariances across different datasets.

Correlation, on the other hand, is a standardized measure of the relationship between two variables.
It measures the strength and direction of the linear relationship between two variables,
with a value between -1 and 1. A correlation of 1 indicates a perfect positive relationship, 
a correlation of -1 indicates a perfect negative relationship, and a correlation of 0 indicates no 
relationship between the variables."""


# ANS10

# In[24]:


"""sample mean = (sum of all values in the sample) / (number of values in the sample)

In symbols:

x̄ = Σx / n"""


# ANS11

# In[25]:


"""  For a normal distribution, the mean, median, and mode are all equal. This is because a normal distribution
is symmetric around its mean, so the mean and median are located at the center of the distribution,
and the mode is the value that occurs with the highest frequency, 
which is also at the center of the distribution."""


# ANS12

# In[26]:


""" Covariance and correlation are both measures of the relationship between two variables in a dataset, but they differ in their scale and interpretation.

Covariance is a measure of how two variables vary together. It is calculated by taking the product 
of the deviations of each variable from their respective means and summing them up.
A positive covariance indicates that the variables tend to increase or decrease together, 
while a negative covariance indicates that the variables tend to move in opposite directions. 
However, the magnitude of the covariance is difficult to interpret, as it depends on the scale of the variables, 
and therefore it is not always clear whether the covariance is large or small.

On the other hand, correlation is a standardized measure of the relationship between two variables. 
It is calculated by dividing the covariance of the variables by the product of their standard deviations. 
Correlation ranges between -1 and 1, where a correlation of -1 indicates a perfect negative relationship,
a correlation of 1 indicates a perfect positive relationship, and a correlation of 0 indicates no relationship. 
Correlation is easier to interpret than covariance, as it is not affected by the scale of the variables.

In summary, covariance measures the strength and direction of the relationship between two variables,
but the magnitude of the covariance is difficult to interpret, while correlation measures the strength 
and direction of the relationship between two variables on a standardized scale, making it easier to interpret.





Regenerate response"""


# ANS13

# In[27]:


"""Outliers are data points that are significantly different from the other observations in a dataset, 
and they can have a significant impact on measures of central tendency and dispersion.

In terms of central tendency, outliers can greatly affect the mean. 
This is because the mean is sensitive to extreme values, and outliers can pull the mean towards them, causing it to become biased.
On the other hand, the median is less affected by outliers,
as it only depends on the order of the values in the dataset. The mode may also be affected,
as an outlier that occurs with a very high frequency can become the new mode.

In terms of dispersion, outliers can greatly affect the range, 
as they can greatly increase or decrease the maximum or minimum values. 
They can also greatly affect the standard deviation and variance, 
as these measures are calculated using the deviations of the data from the mean. 
Outliers can pull the mean away from the center of the distribution, 
which in turn can greatly increase the variance and standard deviation.

For example, consider a dataset of salaries of employees in a company.
If the dataset includes an outlier with a very high salary, 
this can greatly affect the mean salary, making it higher than the typical salary in the company.
Additionally, the outlier can greatly affect the range of salaries, as it increases the maximum value. 
Finally, the presence of the outlier can greatly increase the variance and standard deviation of the dataset, 
indicating that the salaries are more spread out than they actually are for the majority of employees in the company.



"""


# In[ ]:




