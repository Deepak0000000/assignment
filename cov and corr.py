#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


"""To calculate the Pearson correlation coefficient between the amount of time students spend studying for an exam and their final exam scores, you would need to first calculate the covariance and the standard deviations of both variables. Once you have these values, you can use the following formula to calculate the Pearson correlation coefficient:

r = cov(X, Y) / (sd(X) * sd(Y))

where r is the Pearson correlation coefficient, cov(X, Y) is the covariance between X and Y, and sd(X) and sd(Y) are the standard deviations of X and Y, respectively."""


# ANS2

# In[2]:


import scipy.stats as stats

# Sample data
sleep = [8, 6, 7, 7, 5, 6, 8, 7, 9, 6]
job_satisfaction = [8, 7, 5, 6, 7, 8, 9, 6, 5, 7]

# Calculate Spearman's rank correlation coefficient
rs, p_value = stats.spearmanr(sleep, job_satisfaction)

# Print the result
print("Spearman's rank correlation coefficient: ", rs)


# ANS3

# In[3]:


import scipy.stats as stats
import numpy as np

# Sample data
exercise = [3, 5, 7, 2, 6, 4, 2, 5, 3, 4, 6, 5, 2, 3, 4, 5, 1, 3, 6, 5, 7, 2, 3, 5, 4, 5, 6, 2, 1, 5, 6, 4, 2, 3, 7, 5, 4, 6, 3, 5, 4, 2, 6, 3, 4, 5, 2, 1, 4, 6, 7]
bmi = [22.3, 28.6, 31.2, 23.1, 24.4, 27.7, 22.9, 23.8, 22.1, 26.6, 26.8, 23.7, 24.5, 25.1, 25.9, 26.2, 27.5, 24.2, 25.5, 28.1, 32.5, 21.9, 25.3, 28.8, 27.3, 27.6, 28.9, 23.8, 22.1, 28.2, 30.4, 23.9, 22.5, 24.7, 31.1, 26.9, 25.7, 31.8, 25.6, 26.7, 25.3, 24.1, 31.3, 23.5, 26.1, 25.5, 24.4, 23.4, 28.9, 27.6, 33.8]

# Calculate Pearson correlation coefficient
r, p_value = stats.pearsonr(exercise, bmi)

# Calculate Spearman's rank correlation coefficient
rs, p_value_spearman = stats.spearmanr(exercise, bmi)

# Print the results
print("Pearson correlation coefficient: ", r)
print("Spearman's rank correlation coefficient: ", rs)


# ANS4

# In[4]:


import numpy as np

# Enter the data for the number of hours individuals spend watching television per day and their level of physical activity
tv_hours = [4, 3, 5, 6, 2, 4, 3, 5, 1, 2, 3, 4, 5, 6, 2, 4, 3, 5, 6, 2, 4, 3, 5, 1, 2, 3, 4, 5, 6, 2, 4, 3, 5, 6, 2, 4, 3, 5, 1, 2, 3, 4, 5, 6, 2, 4, 3, 5, 6, 2]
physical_activity = [50, 60, 40, 30, 70, 50, 60, 40, 80, 70, 60, 50, 40, 30, 70, 50, 60, 40, 30, 70, 50, 60, 40, 80, 70, 60, 50, 40, 30, 70, 50, 60, 40, 30, 70, 50, 60, 40, 80, 70, 60, 50, 40, 30, 70, 50, 60, 40, 30, 70]

# Calculate the mean and standard deviation of both variables
tv_mean = np.mean(tv_hours)
tv_std = np.std(tv_hours)
activity_mean = np.mean(physical_activity)
activity_std = np.std(physical_activity)

# Calculate the covariance between the two variables
covariance = np.cov(tv_hours, physical_activity)[0][1]

# Calculate the Pearson correlation coefficient
pearson_correlation = covariance / (tv_std * activity_std)

print("The Pearson correlation coefficient between the number of hours individuals spend watching television per day and their level of physical activity is:", pearson_correlation)


# ANS5

# In[5]:


import numpy as np

# Enter the data for the number of sales calls made per day and the number of sales made per week
sales_calls = [30, 25, 40, 20, 35, 30, 45, 15, 25, 20, 30, 40, 35, 25, 20, 30, 45, 35, 25, 20, 30, 40, 15, 25, 30, 35, 20, 40, 25, 30]
sales_made = [10, 7, 12, 6, 11, 10, 13, 5, 7, 6, 9, 12, 10, 7, 6, 8, 13, 11, 7, 6, 9, 12, 5, 7, 10, 11, 6, 12, 7, 10]

# Calculate the mean and standard deviation of both variables
calls_mean = np.mean(sales_calls)
calls_std = np.std(sales_calls)
sales_mean = np.mean(sales_made)
sales_std = np.std(sales_made)

# Calculate the covariance between the two variables
covariance = np.cov(sales_calls, sales_made)[0][1]

# Calculate the Pearson correlation coefficient
pearson_correlation = covariance / (calls_std * sales_std)

print("The Pearson correlation coefficient between the number of sales calls made per day and the number of sales made per week is:", pearson_correlation)


# ANS6

# In[6]:


import numpy as np

# Enter the data for the number of sales calls made per day and the number of sales made per week
sales_calls = [30, 25, 40, 20, 35, 30, 45, 15, 25, 20, 30, 40, 35, 25, 20, 30, 45, 35, 25, 20, 30, 40, 15, 25, 30, 35, 20, 40, 25, 30]
sales_made = [10, 7, 12, 6, 11, 10, 13, 5, 7, 6, 9, 12, 10, 7, 6, 8, 13, 11, 7, 6, 9, 12, 5, 7, 10, 11, 6, 12, 7, 10]

# Calculate the mean and standard deviation of both variables
calls_mean = np.mean(sales_calls)
calls_std = np.std(sales_calls)
sales_mean = np.mean(sales_made)
sales_std = np.std(sales_made)

# Calculate the covariance between the two variables
covariance = np.cov(sales_calls, sales_made)[0][1]

# Calculate the Pearson correlation coefficient
pearson_correlation = covariance / (calls_std * sales_std)

print("The Pearson correlation coefficient between the number of sales calls made per day and the number of sales made per week is:", pearson_correlation)


# In[ ]:




