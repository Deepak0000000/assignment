#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


""" Min-Max scaling, also known as normalization, is a technique used in data preprocessing to rescale numeric data to have a

Example:Suppose we have a dataset of the height (in inches) of five people:

specific range of values between 0 and 1. This is achieved by subtracting the minimum value from each data point and then dividing by the range, which is the difference between the maximum and minimum values in the dataset.
X_scaled = (X - X_min) / (X_max - X_min)


Example:Suppose we have a dataset of the height (in inches) of five people:
65, 68, 72, 56, 75

The minimum value in the dataset is 56, and the maximum value is 75. To scale this data using Min-Max scaling, we subtract 56 from each value and divide by the range (which is 75-56 = 19):

65 -> (65-56)/19 = 0.474
68 -> (68-56)/19 = 0.632
72 -> (72-56)/19 = 0.842
56 -> (56-56)/19 = 0
75 -> (75-56)/19 = 1


0.474, 0.632, 0.842, 0, 1


"""


# ANS2

# In[3]:


"""  The unit vector technique, also known as "Normalization," is a feature scaling method used to transform numeric data into a range of 0 to 1. This method scales each feature individually by dividing each value in the feature by the magnitude of the feature vector.

The formula for normalizing a feature vector is:

X_norm = X / ||X||

Suppose we have a dataset with two features, age and income, and we want to normalize the data using the unit vector technique. The original values for age and income are:


age = [25, 35, 42, 28, 31]
income = [50000, 65000, 80000, 45000, 70000]
To normalize the data using the unit vector technique, we first calculate the magnitude of the feature vector for each feature:


||age|| = sqrt(25^2 + 35^2 + 42^2 + 28^2 + 31^2) = 78.42
||income|| = sqrt(50000^2 + 65000^2 + 80000^2 + 45000^2 + 70000^2) = 174352.63
Then, we divide each value in the feature by its magnitude:


age_norm = [25/78.42, 35/78.42, 42/78.42, 28/78.42, 31/78.42] = [0.318, 0.446, 0.536, 0.357, 0.395]
income_norm = [50000/174352.63, 65000/174352.63, 80000/174352.63, 45000/174352.63,
"""


# ANS3

# In[5]:


"""PCA, or Principal Component Analysis, is a statistical technique used to reduce the dimensionality of a dataset by identifying the most important features, or principal components, that capture the majority of the variability in the data.

PCA works by transforming the original dataset into a new coordinate system that is aligned with the principal components. The first principal component represents the direction of maximum variance in the data,
while the second principal component represents the direction of maximum variance orthogonal to the first principal component, and so on.
The number of principal components is equal to the number of original features in the dataset, but typically only the first few principal 
components are retained to capture most of the variability in the data.


Example:

height = [170, 180, 165, 175, 190]
weight = [60, 80, 55, 70, 85]
shoe_size = [10, 11, 9, 10.5, 12]
age = [25, 30, 22, 27, 35]

standardized_height = [-0.49, 0.49, -1.22, 0.0, 1.22]
standardized_weight = [-1.22, 0.49, -1.65, -0.24, 1.62]
standardized_shoe_size = [-0.24, 0.72, -1.21, 0.24, 1.49]
standardized_age = [-0.46, 0.23, -1.15, -0.23, 1.62]


PC1 = 0.47*standardized_height + 0.49*standardized_weight + 0.42*standardized_shoe_size + 0.59*standardized_age
PC2 = -0.61*standardized_height + 0.45*standardized_weight - 0.42*standardized_shoe_size + 0.5*standardized_age


transformed_data = [[-1.46, 0.41],
                    [0.68, -0.18],
                    [-2.13, -0.02],
                    [-0.34, -0.15],
                    [3.25, -0.06]]

"""


# ANS4

# In[6]:


""" PCA can be used as a feature extraction technique to identify the most important features in a dataset by transforming the data into a new coordinate system aligned with the principal components. In this context, PCA is a way to reduce the dimensionality of a dataset by identifying a lower-dimensional subspace that captures the majority of the variability in the data.

PCA can be used for feature extraction in various applications, such as image processing, natural language processing, and computer vision. In these applications, PCA can be used to extract features from high-dimensional data, such as images or text, and reduce the complexity of the data representation."""


# ANS5

# In[7]:


""" Min-Max scaling is a common preprocessing technique used to transform numerical features to a common scale, typically between 0 and 1. This technique can be applied to the features of a food delivery service dataset, such as price, rating, and delivery time, to ensure that they are on the same scale and have equal weight when building a recommendation system.

To use Min-Max scaling to preprocess the data, we need to follow the following steps:

Identify the numerical features that need to be scaled, such as price, rating, and delivery time.

Compute the minimum and maximum values of each feature in the dataset.

Scale each feature to a common range between 0 and 1 using the following formula:

x_scaled = (x - x_min) / (x_max - x_min)

where x is the original feature value, x_min and x_max are the minimum and maximum values of the feature, respectively, and x_scaled is the scaled feature value.
"""


# ANS6

# In[8]:


"""When working with a large dataset containing many features, it can be challenging to build an accurate predictive model due to the "curse of dimensionality." PCA can be used to address this issue by reducing the dimensionality of the dataset while still preserving the most important information.

Here are the steps to use PCA to reduce the dimensionality of the stock price prediction dataset:

First, we need to normalize the features of the dataset so that they are all on the same scale. We can use standardization, where we subtract the mean of each feature and divide by its standard deviation.

Next, we apply PCA to the normalized dataset. This involves finding the principal components that capture the most significant amount of variation in the dataset. The number of principal components we choose to retain depends on the amount of variance we want to preserve. We can use the scree plot or the explained variance ratio to determine the number of components.

After obtaining the principal components, we can project the data onto a lower-dimensional subspace defined by the principal components. This reduces the dimensionality of the dataset while preserving the most important information.

Finally, we can use the reduced dataset to train a predictive model, such as a regression model, to predict stock prices."""


# ANS7

# In[9]:


""" When working with a large dataset containing many features, it can be challenging to build an accurate predictive model due to the "curse of dimensionality." PCA can be used to address this issue by reducing the dimensionality of the dataset while still preserving the most important information.

Here are the steps to use PCA to reduce the dimensionality of the stock price prediction dataset:

First, we need to normalize the features of the dataset so that they are all on the same scale. We can use standardization, where we subtract the mean of each feature and divide by its standard deviation.

Next, we apply PCA to the normalized dataset. This involves finding the principal components that capture the most significant amount of variation in the dataset. The number of principal components we choose to retain depends on the amount of variance we want to preserve. We can use the scree plot or the explained variance ratio to determine the number of components.

After obtaining the principal components, we can project the data onto a lower-dimensional subspace defined by the principal components. This reduces the dimensionality of the dataset while preserving the most important information.

Finally, we can use the reduced dataset to train a predictive model, such as a regression model, to predict stock prices.

"""


# ANS8

# In[10]:


""" To perform Min-Max scaling to transform the values of the dataset [1, 5, 10, 15, 20] to a range of -1 to 1, we can use the following formula:


x_scaled = (x - min(x)) / (max(x) - min(x)) * 2 - 1
where x is each value in the dataset.

First, we need to find the minimum and maximum values of the dataset:

min_val = min([1, 5, 10, 15, 20]) = 1
max_val = max([1, 5, 10, 15, 20]) = 20
Then, we can apply the Min-Max scaling formula to each value in the dataset:

x_scaled = (x - min_val) / (max_val - min_val) * 2 - 1

For x = 1, x_scaled = (1 - 1) / (20 - 1) * 2 - 1 = -1
For x = 5, x_scaled = (5 - 1) / (20 - 1) * 2 - 1 = -0.2
For x = 10, x_scaled = (10 - 1) / (20 - 1) * 2 - 1 = 0.2
For x = 15, x_scaled = (15 - 1) / (20 - 1) * 2 - 1 = 0.6
For x = 20, x_scaled = (20 - 1) / (20 - 1) * 2 - 1 = 1
Therefore, the Min-Max scaled values of the dataset [1, 5, 10, 15, 20] in the range of -1 to 1 are:


[-1, -0.2, 0.2, 0.6, 1]"""


# ANS9

# In[ ]:


""""""

