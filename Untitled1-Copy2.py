#!/usr/bin/env python
# coding: utf-8

# Data Cleansing --------

# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("ggplot")
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
sns.set_style("darkgrid")
mpl.rcParams['figure.figsize'] = (20,5)


# In[6]:


ytdata = pd.read_csv('US_youtube_trending_data.csv')


# In[3]:


# View first few rows
print(ytdata.head())

# Summary statistics
print(ytdata.describe())

# Check data types and missing values
print(ytdata.info())


# In[4]:


# Remove duplicate rows
ytdata.drop_duplicates(inplace=True)
# Number of non null counts or non missing data points
non_null_counts = ytdata.count()
print(non_null_counts)


# Taking a look at dislikes, likes, and comment counts in how it affects viewership.

# In[3]:


trending_columns = ytdata[['view_count', 'likes', 'dislikes', 'comment_count']]
# Calculate the correlation matrix
correlation_matrix = trending_columns.corr()

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Numerical Attributes')
plt.show()


# This heatmap basically says numbers closer to 1 or -1 indicate postive or negative coorelations, Using this and looking at the View_Count which is our most importnat statistic to determine the best or most trending videos is that likes can most closely be attributed to higher view counts. While dislikes are our most negative impacting attribute which is assumed but is interesting considering the data is composed of the most trending videos.

# 

# In[5]:


# Selecting necessary columns
trending_columns = ytdata[['likes', 'dislikes', 'comment_count', 'view_count']]

# Scatter plot with bubble size representing view_count
plt.figure(figsize=(10, 6))

plt.scatter(selected_columns['likes'], selected_columns['dislikes'], s=selected_columns['view_count'] / 1000, alpha=0.5)
plt.xlabel('Likes')
plt.ylabel('Dislikes')
plt.title('Likes vs Dislikes (Bubble size = View Count)')
plt.grid(True)
plt.colorbar(label='View Count (in thousands)')
plt.show()

# Alternatively, for likes vs comment_count
plt.figure(figsize=(10, 6))

plt.scatter(selected_columns['likes'], selected_columns['comment_count'], s=selected_columns['view_count'] / 1000, alpha=0.5)
plt.xlabel('Likes')
plt.ylabel('Comment Count')
plt.title('Likes vs Comment Count (Bubble size = View Count)')
plt.grid(True)
plt.colorbar(label='View Count (in thousands)')
plt.show()


# While the above graphs are somewhat hard to read we can gather a few key pieces of information, Low like counts generally less comments and views while dislikes are generally less important when it comes to views and engagement.

# Anylyzing Titles and Descriptions.

# In[20]:


from collections import Counter
import re
import string
import matplotlib.pyplot as plt

# Group all titles or tags into a single string
ytext = ' '.join(ytdata['title'])  # For titles

# Preprocessing: Convert text to lowercase, remove punctuation and specific words
ytext = text.lower()  # Convert to lowercase
ytext = re.sub('['+string.punctuation+']', '', text)  # Remove punctuation

# Words to exclude
excluded_words = {'the', 'and', 'or', 'is', 'of','to','in','A','a','On', '1','2','3','4','5','6','7','8', '9', 'To', 'The', 'on', 'my','My', "with","With",'In', 'at', 'You' 'for'}  

# Split the text into words and filter out the excluded words
word_list = ytext.split()
filtered_words = [word for word in word_list if word not in excluded_words]

# Count word frequencies
word_counts = Counter(filtered_words)

# Get the most common words and their frequencies
most_common = word_counts.most_common(20)  # Change 10 to display more or fewer words

# Extract words and counts for the bar chart
words = [word[0] for word in most_common]
counts = [count[1] for count in most_common]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(words, counts)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Most Frequent Words in Video Titles')
plt.xticks(rotation=45, ha='right')  # Rotate x-labels for better readability
plt.tight_layout()
plt.show()


#  Excluding words I dont think were important like "a,and,The,if,", Looking at this bar chart can give us alot of information, Starting from the bottom, Seasonal information in videos like the current and even the word "Season" attribute to more views, another insight is the first 2 enteries, "Official" and "Video" this could mean that putting the word "Official" behind any title could increase veiwership, or adding "Video" to the end. another insight are the words "You" and "For" this could mean videos with titles like "How You can become better at cooking" or "Cooking for begginers" these are more personable and drive more views, another insight I have are based on media catergories, "Game, Music, ft, HIGHLIGHTS" this could just indicate these are popular categories on the site, which should not be ignored, and lastly the use of capital letters, "Highlights" appears twice once all capital and one not while the all caps version is lower on the board it is still the 20th most used word in popular youtube videos, this insight should not be ignored either.

# Now lets take a look at the most popular categories on youtube utilizing the category_id column 

# In[7]:


# Count the occurrences of each category ID
category_counts = ytdata['categoryId'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Videos across Different Categories (Pie Chart)')
plt.axis('equal')
plt.tight_layout()
plt.show()


# Insights----
