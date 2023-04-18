#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("har har mahadev")


# ANS1

# In[2]:


"""Simple linear regression is a statistical method that examines the relationship between a dependent variable and a single independent variable. It is a basic and commonly used type of regression analysis that seeks to model the relationship between two variables by fitting a linear equation to the data. For example, if we want to predict the sales of a product based on its price, we can use simple linear regression to estimate how much sales will change for each unit change in price.

Multiple linear regression, on the other hand, is a statistical method that examines the relationship between a dependent variable and two or more independent variables. It is an extension of simple linear regression that allows us to model more complex relationships between multiple variables. For example, if we want to predict the house price based on various factors such as the size of the house, number of bedrooms, and location, we can use multiple linear regression to estimate the effect of each factor on the house price.

Here are examples of both:

Example of Simple Linear Regression:
Suppose we want to predict the weight of a person based on their height. We collect data on the heights and weights of a sample of people and use simple linear regression to estimate the relationship between the two variables. The resulting regression equation might look like this:

Weight = 50 + 0.6 * Height

This equation tells us that for each additional centimeter of height, we can expect the weight of the person to increase by 0.6 kilograms.

Example of Multiple Linear Regression:
Suppose we want to predict the score of a student on an exam based on their study hours, attendance, and previous exam score. We collect data on these three variables and use multiple linear regression to estimate the relationship between them. The resulting regression equation might look like this:

Score = 40 + 3 * Study Hours + 5 * Attendance + 0.5 * Previous Exam Score"""


# ANS2

# In[3]:


"""Linear regression is a widely used statistical technique for modeling the relationship between a dependent variable and one or more independent variables. However, it is important to note that linear regression relies on certain assumptions that must hold for the results to be reliable and meaningful. Here are the main assumptions of linear regression:

Linearity: The relationship between the dependent variable and the independent variables should be linear. This means that the change in the dependent variable should be proportional to the change in the independent variables.

Independence: The observations in the dataset should be independent of each other. This means that the value of the dependent variable for one observation should not be influenced by the value of the dependent variable for another observation.

Homoscedasticity: The variance of the errors (or residuals) should be constant across all levels of the independent variables. This means that the errors should not be systematically larger or smaller for certain values of the independent variables.

Normality: The errors should be normally distributed. This means that the distribution of the errors should be symmetrical around zero.

"""


# ANS3

# In[4]:


""" In a linear regression model, the slope and intercept are the coefficients of the regression equation. The slope represents the change in the dependent variable for each one-unit increase in the independent variable, while the intercept represents the value of the dependent variable when the independent variable is zero.

The equation for a simple linear regression model is:

Y = b0 + b1*X

where Y is the dependent variable, X is the independent variable, b0 is the intercept, and b1 is the slope.

To interpret the slope and intercept, we can use a real-world scenario as an example. Suppose we want to predict the salary of an employee based on their years of experience. We collect data on the salaries and years of experience of a sample of employees and use linear regression to estimate the relationship between the two variables. The resulting regression equation might look like this:

Salary = 35,000 + 5,000*Years of Experience

This equation tells us that the intercept is 35,000, which means that an employee with zero years of experience would have a salary of 35,000. The slope is 5,000, which means that for each additional year of experience, we can expect the salary to increase by 5,000.

So, if an employee has three years of experience, we can use the regression equation to predict their salary:

Salary = 35,000 + 5,000*3 = 50,000"""


# ANS4

# In[5]:


""" Gradient descent is an optimization algorithm that is widely used in machine learning to minimize the error or loss function of a model. The basic idea behind gradient descent is to iteratively adjust the parameters of a model in the direction of the negative gradient of the loss function, until the parameters converge to a minimum.

The negative gradient of the loss function represents the direction of steepest descent, which is the direction that leads to the minimum value of the loss function. By iteratively adjusting the parameters of the model in this direction, we can gradually approach the minimum of the loss function.

The gradient descent algorithm works as follows:

Initialize the parameters of the model to some arbitrary values.

Compute the gradient of the loss function with respect to each parameter.

Update each parameter by subtracting a fraction of the gradient from its current value.

Repeat steps 2 and 3 until the parameters converge to a minimum.

The fraction that is subtracted from the gradient is called the learning rate. It determines the size of the steps that the algorithm takes in the direction of the negative gradient. If the learning rate is too small, the algorithm may converge slowly or get stuck in local minima. If the learning rate is too large, the algorithm may overshoot the minimum and diverge.

Gradient descent can be used to optimize many types of models, including linear regression, logistic regression, and neural networks. In machine learning, it is used to find the parameters that minimize the error or loss function of a model, so that the model can make accurate predictions on new data."""


# ANS5

# In[6]:


""" Multiple linear regression is a statistical model that describes the relationship between a dependent variable and two or more independent variables. In multiple linear regression, the dependent variable is assumed to be a linear function of the independent variables, with some added error or noise term.

The multiple linear regression model can be expressed as:

Y = b0 + b1X1 + b2X2 + ... + bn*Xn + ε

where Y is the dependent variable, X1, X2, ..., Xn are the independent variables, b0 is the intercept or constant term, and b1, b2, ..., bn are the coefficients or regression weights that represent the effect of each independent variable on the dependent variable. ε is the error or noise term, which represents the unexplained variability in the dependent variable.

Compared to simple linear regression, which only has one independent variable, multiple linear regression allows us to model the relationship between the dependent variable and multiple independent variables simultaneously. This can be useful in situations where the dependent variable is influenced by several factors or predictors, or where there are complex interactions between the predictors."""


# ANS6

# In[7]:


""" Multicollinearity in multiple linear regression refers to a situation where two or more independent variables are highly correlated with each other. This can cause problems in the regression analysis, such as unstable or inconsistent estimates of the regression coefficients, reduced precision of the estimates, and difficulty in interpreting the effects of the independent variables on the dependent variable.

There are several ways to detect multicollinearity in a multiple linear regression model:

Correlation matrix: One way to detect multicollinearity is to examine the correlation matrix of the independent variables. If two or more independent variables have a high correlation coefficient (e.g., above 0.8 or 0.9), this suggests that there may be multicollinearity.

Variance Inflation Factor (VIF): Another way to detect multicollinearity is to calculate the VIF for each independent variable. VIF measures how much the variance of the estimated regression coefficient is inflated due to the presence of other independent variables in the model. A high VIF (e.g., above 5 or 10) suggests that there may be multicollinearity."""


# ANS7

# In[8]:


""" Polynomial regression is a type of regression analysis where the relationship between the dependent variable and one or more independent variables is modeled as an nth degree polynomial function. Polynomial regression is used when the linear relationship between the dependent and independent variables is not sufficient to explain the variation in the dependent variable.

In polynomial regression, the model equation takes the form:

Y = β0 + β1X + β2X^2 + ... + βn*X^n + ε

where Y is the dependent variable, X is the independent variable, β0, β1, β2, ..., βn are the coefficients of the polynomial function, ε is the error term, and n is the degree of the polynomial function.

Compared to linear regression, which models the relationship between the dependent and independent variables as a straight line, polynomial regression models the relationship as a curved line that can better capture the nonlinear relationship between the variables. Polynomial regression can be used to model a wide range of functional forms, such as quadratic, cubic, or higher order functions."""


# ANS8

# In[9]:


"""Advantages of Polynomial Regression:

Can model complex, nonlinear relationships between the dependent and independent variables
Provides a better fit to data that have a curvilinear pattern
Allows for more accurate predictions than linear regression when the data is not linear
Disadvantages of Polynomial Regression:

Can be more prone to overfitting the model to the training data, leading to poor performance on new data
Can be more difficult to interpret than linear regression
Can require more data points and computational resources than linear regression, especially for higher degree polynomials"""


# In[ ]:




