#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


""" To solve this problem using Bayes' theorem, let's define the events:

A: An employee is a smoker.
B: An employee uses the health insurance plan.

We are given the following probabilities:

P(B) = 0.70 (70% of employees use the health insurance plan)
P(A|B) = 0.40 (40% of employees who use the health insurance plan are smokers)

We want to find the probability of an employee being a smoker given that they use the health insurance plan, P(A|B).

Using Bayes' theorem, the formula is:

P(A|B) = (P(B|A) * P(A)) / P(B)

P(B|A) is the probability of an employee using the health insurance plan given that they are a smoker. Unfortunately, we don't have this information explicitly given in the problem statement. Therefore, we cannot calculate P(A|B) using Bayes' theorem without knowing P(B|A)."""


# ANS2

# In[2]:


""" The difference between Bernoulli Naive Bayes and Multinomial Naive Bayes lies in the assumptions they make about the underlying data and the probability distributions they model.

Bernoulli Naive Bayes:
Bernoulli Naive Bayes is typically used for binary or boolean features, where each feature can take only two possible values, usually 0 and 1. It assumes that features are independent of each other given the class label. This algorithm calculates the probability of each feature being present (1) or absent (0) in each class and uses those probabilities to make predictions. It is commonly used in text classification tasks, where the presence or absence of specific words is used as features.

Multinomial Naive Bayes:
Multinomial Naive Bayes is suitable for features that represent discrete counts or frequencies. It assumes that features follow a multinomial distribution, which means they can take integer values and represent the count or frequency of an event. It also assumes that features are conditionally independent given the class label. Multinomial Naive Bayes is commonly used for document classification tasks, where features are often word frequencies or term frequencies-inverse document frequencies (TF-IDF)."""


# ANS3

# In[3]:


""" Bernoulli Naive Bayes handles missing values by considering them as a separate category or value. When a feature has a missing value, it is treated as a distinct category or level of that feature.

In Bernoulli Naive Bayes, each feature is represented as a binary variable, where it can take two possible values: 0 (absence) or 1 (presence). When a missing value is encountered for a feature, it is treated as a third category, separate from 0 and 1. This means that the missing value is considered as a valid value and contributes to the conditional probability calculations.

During the training phase, the algorithm estimates the probabilities of each feature value (0, 1, and missing) for each class label based on the training data. The presence of missing values in the training data leads to the calculation of probabilities for the missing category as well.

During the prediction phase, when encountering a missing value for a particular feature in a test instance, Bernoulli Naive Bayes incorporates the missing category in the probability calculations. It calculates the probabilities for each class label based on the available feature values (0, 1) as well as the missing category."""


# ANS4

# In[4]:


""" Yes, Gaussian Naive Bayes can be used for multi-class classification tasks. Gaussian Naive Bayes is a variant of Naive Bayes that assumes that the features follow a Gaussian or normal distribution. It is commonly used for continuous or numerical features.

In the case of multi-class classification, where there are more than two classes, Gaussian Naive Bayes can still be applied. The algorithm extends the basic Naive Bayes framework to handle multiple classes by estimating the class probabilities and the conditional probabilities of the features for each class.

During the training phase, Gaussian Naive Bayes estimates the mean and standard deviation of each feature for each class label. These estimates are used to model the class-conditional probabilities assuming a Gaussian distribution for each feature.

During the prediction phase, when given a new instance with feature values, Gaussian Naive Bayes calculates the probabilities of the instance belonging to each class using the class prior probabilities and the class-conditional probabilities derived from the Gaussian distribution."""


# In[ ]:




