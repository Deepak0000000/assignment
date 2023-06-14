#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


""" Gradient Boosting Regression, also known as Gradient Boosted Regression Trees (GBRT), is a machine learning technique used for regression problems. It is an ensemble method that combines multiple weak prediction models, typically decision trees, to create a more powerful and accurate predictor.

The basic idea behind gradient boosting regression is to iteratively build an ensemble of weak regression models in a stage-wise manner. Each weak model is trained to correct the mistakes made by the previous models in the ensemble. The process starts with an initial weak model, and in each subsequent iteration, a new weak model is added to the ensemble to minimize the residual errors.

The gradient boosting algorithm optimizes a differentiable loss function by minimizing the residuals using gradient descent. In each iteration, the algorithm calculates the negative gradient of the loss function with respect to the current ensemble's predictions. The new weak model is then fitted to the negative gradient values, which represents the direction in which the ensemble's predictions should be updated to reduce the error.

The weak models, typically decision trees, are added to the ensemble in a greedy manner. Each tree is trained to predict the negative gradient values, and its predictions are combined with the predictions of the previous trees. The learning rate, which determines the contribution of each weak model to the ensemble, is used to control the step size in each iteration. Lower learning rates yield more accurate models but require more iterations to converge."""


# ANS2

# In[2]:


import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

class GradientBoostingRegressor:
    def __init__(self, n_estimators=100, learning_rate=0.1):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models = []

    def fit(self, X, y):
        # Initialize the target variable with the mean value
        y_pred = np.full_like(y, np.mean(y))

        for _ in range(self.n_estimators):
            # Calculate the negative gradient (residuals)
            residuals = y - y_pred

            # Train a weak model (in this case, a decision stump)
            stump = DecisionStump()
            stump.fit(X, residuals)

            # Update the predictions by adding the weighted stump predictions
            update = self.learning_rate * stump.predict(X)
            y_pred += update

            # Store the trained model
            self.models.append(stump)

    def predict(self, X):
        y_pred = np.zeros(len(X))

        for model in self.models:
            y_pred += self.learning_rate * model.predict(X)

        return y_pred

class DecisionStump:
    def __init__(self):
        self.feature_index = None
        self.threshold = None
        self.prediction = None

    def fit(self, X, y):
        num_samples, num_features = X.shape
        best_mse = np.inf

        for feature_index in range(num_features):
            thresholds = np.unique(X[:, feature_index])

            for threshold in thresholds:
                # Calculate predictions based on the threshold
                preds = np.where(X[:, feature_index] < threshold, np.mean(y[X[:, feature_index] < threshold]), np.mean(y[X[:, feature_index] >= threshold]))

                # Calculate mean squared error (MSE)
                mse = mean_squared_error(y, preds)

                # Update the best split if necessary
                if mse < best_mse:
                    best_mse = mse
                    self.feature_index = feature_index
                    self.threshold = threshold
                    self.prediction = preds

    def predict(self, X):
        return np.where(X[:, self.feature_index] < self.threshold, np.mean(self.prediction), np.mean(self.prediction))

# Generate a small regression dataset
np.random.seed(42)
X = np.random.rand(100, 1)
y = 2 * X[:, 0] + np.random.randn(100)

# Split the dataset into train and test sets
X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]

# Train the gradient boosting regression model
gb_regressor = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
gb_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gb_regressor.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation results
print("Mean Squared Error (MSE):", mse)
print("R-squared:", r2)


# ANS3

# In[4]:


"""from sklearn.model_selection import GridSearchCV

# Generate a small regression dataset
np.random.seed(42)
X = np.random.rand(100, 2)
y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(100)

# Split the dataset into train and test sets
X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]

# Define the parameter grid for grid search
param_grid = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.1, 0.01, 0.001],
    'max_depth': [2, 3, 4]
}

# Create the gradient boosting regressor
gb_regressor = GradientBoostingRegressor()

# Perform grid search
grid_search = GridSearchCV(gb_regressor, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_

# Train the model with the best hyperparameters
best_gb_regressor = GradientBoostingRegressor(**best_params)
best_gb_regressor.fit(X_train, y_train)

# Make predictions on the test set with the best model
y_pred = best_gb_regressor.predict(X_test)

# Calculate evaluation metrics for the best model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the best hyperparameters and evaluation results
print("Best Hyperparameters:", best_params)
print("Mean Squared Error (MSE):", mse)
print("R-squared:", r2)
"""


# ANS4

# In[5]:


""" In the context of gradient boosting, a weak learner refers to a simple, relatively low-complexity model that is used as a base model in the ensemble. It is also commonly known as a base or individual model. Weak learners are typically simpler than the final boosted model and have limited predictive power on their own.

In gradient boosting, the weak learner is often a decision tree, specifically a shallow or "stump" tree. A decision stump is a decision tree with only a single split, meaning it has a maximum depth of one. It makes predictions based on a single feature and a threshold value.

The use of weak learners in gradient boosting is a key aspect of the algorithm. Instead of trying to fit a single strong model to the data, gradient boosting iteratively builds an ensemble of weak learners, with each weak learner focusing on learning and correcting the mistakes of the previous learners. By combining multiple weak models, the ensemble can collectively produce a more accurate and robust prediction.

The key idea behind gradient boosting is that by iteratively adding weak learners and adjusting their weights, the ensemble can gradually improve its predictive performance. The algorithm places more emphasis on the samples that are difficult to predict correctly, enabling subsequent weak learners to focus on these challenging instances. This iterative process of building and combining weak learners gradually reduces the overall error of the ensemble.

The weak learners in gradient boosting are typically trained in a greedy manner, sequentially one after another, based on the negative gradients of the loss function. The loss function measures the difference between the predicted values and the true values of the target variable. The weak learners are trained to minimize this loss."""


# ANS5

# In[6]:


""" The intuition behind the Gradient Boosting algorithm stems from the idea of building a strong predictive model by iteratively improving upon the mistakes made by previous models in the ensemble. The algorithm combines weak learners, typically decision trees, to create a powerful and accurate predictor.

Here is a step-by-step intuition of how the Gradient Boosting algorithm works:

Initialization: The algorithm starts by initializing the target variable's predictions with a simple model, often the mean value of the target variable. This serves as the starting point for subsequent iterations.

Fitting weak learners: In each iteration, a weak learner, such as a decision tree, is trained to predict the errors (residuals) made by the previous models. The weak learner focuses on capturing the patterns in the residuals that were not captured by the previous models.

Weighted combination: The predictions of the weak learner are combined with the previous predictions, weighted by a learning rate. The learning rate determines how much influence each weak learner has on the final prediction. Lower learning rates lead to slower learning but can improve generalization.

Updating predictions: The updated predictions are used as the new target variable for the next iteration. The process of fitting weak learners, combining predictions, and updating the target variable is repeated for a specified number of iterations or until a convergence criterion is met.

Ensemble prediction: The final prediction is obtained by summing the predictions from all the weak learners, each weighted by its learning rate. The resulting prediction is a combination of the predictions made by each weak learner, with the aim of reducing the overall error and improving accuracy."""


# ANS6

# In[7]:


""" The Gradient Boosting algorithm builds an ensemble of weak learners by iteratively adding them to the ensemble, with each new learner focusing on correcting the mistakes made by the previous learners. Here's a step-by-step explanation of how the ensemble is built:

Initialization: The algorithm starts by initializing the target variable's predictions with a simple model, often the mean value of the target variable. This serves as the starting point for subsequent iterations.

Compute residuals: The difference between the predicted values and the true values of the target variable is computed. These differences, called residuals or errors, represent the amount of information left unexplained by the current ensemble.

Train a weak learner: A weak learner, typically a decision tree, is trained to predict the residuals. The weak learner is trained to find patterns or relationships in the data that can help reduce the residuals and improve predictions.

Update ensemble predictions: The predictions from the weak learner are added to the predictions made by the previous learners, with each prediction weighted by a learning rate. The learning rate determines the contribution of each weak learner to the final prediction. Typically, a lower learning rate is used to prevent overfitting and improve generalization.

Update residuals: The residuals are updated by subtracting the predictions made by the current weak learner from the previous residuals. The updated residuals represent the remaining errors that need to be addressed by the next weak learner.

Repeat steps 3-5: Steps 3 to 5 are repeated for a specified number of iterations or until a convergence criterion is met. In each iteration, a new weak learner is trained to predict the updated residuals, and its predictions are added to the ensemble.

Final ensemble prediction: The final prediction is obtained by summing the predictions from all the weak learners in the ensemble, each weighted by its learning rate. The resulting prediction is a combination of the predictions made by each weak learner, with the aim of reducing the overall error and improving accuracy."""


# ANS7

# In[8]:


""" Constructing the mathematical intuition of the Gradient Boosting algorithm involves understanding the underlying principles and mathematical concepts that drive its iterative optimization process. Here are the key steps involved in constructing the mathematical intuition of the Gradient Boosting algorithm:

Loss function selection: Select an appropriate loss function that measures the discrepancy between the predicted values and the true values of the target variable. Common choices include mean squared error (MSE) for regression problems and log loss (binary cross-entropy) for classification problems.

Initialization of the ensemble: Initialize the target variable's predictions with a simple model, often the mean value of the target variable for regression or the log-odds for binary classification. This serves as the starting point for subsequent iterations.

Gradient descent optimization: Use gradient descent optimization to iteratively minimize the loss function. The negative gradient of the loss function with respect to the predictions is calculated, representing the direction of steepest descent. This negative gradient is also known as the "pseudo-residuals" or "negative gradients."

Train a weak learner: Train a weak learner, typically a decision tree, to predict the negative gradients (pseudo-residuals). The weak learner is fitted to the negative gradients as the target variable and the original input features as predictors.

Update ensemble predictions: Update the predictions made by the ensemble by adding the predictions from the weak learner, weighted by a learning rate. The learning rate determines the contribution of each weak learner to the final prediction. Lower learning rates place less emphasis on the predictions of each individual weak learner, reducing overfitting and improving generalization.

Update residuals: Calculate the updated residuals by subtracting the predictions made by the current weak learner from the previous residuals. The updated residuals represent the remaining errors that need to be addressed by the next weak learner.

Repeat steps 3-6: Iterate steps 3 to 6 for a specified number of iterations or until a convergence criterion is met. In each iteration, a new weak learner is trained to predict the updated residuals, and its predictions are added to the ensemble.

Final ensemble prediction: Obtain the final prediction by summing the predictions from all the weak learners in the ensemble, each weighted by its learning rate. The resulting prediction is a combination of the predictions made by each weak learner, aiming to reduce the overall error and improve accuracy."""


# In[ ]:




