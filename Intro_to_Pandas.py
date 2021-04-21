#!/usr/bin/env python
# coding: utf-8

# # This is a small lab introducing Pandas in Data Science
# ### In this lab we see how Pandas can be used on structured data to help us evaluate tables

# In[1]:


import pandas as pd


# In[2]:


csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)


# In[3]:


df.head()


# In[5]:


x = df.head()
x


# In[7]:


x = df[['Length']]
x


# In[11]:


y = df[['Artist','Released','Genre']]
y


# In[13]:


z = df.iloc[0,0]
z


# In[15]:


k = df.loc[1,'Artist']
k


# In[16]:


new_index=['a','b','c','d','e','f','g','h']

df_new = df
df_new.index = new_index
df_new = df.loc['a','Artist']
df_new = df.loc['a':'d','Artist']
df_new


# In[ ]:




