#!/usr/bin/env python
# coding: utf-8

# # 01. Importing libraries

# In[1]:


# Import libraries
import pandas as pd
import numpy as np
import os


# # 02. Importing Data

# In[2]:


path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[3]:


df_prods = pd.read_csv(os.path.join(path, '02 Data', 'Original Data','products.csv'), index_col = False)


# In[62]:


df_ords = pd.read_csv(os.path.join(path, '02 Data','Prepared Data' ,'orders_wrangled.csv'), index_col = False)


# # 03. Mixed-Type Data

# In[5]:


# create a data frame 
df_test = pd.DataFrame()


# In[6]:


# create a mixed type column 
df_test['mix'] = ['a', 'b', 1, True]


# In[7]:


df_test.head()


# In[8]:


# check for mixed types
for col in df_test.columns.tolist():
  weird = (df_test[[col]].applymap(type) != df_test[[col]].iloc[0].apply(type)).any(axis = 1)
  if len (df_test[weird]) > 0:
    print (col)


# In[9]:


# convert a column’s data type from numeric to string
df_test['mix'] = df_test['mix'].astype('str')


# # 04. Missing Values

# In[10]:


# Finding Missing Value
df_prods.isnull().sum()


# In[11]:


# create a subset containing only the 16 values in question.
df_nan=df_prods[df_prods['product_name'].isnull()== True]


# In[12]:


df_nan


# In[13]:


# Addressing Missing Values


# In[14]:


df_prods.describe()


# In[17]:


df_prods.shape


# In[18]:


#  non-missing values in a new dataframe
df_prods_clean = df_prods[df_prods['product_name'].isnull() == False]


# In[19]:


df_prods_clean.shape


# In[20]:


# Another way you can drop all missing values
df_prods.dropna(inplace = True)


# In[25]:


df_prods.dropna(subset = ['product_name'], inplace = True)


# In[26]:





# # 05. Duplicates

# In[27]:


# Finding Duplicates, look for full duplicates within Df
df_dups = df_prods_clean[df_prods_clean.duplicated()]


# In[28]:


df_dups


# In[29]:


df_prods_clean.shape


# In[30]:


# Addressing Duplicates
df_prods_clean_no_dups = df_prods_clean.drop_duplicates()


# In[31]:


df_prods_clean_no_dups.shape


# In[32]:


df_prods_clean_no_dups.to_csv(os.path.join(path, '02 Data','Original Data', 'products_checked.csv'))


# # Task Procedure

# In[60]:


# 2 
df_ords.describe()


# # There is a column called "unnamed:0" and some max values are less than the count, the minimum and maximum are the same in the "order number" column

# In[64]:


# 3 Check for mixed-type data in df_ords
for col in df_ords.columns.tolist():
  weird = (df_ords[[col]].applymap(type) != df_ords[[col]].iloc[0].apply(type)).any(axis = 1)
  if len (df_ords[weird]) > 0:
    print (col)


# # 4 No Mixed data

# In[69]:


# 5 Finding Missing Value
df_ords.isnull().sum()


# In[66]:


# create a subset containing only the Missing values in question.

df_nan=df_ords[df_ords['days_since_prior_order'].isnull()== True]


# In[67]:


df_nan


# # In my opinion, I would use the average since the days that differ from the previous purchase do not cover a large relevant range in the precision of the data.

# In[79]:


# 6 Addressing the missing values, replacing with the mean

df_ords['days_since_prior_order'].fillna(1.111484e+01, inplace=True)


# In[75]:


df_ords


# In[81]:


df_ords_clean = df_ords[df_ords['days_since_prior_order'].isnull() ==True]


# In[82]:


# 7 check for duplicate values
df_dups = df_ords_clean[df_ords_clean.duplicated()]


# In[83]:


df_dups


# # No Duplicates Values

# In[85]:


# 9.a exporting df_ords_clean dataframe
df_ords_clean.to_csv(os.path.join(path, '02 Data','Prepared Data', 'orders_checked.csv'))


# In[ ]:


# 9.b exporting df_prods_clean_no_dups dataframe
df_prods_clean_no_dups.to_csv(os.path.join(path, '02 Data','Prepared Data', 'products_checked.csv'))

