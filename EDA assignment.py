#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_excel('flight_price.xlsx')
df.head()


# In[3]:


df.shape


# ANS2

# In[4]:


flight_price = df['Price']

plt.hist(flight_price)
plt.title("Distribution of the flight price")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()


# ANS3

# In[5]:


flight_price = df['Price']
print("The minimum value of the flight price dataset:",flight_price.min())
print("The maximum value of the flight price dataset:",flight_price.max())


# ANS4

# In[6]:


import seaborn as sns
airline_prices = df[['Airline', 'Price']]

# Step 4: Create a box plot
sns.boxplot(x='Airline', y='Price', data=airline_prices)
plt.title("Flight price by Airline")
plt.xlabel('Airline')
plt.ylabel('Price')
plt.show()


# ANS5

# In[7]:


import seaborn as sns
airline_prices = df['Price']

# Step 4: Create a box plot
sns.boxplot(x=airline_prices)
plt.title("Flight price by Airline")
plt.xlabel('Airline')
plt.ylabel('Price')
plt.show()


# ANS6

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
flight_df = pd.read_excel('flight_price.xlsx')

# Clean the dataset
flight_df = flight_df.dropna() # Remove any missing values

# Analyze departure date
flight_df['Date_of_Journey'] = pd.to_datetime(flight_df['Date_of_Journey'])
flight_df['Month'] = flight_df['Date_of_Journey'].dt.month
plt.hist(flight_df['Month'])
plt.xlabel('Month')
plt.ylabel('Number of Flights')
plt.show()

# Analyze destination
destination_counts = flight_df.groupby('Destination')['Destination'].count()
destination_counts.plot(kind='bar')
plt.xlabel('Destination')
plt.ylabel('Number of Flights')
plt.show()

# Analyze airline
airline_counts = flight_df.groupby('Airline')['Airline'].count()
airline_counts.plot(kind='bar')
plt.xlabel('Airline')
plt.ylabel('Number of Flights')
plt.show()

# Analyze price
flight_df.boxplot(column='Price', by='Month')
plt.xlabel('Month')
plt.ylabel('Price')
plt.show()


# ANS7

# In[9]:


df.head()


# In[10]:


# Analyze the impact of departure and arrival locations on flight prices
departure_prices = df.groupby('Destination')['Price'].mean().reset_index()
arrival_prices = df.groupby('Arrival Location')['Price'].mean().reset_index()
print(departure_prices)
print(arrival_prices)

# Analyze the impact of departure and arrival dates on flight prices
flight_data['Departure Date'] = pd.to_datetime(flight_data['Departure Date'])
flight_data['Arrival Date'] = pd.to_datetime(flight_data['Arrival Date'])
flight_data['Travel Days'] = (df['Arrival Date'] - df['Departure Date']).dt.days
travel_days_prices = df.groupby('Travel Days')['Price'].mean().reset_index()
print(travel_days_prices)

# Analyze the impact of airline carriers on flight prices
airline_prices = df.groupby('Airline')['Price'].mean().reset_index()
print(airline_prices)

# Analyze the impact of time of day or day of week on flight prices
df['Departure Time'] = pd.to_datetime(flight_data['Departure Time'])
df['Departure Hour'] = df['Departure Time'].dt.hour
df['Departure Day'] = df['Departure Time'].dt.day_name()
hour_prices = df.groupby('Departure Hour')['Price'].mean().reset_index()
day_prices = df.groupby('Departure Day')['Price'].mean().reset_index()
print(hour_prices)
print(day_prices)

# Analyze the impact of type of cabin on flight prices
cabin_prices = df.groupby('Cabin Type')['Price'].mean().reset_index()
print(cabin_prices)


# 
# 
# ANS9
# 
# 
# 
# 

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')


# In[ ]:


df.shape


# ANS9

# In[ ]:





# In[ ]:


import seaborn as sns
google_play_store = df[['Category', 'Rating']]

sns.boxplot(x='Category',y='Rating',data=google_play_store)
plt.title("Rating by the category")
plt.xlabel("category")
plt.ylabel("Rating")
plt.show()


# ANS10

# In[ ]:


df.isnull().sum()


# In[ ]:


"""There are missing values in the dataset of google playstore dataset 
Missing values can impact our analysis in several ways:

Bias: Missing values may cause bias in our analysis, as the data may no longer be representative of the population we are trying to analyze.

Accuracy: Missing values may reduce the accuracy of our analysis, as we may be missing important information that could impact our results.

Sample size: Missing values may reduce the size of our dataset, which can impact the statistical power of our analysis."""


# ANS11

# In[ ]:


df.head(2)


# In[ ]:


size = df['Size']
rating = df['Rating']

plt.scatter(rating,size)
plt.title("Scatter plot of Rating and size")
plt.xlabel("Rting")
plt.ylabel("Size")
plt.show()


# ANS12

# In[13]:





# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv'


# In[14]:


df.head()


# In[12]:


# Drop any duplicates
df.drop_duplicates(inplace=True)

# Remove any rows with missing data
df.dropna(inplace=True)

# Convert the ratings column to numeric
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Group the dataset by app category and calculate the mean rating for each category
category_ratings = df.groupby('Category')['Rating'].mean()

# Sort the categories by their average rating in descending order
category_ratings = category_ratings.sort_values(ascending=False)

import matplotlib.pyplot as plt

# Create a bar chart of the top 10 categories by average rating
plt.bar(category_ratings.index[:10], category_ratings[:10])
plt.xticks(rotation=90)
plt.xlabel('Category')
plt.ylabel('Average Rating')
plt.title('Top 10 App Categories by Average Rating')
plt.show()


# ANS13

# In[15]:


# Drop any duplicates
df.drop_duplicates(inplace=True)

# Remove any rows with missing data
df.dropna(inplace=True)

# Convert the installs column to numeric
df['Installs'] = pd.to_numeric(df['Installs'].str.replace('+', '').str.replace(',', ''))

# Group the dataset by app developers and calculate the total number of app installs for each developer
developer_installs = df.groupby('Developer')['Installs'].sum().sort_values(ascending=False)

# Group the dataset by app developers and calculate the mean rating for each developer
developer_ratings = df.groupby('Developer')['Rating'].mean().sort_values(ascending=False)


# Group the dataset by app developers and count the number of apps developed by each developer
developer_apps = df.groupby('Developer')['App'].count().sort_values(ascending=False)


# Combine the data into a single dataframe
developer_data = pd.concat([developer_installs, developer_ratings, developer_apps], axis=1)
developer_data.columns = ['Total Installs', 'Average Rating', 'Total Apps']

import matplotlib.pyplot as plt

# Create a scatter plot of average rating vs. total installs
plt.scatter(developer_data['Average Rating'], developer_data['Total Installs'])
plt.xlabel('Average Rating')
plt.ylabel('Total Installs')
plt.title('Developer Success: Average Rating vs. Total Installs')
plt.show()

# Create a scatter plot of total apps vs. total installs
plt.scatter(developer_data['Total Apps'], developer_data['Total Installs'])
plt.xlabel('Total Apps')
plt.ylabel('Total Installs')
plt.title('Developer Success: Total Apps vs. Total Installs')
plt.show()


# In[ ]:




