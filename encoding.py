#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[21]:


"""Ordinal Encoding and Label Encoding are both techniques used to convert categorical data into numerical data, but they differ in how they assign numerical values to the categories.

Ordinal Encoding assigns numerical values to the categories based on their order or rank in the dataset. For example, if we have a categorical feature "size" with categories "small", "medium", and "large", we can assign the values 1, 2, and 3 respectively, as "small" is ranked lower than "medium", and "medium" is ranked lower than "large".

On the other hand, Label Encoding assigns numerical values to the categories arbitrarily, usually starting from 0. Using the same example as above, we could assign the values 0, 1, and 2 to "small", "medium", and "large" respectively, without taking into account their order or any other information.

When to use Ordinal Encoding versus Label Encoding depends on the specific dataset and the problem at hand. If the categorical variable has a clear ordering, such as "low", "medium", and "high", then Ordinal Encoding is appropriate. If there is no clear ordering, such as with "red", "green", and "blue", then Label Encoding can be used."""


# ANS2

# In[22]:


""" Target Guided Ordinal Encoding is a technique used to encode categorical variables based on their correlation with the target variable. It is a variation of Ordinal Encoding, where the numerical values assigned to the categories are determined by their relationship with the target variable.

The basic idea behind Target Guided Ordinal Encoding is to replace each category with a value that represents the likelihood of that category leading to a certain outcome. This is achieved by calculating the mean of the target variable for each category, and then encoding the categories based on their corresponding mean values. Categories with higher mean values are assigned a higher numerical value, and those with lower mean values are assigned a lower numerical value."""


# ANS3

# In[23]:


""" Covariance is a statistical measure that quantifies the degree to which two variables are related to each other. More specifically, covariance measures the joint variability between two variables, meaning how much they vary together in relation to their individual means. If the two variables tend to move in the same direction, then their covariance will be positive, whereas if they tend to move in opposite directions, then their covariance will be negative.

Covariance is important in statistical analysis because it helps us understand the relationship between two variables. Specifically, it allows us to determine whether two variables are positively or negatively correlated, and how strong that correlation is. Covariance can also be used in other statistical techniques, such as principal component analysis and linear regression.

Covariance is calculated by taking the product of the deviation of each variable from its mean and then summing those products over all observations. More formally, the covariance between two variables X and Y, with means μx and μy, respectively, is given by the following formula:

cov(X,Y) = Σ[(Xi - μx) * (Yi - μy)] / (n-1)"""


# ANS4

# In[24]:


from sklearn.preprocessing import LabelEncoder
import pandas as pd

# create a sample dataset
data = {
    'Color': ['red', 'green', 'blue', 'blue', 'red', 'green'],
    'Size': ['small', 'medium', 'small', 'large', 'medium', 'large'],
    'Material': ['wood', 'metal', 'plastic', 'wood', 'metal', 'plastic']
}

# create a pandas dataframe from the data
df = pd.DataFrame(data)

# create a LabelEncoder object
le = LabelEncoder()

# encode the categorical variables using LabelEncoder
df['Color'] = le.fit_transform(df['Color'])
df['Size'] = le.fit_transform(df['Size'])
df['Material'] = le.fit_transform(df['Material'])

# print the encoded dataframe
print(df)


# ANS5

# In[25]:


import pandas as pd

# create a sample dataset
data = {
    'Age': [30, 40, 25, 35, 50],
    'Income': [50000, 75000, 40000, 60000, 90000],
    'Education': [12, 16, 10, 14, 18]
}

# create a pandas dataframe from the data
df = pd.DataFrame(data)

# calculate the covariance matrix
covariance_matrix = df.cov()

# print the covariance matrix
print(covariance_matrix)


# ANS6

# In[26]:


"""For the categorical variable "Gender," we can use label encoding, as there are only two categories, Male and Female. We can assign the values 0 and 1 to Male and Female, respectively.

For the categorical variable "Education Level," we can use ordinal encoding. The categories have a natural order, with High School being the lowest level of education and PhD being the highest level of education. We can assign the values 0, 1, 2, and 3 to High School, Bachelor's, Master's, and PhD, respectively.

For the categorical variable "Employment Status," we can use one-hot encoding. The categories do not have a natural order, and using ordinal encoding may imply a ranking or order that does not exist. With one-hot encoding, we create a new binary feature for each category, where the value is 1 if the observation belongs to that category and 0 otherwise. For example, we can create new features "Unemployed", "Part-Time", and "Full-Time", with values 1 or 0 depending on the employment status of each observation.

The choice of encoding method depends on the nature of the categorical variable and its categories. In general, label encoding is used for binary variables, ordinal encoding is used for ordered categorical variables, and one-hot encoding is used for unordered categorical variables. However, there may be exceptions and other encoding methods, such as target encoding or frequency encoding, that may be more appropriate in certain situations."""


# ANS7

# In[27]:


import pandas as pd

# create a sample dataset
data = {
    'Temperature': [25, 30, 20, 22, 28],
    'Humidity': [50, 60, 40, 45, 55],
    'Weather Condition': ['Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy'],
    'Wind Direction': ['North', 'South', 'East', 'West', 'North']
}

# create a pandas dataframe from the data
df = pd.DataFrame(data)

# calculate the covariance matrix
covariance_matrix = df.cov()

# print the covariance matrix
print(covariance_matrix)


# In[ ]:




