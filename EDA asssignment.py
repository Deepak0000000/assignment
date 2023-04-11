#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[2]:


"""
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine.  Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are many more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.


Attribute Information:

Input variables (based on physicochemical tests):
- 1 - fixed acidity
- 2 - volatile acidity
- 3 - citric acid
- 4 - residual sugar
- 5 - chlorides
- 6 - free sulfur dioxide
- 7 - total sulfur dioxide
- 8 - density
- 9 - pH
- 10 - sulphates
- 11 - alcohol

Output variable (based on sensory data):
- 12 - quality (score between 0 and 10)"""


# ANS2

# In[3]:


"""Missing data is a common issue in datasets and can affect the accuracy of machine learning models. Imputation techniques are used to fill in the missing values with estimates based on the available data. The following are some common imputation techniques:

Mean imputation: This technique involves replacing missing values with the mean of the available data. It is a simple and quick technique but can result in biased estimates, especially when the missing values are not missing at random.

Median imputation: This technique involves replacing missing values with the median of the available data. It is also a simple and quick technique but can be less sensitive to outliers than mean imputation.

Mode imputation: This technique involves replacing missing values with the mode of the available data. It is suitable for categorical variables but can result in biased estimates if the mode is not representative of the underlying distribution.

K-nearest neighbor imputation: This technique involves finding the k nearest neighbors of each missing value and using their values to impute the missing value. It can produce more accurate estimates than mean or median imputation, especially when the missing values are not missing at random. However, it can be computationally expensive, and the choice of k can affect the accuracy of the estimates.

Multiple imputation: This technique involves generating multiple imputed datasets and averaging the results. It can produce more accurate estimates than single imputation methods but can be computationally expensive.

Advantages and disadvantages of different imputation techniques:

Mean imputation: Advantages - Simple and quick, does not require complex modeling. Disadvantages - Can result in biased estimates, especially when missing values are not missing at random.

Median imputation: Advantages - Simple and quick, less sensitive to outliers than mean imputation. Disadvantages - Can result in biased estimates if the distribution is not symmetric.

Mode imputation: Advantages - Suitable for categorical variables. Disadvantages - Can result in biased estimates if the mode is not representative of the underlying distribution.

K-nearest neighbor imputation: Advantages - Can produce more accurate estimates than mean or median imputation, especially when the missing values are not missing at random. Disadvantages - Can be computationally expensive, and the choice of k can affect the accuracy of the estimates.

Multiple imputation: Advantages - Can produce more accurate estimates than single imputation methods. Disadvantages - Can be computationally expensive, and the number of imputed datasets can affect the accuracy of the estimates."""


# ANS3

# In[6]:


"""## Explore More Visualization
fig,axis=plt.subplots(1,2,figsize=(15,7))
plt.subplot(121)
sns.histplot(data=df,x='average',bins=30,kde=True,color='g')
plt.subplot(122)
sns.histplot(data=df,x='average',bins=30,kde=True,hue='gender')
plt.show()
  
    

1.We can ovserve that in this dataset by visualizing  here  the female candidate perform well as compard to the male candidate 


plt.subplot(1,3,figsize=(25,6))
plt.subplot(141)
sns.histplot(data=df,x='average',kde=True,hue='lunch')
plt.subplot(142)
sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='lunch')
plt.subplot(143)
sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='lunch')
plt.show()

1. according to this data set the satandard lunch helps the student perform well in exams be it male or female




plt.subplots(1,3,figsize=(25,6))
plt.subplot(141)
ax =sns.histplot(data=df,x='average',kde=True,hue='parental_level_of_education')
plt.subplot(142)
ax =sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='parental_level_of_education')
plt.subplot(143)
ax =sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='parental_level_of_education')
plt.show()


In general parent's education don't help student perform well in exam.
- 2nd plot shows that parent's whose education is of associate's degree or master's degree their male child tend to perform well in exam
- 3rd plot we can see there is no effect of parent's education on female students.


plt.subplots(1,3,figsize=(25,6))
plt.subplot(141)
ax =sns.histplot(data=df,x='average',kde=True,hue='race_ethnicity')
plt.subplot(142)
ax =sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='race_ethnicity')
plt.subplot(143)
ax =sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='race_ethnicity')
plt.show()



Students of group A and group B tends to perform poorly in exam.
- Students of group A and group B tends to perform poorly in exam irrespective of whether they are male or female

"""


# ANS4
# 

# In[7]:


"""Feature engineering is the process of selecting and transforming variables to improve the performance of a machine learning model. It involves the following steps:

Data cleaning and preparation: This step involves cleaning the dataset, handling missing values, and converting categorical variables into numerical ones. The dataset may also be split into training and testing sets.

Feature selection: This step involves selecting the most relevant variables for the model. This can be done using statistical tests, domain knowledge, or feature importance rankings.

Feature scaling: This step involves scaling the variables to ensure that they are on the same scale. This can be done using standardization or normalization techniques.

Feature engineering: This step involves transforming the variables to create new features that may be more informative for the model. This can be done using techniques such as polynomial features, feature interactions, or dimensionality reduction."""


# ANS5

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the wine quality dataset
df = pd.read_csv('winequality-red.csv')

# Plot the distributions of each feature
sns.displot(df, x="fixed acidity", kde=True)
plt.show()

sns.displot(df, x="volatile acidity", kde=True)
plt.show()

sns.displot(df, x="citric acid", kde=True)
plt.show()

sns.displot(df, x="residual sugar", kde=True)
plt.show()

sns.displot(df, x="chlorides", kde=True)
plt.show()

sns.displot(df, x="free sulfur dioxide", kde=True)
plt.show()

sns.displot(df, x="total sulfur dioxide", kde=True)
plt.show()

sns.displot(df, x="density", kde=True)
plt.show()

sns.displot(df, x="pH", kde=True)
plt.show()

sns.displot(df, x="sulphates", kde=True)
plt.show()

sns.displot(df, x="alcohol", kde=True)
plt.show()


# ANS6

# In[12]:


from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

# Load the wine quality dataset
df = pd.read_csv('winequality-red.csv')

# Split the dataset into features and labels
X = df.drop('quality', axis=1)
y = df['quality']

# Apply PCA
pca = PCA(n_components=len(X.columns))
pca.fit(X)

# Determine the minimum number of principal components required to explain 90% of the variance
explained_variances = pca.explained_variance_ratio_
cumulative_variances = np.cumsum(explained_variances)
n_components = np.argmax(cumulative_variances >= 0.9) + 1

print("Minimum number of principal components required to explain 90% of variance:", n_components)


# In[ ]:





# In[ ]:




