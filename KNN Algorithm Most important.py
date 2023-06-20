#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[3]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# In[4]:


iris = load_iris()


# In[7]:


iris


# In[8]:


## Split the dataset into features and lavels
X = iris.data
y=iris.target


# In[10]:


## Split the data in to trainnnig and testing split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# In[11]:


X_train


# In[12]:


X_test


# In[16]:


## create the object of KNN
knn = KNeighborsClassifier(n_neighbors=3)


# In[17]:


knn


# In[18]:


## Train the KNN classifier
knn.fit(X_train,y_train)


# In[19]:


## predict the lavels for the test set
y_pred = knn.predict(X_test)


# In[21]:


## calculate the accuracy of the classifier
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy)


# ANS2

# In[26]:


from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error


# In[27]:


boston  = load_boston()


# In[28]:


boston


# In[30]:


X = boston.data
y = boston.target


# In[31]:


X


# In[32]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# In[33]:


X_train


# In[34]:


knn = KNeighborsRegressor(n_neighbors=3)


# In[35]:


knn.fit(X_train,y_train)


# In[36]:


y_pred = knn.predict(X_test)


# In[38]:


mse = mean_squared_error(y_test,y_pred)
print("Mean Squared Error:",mse)


# In[ ]:





# ANS3

# In[42]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier


# In[43]:


iris = load_iris()


# In[44]:


X  = iris.data
y = iris.target


# In[45]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# In[52]:


k_values = [3,5,7,9,11]

for k in k_values:
    knn  = KNeighborsClassifier(n_neighbors=k)
    
    scores = cross_val_score(knn, X_train, y_train, cv=5)
    avg_score = scores.mean()
    
    # Print the results
    print("K =", k, "Average Score =", avg_score)


# ANS4

# In[56]:


from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor


# In[57]:


boston = load_boston()


# In[60]:


boston


# In[61]:


X = boston.data
y = boston.target


# In[62]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=42)


# In[63]:


## Perform feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[67]:


# Create a KNN regressor object
knn = KNeighborsRegressor(n_neighbors=3)

# Train the KNN regressor
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

mse = mean_squared_error(y_test,y_pred)
print("mEan Squared Error:",mse)


# ANS5

# In[68]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the Iris dataset
iris = load_iris()

# Split the dataset into features and labels
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN classifier object with weighted voting
knn = KNeighborsClassifier(n_neighbors=3, weights='distance')

# Train the KNN classifier
knn.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = knn.predict(X_test)

# Print the predicted labels
print("Predicted Labels:", y_pred)


# ANS6

# In[70]:


from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def knn_classifier_with_standardization(X_train, X_test, y_train, y_test, n_neighbors=3):
    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Create a KNN classifier object
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    
    # Train the KNN classifier
    knn.fit(X_train_scaled, y_train)
    
    # Predict the labels for the test set
    y_pred = knn.predict(X_test_scaled)
    
    return y_pred


# ANS7

# In[71]:


import math

def euclidean_distance(point1, point2):
    # Ensure both points have the same number of dimensions
    if len(point1) != len(point2):
        raise ValueError("Both points must have the same number of dimensions.")
    
    # Calculate the squared Euclidean distance for each dimension
    squared_distance = sum((x - y) ** 2 for x, y in zip(point1, point2))
    
    # Return the square root of the sum of squared distances
    distance = math.sqrt(squared_distance)
    return distance


# ANS8

# In[72]:


def manhattan_distance(point1, point2):
    # Ensure both points have the same number of dimensions
    if len(point1) != len(point2):
        raise ValueError("Both points must have the same number of dimensions.")
    
    # Calculate the Manhattan distance for each dimension
    distance = sum(abs(x - y) for x, y in zip(point1, point2))
    
    return distance
point1 = (1, 2, 3)
point2 = (4, 5, 6)

distance = manhattan_distance(point1, point2)
print("Manhattan distance:", distance)


# In[ ]:




