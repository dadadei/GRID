#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas matplotlib seaborn')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Data Preparation
data = {'Number of Games': [1, 5, 10, 20, 50, 100, 231],
        'Number of Users': [21923, 114, 60, 22, 9, 6, 1]}

df = pd.DataFrame(data)

# Bar Plot for User Behavior Analysis
plt.figure(figsize=(10, 6))
sns.barplot(x='Number of Games', y='Number of Users', data=df)
plt.title('User Behavior Analysis')
plt.xlabel('Number of Games Created')
plt.ylabel('Number of Users')
plt.show()

# Pie Chart for Game Creation Analysis
labels = ['Created', 'In Draft']
sizes = [68.6, 31.4]
colors = ['#66b3ff', '#ff9999']
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Game Creation Analysis')
plt.axis('equal')
plt.show()

# Pie Chart for Sound Usage
labels = ['With Sound', 'Without Sound']
sizes = [84.1, 15.9]
colors = ['#99ff99', '#ffcc99']
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Sound Usage in Games')
plt.axis('equal')
plt.show()


# In[ ]:




