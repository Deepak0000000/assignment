#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[2]:


"""Probability Mass Function (PMF) and Probability Density Function (PDF) are two important concepts in probability theory and statistics. They are used to describe the probability distribution of a random variable.

A Probability Mass Function (PMF) is a function that gives the probability that a discrete random variable is exactly equal to a particular value. It is typically denoted as P(X = x) where X is the random variable and x is a specific value. The PMF is defined for all possible values of X and satisfies the following properties:

Non-negative: P(X = x) ≥ 0 for all x.
Normalized: The sum of all possible values of P(X = x) is equal to 1.
An example of a discrete random variable is the outcome of a coin toss. The random variable X can take on two possible values: heads (H) or tails (T). The PMF for X is:

P(X=H) = 0.5
P(X=T) = 0.5

Here, the PMF tells us the probability of getting heads or tails when we flip a coin.

A Probability Density Function (PDF) is a function that describes the probability distribution of a continuous random variable. It is denoted as f(x) and satisfies the following properties:

Non-negative: f(x) ≥ 0 for all x.
Normalized: The integral of f(x) over all possible values of x is equal to 1.
An example of a continuous random variable is the height of people in a population. The random variable X can take on any value between 0 and infinity. The PDF for X is:

f(x) = 1/(σ√(2π)) * e^(-(x-μ)²/(2σ²))

Here, μ and σ are the mean and standard deviation of the population, respectively. The PDF tells us the relative likelihood of different heights occurring in the population."""


# ANS2

# In[3]:


"""  The Cumulative Density Function (CDF) is a function that gives the probability that a random variable X takes a value less than or equal to a given value x. It is denoted as F(x) and is defined for both continuous and discrete random variables.

For a discrete random variable X, the CDF is given by:

F(x) = P(X ≤ x)

For a continuous random variable X, the CDF is given by:

F(x) = ∫_-∞^x f(t) dt

where f(t) is the Probability Density Function (PDF) of X.

The CDF is an important concept in probability theory and statistics because it provides a way to describe the distribution of a random variable. The CDF satisfies the following properties:

Non-decreasing: F(x) is a non-decreasing function of x.
Bounded: 0 ≤ F(x) ≤ 1 for all x.
Right-continuous: F(x) is a right-continuous function of x, meaning that the limit of F(x) as x approaches a given value from the right is equal to F(x).
The CDF can be used to calculate probabilities for a range of values of the random variable X. For example, the probability that X lies between two values a and b is given by:

P(a < X ≤ b) = F(b) - F(a)

Additionally, the CDF can be used to calculate other important statistics such as the median and quartiles of a distribution.

An example of a CDF is the distribution of the sum of two dice rolls. The possible values of the sum range from 2 to 12, and each value has a different probability of occurring. The CDF for this distribution is:

F(x) = P(X ≤ x) =
0, for x < 2
1/36, for 2 ≤ x < 3
3/36, for 3 ≤ x < 4


Here, the CDF tells us the probability of getting a sum less than or equal to a given value x when we roll two dice. For example, the probability of getting a sum less than or equal to 7 is F(7) = 21/36."""


# ANS3

# In[4]:


""" The normal distribution, also known as the Gaussian distribution, is a probability distribution that is widely used as a model for many natural and social phenomena. Some examples of situations where the normal distribution might be used as a model include:

Heights of people: The heights of people in a population often follow a normal distribution. The mean and standard deviation of the distribution can be used to describe the average height and the amount of variability in heights, respectively.

Test scores: The scores on many standardized tests, such as the SAT and GRE, are often normally distributed. The mean and standard deviation of the distribution can be used to describe the average score and the spread of scores, respectively.

Errors in measurements: The errors in measurements of physical quantities, such as length and weight, often follow a normal distribution. The mean and standard deviation of the distribution can be used to describe the average error and the precision of the measurements, respectively.

Stock prices: The daily percentage changes in stock prices often follow a normal distribution. The mean and standard deviation of the distribution can be used to describe the average rate of return and the volatility of the stock, respectively."""


# ANS4

# In[5]:


""" The normal distribution, also known as the Gaussian distribution, is an important concept in probability theory and statistics because it is used to model many natural and social phenomena. 
The normal distribution is characterized by its bell-shaped curve and is symmetrical around its mean. The area under the curve represents the probability of observing a value within a certain range of the distribution.

The importance of the normal distribution lies in its versatility and applicability to many real-life situations. It is used extensively in scientific research, engineering, finance, and many other fields to describe and analyze data.

Here are some examples of real-life situations where the normal distribution is used:

Heights of people: The heights of people in a population often follow a normal distribution. This can be useful in fields such as clothing design and ergonomics.

IQ scores: IQ scores, which are used to measure intelligence, are often normally distributed. This can be useful in education and psychology research.

Body weight: Body weight in a population often follows a normal distribution. This can be useful in fields such as health and nutrition."""


# ANS5

# In[6]:


"""  The Bernoulli distribution is a probability distribution that models a single binary event that can have two outcomes, often labeled as success and failure. The distribution is named after the Swiss mathematician Jacob Bernoulli, who first studied it in the 17th century. The Bernoulli distribution is characterized by a single parameter p, which represents the probability of success.

An example of the Bernoulli distribution would be flipping a coin, where success could be defined as getting heads and failure as getting tails. If the coin is fair, then the probability of success is 0.5, and the Bernoulli distribution would be used to model the probability of getting heads on a single flip of the coin.

The main difference between the Bernoulli distribution and the binomial distribution is that the Bernoulli distribution models a single event with two possible outcomes, while the binomial distribution models the probability of a fixed number of successes in a fixed number of independent trials, where each trial has a Bernoulli distribution."""


# ANS6

# In[7]:


""" In this case, we want to find the probability that a randomly selected observation will be greater than 60. So we need to calculate the z-score for x = 60.

z = (60 - 50) / 10
z = 1

Now we need to find the probability that a standard normal variable is greater than z = 1. We can look this up in a standard normal distribution table or use a calculator.

Using a standard normal distribution table, we can find that the probability of a standard normal variable being greater than z = 1 is approximately 0.1587.

Therefore, the probability that a randomly selected observation from the given dataset will be greater than 60 is approximately 0.1587 or 15.87% (rounded to two decimal places)."""


# ANS7

# In[8]:


""" The uniform distribution is a probability distribution that assigns equal probability to all outcomes in a given range.
It is often used to model situations where all outcomes in a given interval are equally likely.

An example of the uniform distribution is rolling a fair six-sided die. In this case, 
each outcome (1, 2, 3, 4, 5, or 6) is equally likely, and the probability of each outcome is 1/6. The range of possible outcomes is from 1 to 6,
and each outcome has an equal probability of occurring."""


# ANS8

# In[9]:


"""The z-score, also known as the standard score, is a measure of how many standard deviations an observation or
data point is away 
from the mean of the distribution. It is used to standardize the data and make it easier to compare values
from different distributions.

The formula for calculating the z-score is:

z = (x - μ) / σ

where x is the value of the observation, μ is the mean of the distribution, 
and σ is the standard deviation of the distribution.

The z-score is important because it allows us to compare observations from different distributions on a common scale.
By standardizing the data, we can determine how extreme an observation is compared to the rest of the distribution, 
regardless of the units or scale of the original data."""


# ANS9

# In[10]:


""" The Central Limit Theorem (CLT) is a fundamental concept in statistics that states that the sum or average of a large number of independent and identically distributed (iid) random variables will follow a normal distribution, regardless of the underlying distribution of the individual variables.

In other words, the CLT asserts that the distribution of the sum or average of a large number of independent samples will be approximately normal, even if the individual samples are not normally distributed.

The significance of the CLT is that it provides a foundation for statistical inference, allowing us to make probabilistic statements about the sample mean or the difference between sample means based on a relatively small number of samples, without knowing the underlying distribution of the population."""


# ANS10

# In[11]:


""" The Central Limit Theorem (CLT) has certain assumptions that must be met in order for it to hold true. These assumptions are as follows:

Random Sampling: The data should be collected using a random sampling method. This means that each member of the population has an equal chance of being selected for the sample.

Independence: The sample should be composed of independent observations. In other words, the value of one observation should not be influenced by the value of any other observation.

Sample Size: The sample size should be sufficiently large. A common rule of thumb is that the sample size should be at least 30, but this may vary depending on the underlying distribution of the data."""


# In[ ]:




