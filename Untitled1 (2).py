#!/usr/bin/env python
# coding: utf-8

# In[20]:


print("har har mahadev")


# ANS1

# In[21]:


"""Ridge regression is a type of regularized linear regression method that adds a penalty term to the sum of squared coefficients in the cost function of the regression model. This penalty term, also known as L2 regularization, shrinks the coefficient estimates towards zero and can help prevent overfitting, particularly when there are many correlated predictor variables in the model.

In contrast, ordinary least squares (OLS) regression does not include any regularization term and simply minimizes the sum of squared residuals between the predicted values and the actual values of the target variable."""


# ANS2

# In[22]:


""" Ridge regression, like ordinary least squares regression, is based on a set of assumptions about the data. These assumptions include:

Linearity: The relationship between the independent variables and the dependent variable is assumed to be linear.

Independence: The observations are assumed to be independent of each other. This means that the value of one observation does not depend on the value of another observation.

Homoscedasticity: The variance of the errors is assumed to be constant across all levels of the independent variables. This means that the scatter of the residuals should be roughly the same across the range of the predictor variables.

Normality: The errors are assumed to be normally distributed. This means that the distribution of the residuals should be approximately symmetric and bell-shaped.

No multicollinearity: The predictor variables are assumed to be linearly independent of each other. This means that there should be no perfect correlation between any two predictor variables."""


# ANS3

# In[23]:


""" The tuning parameter lambda, also known as the regularization parameter, controls the amount of regularization applied in Ridge regression. A higher value of lambda corresponds to stronger regularization, which can shrink the coefficients more towards zero.

One common method for selecting the optimal value of lambda in Ridge regression is to use cross-validation. The data is randomly partitioned into several folds, and the model is trained on each fold while using the remaining folds for validation. This process is repeated multiple times, and the average validation error is computed for each value of lambda. The value of lambda that corresponds to the minimum validation error is selected as the optimal value.

Another method for selecting the optimal value of lambda is to use a grid search, which involves testing multiple values of lambda and selecting the one that results in the best performance according to a chosen metric, such as mean squared error (MSE) or coefficient of determination (R-squared)."""


# ANS4

# In[24]:


""" Ridge Regression can be used for feature selection, but it does not perform explicit feature selection like some other methods such as Lasso Regression.

In Ridge Regression, the L2 regularization penalty term shrinks the coefficients towards zero, but it does not set them exactly to zero. This means that all features are retained in the model, but some features may have smaller coefficients compared to others, indicating that they have less impact on the target variable.

However, the magnitude of the coefficients can be used as a proxy for feature importance. Features with larger coefficients are more important, while features with smaller coefficients are less important. Therefore, Ridge Regression can indirectly perform feature selection by reducing the impact of less important features on the target variable."""


# ANS5

# In[25]:


"""Ridge Regression is a useful tool for handling multicollinearity in linear regression. Multicollinearity occurs when two or more predictor variables in a regression model are highly correlated with each other. This can result in unstable and unreliable coefficient estimates, as well as decreased predictive performance of the model.

Ridge Regression can help mitigate the negative effects of multicollinearity by introducing a penalty term to the regression model that shrinks the coefficient estimates towards zero. This penalty term has the effect of reducing the impact of highly correlated predictors, making the model more stable and less sensitive to small changes in the data.

In particular, Ridge Regression can help to prevent overfitting in the presence of multicollinearity. Overfitting occurs when the model fits the training data too closely, resulting in poor generalization to new data. By shrinking the coefficient estimates towards zero, Ridge Regression can reduce the complexity of the model and help prevent overfitting. """


# ANS6

# In[26]:


""" Yes, Ridge Regression can handle both categorical and continuous independent variables, as long as the categorical variables are properly encoded.

In regression analysis, categorical variables need to be converted into numerical variables before they can be included in a regression model. This is typically done using one of several encoding methods, such as dummy encoding, effect coding, or contrast coding. These methods convert categorical variables into one or more numerical variables that can be used as independent variables in the regression model.

Once the categorical variables are properly encoded, they can be included in a Ridge Regression model alongside continuous variables. The Ridge Regression model will then use both types of variables to make predictions about the target variable."""


# ANS7

# In[27]:


""" In Ridge Regression, the coefficients can be interpreted in a similar way to those in ordinary least squares regression, but with some important differences due to the presence of the L2 regularization penalty.

The coefficients in Ridge Regression represent the change in the target variable (dependent variable) associated with a one-unit change in the corresponding independent variable, holding all other independent variables constant. However, in Ridge Regression, the coefficients are not only influenced by the relationship between the independent and dependent variables, but also by the strength of the regularization penalty, which is controlled by the tuning parameter λ.

The larger the value of λ, the greater the amount of shrinkage applied to the coefficients, resulting in smaller coefficients. Therefore, the interpretation of the coefficients in Ridge Regression should take into account the magnitude of λ, in addition to their sign and size."""


# ANS8

# In[ ]:


""" """

