#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[2]:


"""Missing values in a dataset refer to the absence of data in one or more observations or variables. This can happen due to various reasons such as data entry errors, equipment failure, survey non-response, etc. Handling missing values is important as it can affect the quality of the data analysis and can lead to biased or incorrect results. Some reasons why it is essential to handle missing values are:

Missing values can reduce the representativeness of the sample and can cause biased estimates.

Missing values can affect the accuracy of the statistical analysis and can lead to incorrect conclusions.
Here are some algorithms that are not affected by missing values:

Decision trees: Decision trees can handle missing values by ignoring the missing attribute during the computation of the split.

Random Forest: Similar to decision trees, Random Forest can handle missing values by ignoring the missing attribute during the computation of the split.

K-Nearest Neighbors (KNN): KNN can handle missing values by using the mean or median value of the k nearest neighbors to impute the missing value.
"""


# ANS2

# In[4]:


""" Missing Values
Missing values occurs in dataset when some of the informations is not stored for a variable
There are 3 mechanisms

1 Missing Completely at Random, MCAR:
Missing completely at random (MCAR) is a type of missing data mechanism in which the probability of a value being missing is unrelated to both the observed data and the missing data. In other words, if the data is MCAR, the missing values are randomly distributed throughout the dataset, and there is no systematic reason for why they are missing.

For example, in a survey about the prevalence of a certain disease, the missing data might be MCAR if the survey participants with missing values for certain questions were selected randomly and their missing responses are not related to their disease status or any other variables measured in the survey.

 2. Missing at Random MAR:
Missing at Random (MAR) is a type of missing data mechanism in which the probability of a value being missing depends only on the observed data, but not on the missing data itself. In other words, if the data is MAR, the missing values are systematically related to the observed data, but not to the missing data.
Here are a few examples of missing at random:

Income data: Suppose you are collecting income data from a group of people, but some participants choose not to report their income. If the decision to report or not report income is related to the participant's age or gender, but not to their income level, then the data is missing at random.

Medical data: Suppose you are collecting medical data on patients, including their blood pressure, but some patients do not report their blood pressure. If the patients who do not report their blood pressure are more likely to be younger or have healthier lifestyles, but the missingness is not related to their actual blood pressure values, then the data is missing at random.

 3. Missing data not at random (MNAR) 
It is a type of missing data mechanism where the probability of missing values depends on the value of the missing data itself. In other words, if the data is MNAR, the missingness is not random and is dependent on unobserved or unmeasured factors that are associated with the missing values.


1.Example:- Deletion: In this technique, the rows or columns with missing values are deleted from the dataset. This is an easy but sometimes inefficient technique.



import pandas as pd


df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, None], 'C': [None, None, 10, 11]})


df_drop_rows = df.dropna(axis=0)
print("DataFrame after dropping rows with missing values:\n", df_drop_rows)


df_drop_cols = df.dropna(axis=1)
print("DataFrame after dropping columns with missing values:\n", df_drop_cols)

2.Imputation: In this technique, missing values are filled in using a value derived from the other data in the dataset. Some common imputation techniques are mean imputation, median imputation, mode imputation, and interpolation.
Example:


import pandas as pd
import numpy as np


df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, None], 'C': [None, None, 10, 11]})


df_mean = df.fillna(df.mean())
print("DataFrame after mean imputation:\n", df_mean)


df_median = df.fillna(df.median())
print("DataFrame after median imputation:\n", df_median)


df_mode = df.fillna(df.mode().iloc[0])
print("DataFrame after mode imputation:\n", df_mode)


df_interpolate = df.interpolate()
print("DataFrame after interpolation:\n", df_interpolate)

"""


# ANS3

# In[5]:


"""Imbalanced data refers to a situation in which the distribution of target classes in a dataset is not equal, i.e., one class has significantly fewer samples than the other(s). In such a case, the machine learning model may become biased towards the majority class, leading to poor performance on the minority class. This is because the model is trained to optimize a performance metric that does not take into account the class imbalance, and therefore, it may predict the majority class in most cases.

If imbalanced data is not handled, it can lead to several issues, such as:

Poor performance on the minority class: A model trained on imbalanced data may not be able to accurately classify the minority class, leading to poor performance on this class.

Overfitting: A model trained on imbalanced data may overfit to the majority class and fail to generalize well to new data.

Incorrect conclusions: If the minority class is of interest, an imbalanced dataset can lead to incorrect conclusions about the effectiveness of a model or treatment.

Biased evaluation: If an evaluation metric that does not account for the class imbalance is used, the performance of the model may be overestimated.

To handle imbalanced data, several techniques can be used, such as:

Resampling: Resampling involves either undersampling the majority class or oversampling the minority class to balance the class distribution in the dataset.

Cost-sensitive learning: Cost-sensitive learning involves assigning different misclassification costs to different classes to take into account the class imbalance."""


# ANS4

# In[8]:


""" Up-sampling and down-sampling are two techniques used in data resampling to handle imbalanced datasets.

Up-sampling involves increasing the number of samples in the minority class by replicating existing samples or generating synthetic samples. For example, if we have a dataset with 100 samples and only 10 belong to the minority class, we can up-sample the minority class by duplicating or generating new samples, so that we end up with a balanced dataset.

Down-sampling involves decreasing the number of samples in the majority class by randomly removing samples. 
For example, if we have a dataset with 100 samples and only 10 belong to the minority class, we can down-sample the majority class by randomly removing samples, so that we end up with a balanced dataset."""
import numpy as np
import pandas as pd

np.random.seed(123)

n_samples = 1000
class_0_ratio = 0.9
n_class_0 = int(n_samples*class_0_ratio)
n_class_1 = n_samples - n_class_0
n_class_0,n_class_0

class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})

df=pd.concat([class_0,class_1]).reset_index(drop=True)


# In[10]:


df['target'].value_counts()


# In[11]:


1.## upsampling 
df_minority=df[df['target']==1]
df_majority=df[df['target']==0]

from sklearn.utils import resample
df_minority_upsampled=resample(df_minority,replace=True, #Sample With replacement
         n_samples=len(df_majority),
         random_state=42
        )

df_minority_upsampled.shape

df_minority_upsampled.head()

df_upsampled=pd.concat([df_majority,df_minority_upsampled])

df_upsampled['target'].value_counts()


# In[13]:


2.##Downsampling
df_minority=df[df['target']==1]
df_majority=df[df['target']==0]

from sklearn.utils import resample
df_majority_upsampled=resample(df_minority,replace=True, #Sample With replacement
         n_samples=len(df_majority),
         random_state=42
        )


# ANS5

# In[18]:


"""  Data augmentation is a technique used in machine learning and deep learning to artificially increase the size of a dataset by creating modified copies of existing data. The objective is to increase the diversity and quantity of the training data, which can help improve the accuracy and robustness of a model.

There are several methods of data augmentation, including image flipping, rotation, scaling, and cropping. These techniques can be used to generate new samples that are similar to the original data, but with minor variations. For example, rotating an image by a small angle can create a new sample that is different from the original, but still belongs to the same class.


"""
get_ipython().system('pip install imbalanced-learn')

from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
from collections import Counter

# Generate an imbalanced dataset
X, y = make_classification(n_classes=2, class_sep=2,
                           weights=[0.1, 0.9], n_informative=3,
                           n_redundant=1, flip_y=0, n_features=20,
                           n_clusters_per_class=1, n_samples=1000,
                           random_state=10)


counter = Counter(y)
print('Before SMOTE:', counter)


smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)


counter = Counter(y_resampled)
print('After SMOTE:', counter)


# ANS6

# In[19]:


""" Outliers are observations or data points that are significantly different from other observations in a dataset. Outliers can occur due to various reasons such as measurement errors, data entry errors, or genuinely rare events.

Handling outliers is essential because they can have a significant impact on the statistical analysis of a dataset. Outliers can skew the mean, 
standard deviation, and other measures of central tendency and variability,
leading to incorrect conclusions or inferences about the underlying data distribution."""


# ANS7

# In[1]:


"""There are several techniques you can use to handle missing data in your analysis. Here are some common ones:

Listwise deletion: This involves removing any rows that have missing data. While this can be an easy solution, it can also lead to a loss of valuable data.

Imputation: This involves replacing missing values with estimates. There are several methods for imputation, including mean imputation (replacing missing values with the mean of the non-missing values), mode imputation (replacing missing values with the mode of the non-missing values), and regression imputation (using a regression model to predict missing values).

Multiple imputation: This involves creating multiple imputed datasets and analyzing each one separately. The results are then combined to provide a final analysis.

Using machine learning algorithms: Some machine learning algorithms can handle missing data directly. For example, decision trees and random forests can handle missing data by simply ignoring the missing values. """


# ANS8

# In[2]:


""" If you have a large dataset and find that only a small percentage of the data is missing, you can use several strategies to determine if the missing data is missing at random or if there is a pattern to the missing data. Here are some common strategies:

Check for missing data patterns: Look for patterns in the missing data. For example, if certain variables have a higher percentage of missing data than others, this may indicate that there is a pattern to the missing data.

Perform statistical tests: Perform statistical tests to see if the missing data is related to other variables in the dataset. For example, you could perform a chi-square test to determine if the missing data is related to a categorical variable.

Use imputation techniques: Use imputation techniques to fill in the missing data and then compare the results to the original dataset. If the results are similar, this may indicate that the missing data is missing at random.

Use machine learning algorithms: Use machine learning algorithms to predict the missing data and compare the predicted values to the actual values. If the predicted values are similar to the actual values, this may indicate that the missing data is missing at random."""


# ANS9

# In[4]:


"""  When working with an imbalanced dataset, where the majority of patients do not have the condition of interest, there are several strategies you can use to evaluate the performance of your machine learning model. Here are some common strategies:

Use appropriate evaluation metrics: Traditional evaluation metrics like accuracy may not be suitable for imbalanced datasets since they may give misleading results. Instead, consider using metrics such as precision, recall, F1 score, and area under the receiver operating characteristic curve (AUC-ROC) that take into account both true positives and false positives.

Resampling techniques: You can use resampling techniques such as oversampling, undersampling, or a combination of both to balance the dataset. Oversampling involves increasing the number of minority class samples, while undersampling involves decreasing the number of majority class samples. Resampling can help the model to learn from the minority class samples, which may improve the overall performance."""


# ANS10

# In[5]:


""" When dealing with an unbalanced dataset in which the majority of customers report being satisfied, there are several methods that you can use to balance the dataset and down-sample the majority class. Here are some common techniques:

Random under-sampling: In this method, you randomly select a subset of the majority class samples equal in size to the minority class samples. This approach can be fast and easy to implement, but it can also result in a loss of information if the sample size becomes too small.

Cluster-based under-sampling: This method groups similar majority class samples into clusters and then selects a representative sample from each cluster. This approach can preserve the information in the majority class and reduce the risk of losing important information.

Tomek links: This is a method that identifies samples that are close to each other but belong to different classes. By removing the majority class samples that form a Tomek link, you can remove noisy samples and potentially improve the performance of the model."""


# ANS11

# In[6]:


"""  When working with a dataset with a low percentage of occurrences of a rare event, there are several methods that you can use to balance the dataset and up-sample the minority class. Here are some common techniques:

Random over-sampling: In this method, you randomly duplicate minority class samples to increase their number. This approach can be fast and easy to implement, but it can also result in overfitting if the dataset becomes too large.

Synthetic minority over-sampling technique (SMOTE): This method generates synthetic samples for the minority class by creating new samples that are similar to existing minority class samples. This approach can increase the number of minority class samples and help the model to learn from them.

Adaptive synthetic (ADASYN): This is an extension of SMOTE that generates more synthetic samples for minority class samples that are harder to learn, which can improve the performance of the model.

Combination of over-sampling and under-sampling: You can also combine over-sampling of the minority class with under-sampling of the majority class. This can help to increase the number of minority class samples and reduce the number of majority class samples, resulting in a more balanced dataset."""


# In[ ]:




