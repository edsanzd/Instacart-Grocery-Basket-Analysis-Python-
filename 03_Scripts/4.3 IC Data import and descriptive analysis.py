#!/usr/bin/env python
# coding: utf-8

# # 01. Importing Libraries

# In[1]:


# Import libraries
import pandas as pd
import numpy as np
import os


# # 02. Importing Data

# In[19]:


df = pd.read_csv(r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis\02 Data\Original Data\orders.csv',index_col=False)


# In[15]:


df = pd.read_csv(r"C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis\02 Data\Original Data\orders.csv", index_col = False)


# In[16]:


df = pd.read_csv(r"C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis\02 Data\Original Data\orders.csv", index_col = False)


# In[17]:


path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[18]:


path


# In[20]:


df = pd.read_csv(os.path.join(path, '02 Data', 'Original Data', 'orders.csv'), index_col = False)


# In[21]:


df.head()


# In[22]:


df.head(30)


# In[23]:


df.tail()


# In[24]:


df.shape


# In[25]:


df.info()


# In[26]:


df.dtypes


# In[27]:


df.columns


# In[28]:


df.describe()


# In[29]:


df = pd.read_csv(os.path.join(path, '02 Data', 'Original Data', 'orders.csv'), nrows=1000)


# In[30]:


vars_list = ['order_id', 'user_id', 'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order']


# In[31]:


df = pd.read_csv(os.path.join(path, '02 Data', 'Original Data', 'orders.csv'), usecols = vars_list)


# In[32]:


vars_list


# In[33]:


df.head()


# In[34]:


df_prods = pd.read_csv(os.path.join(path, '02 Data', 'Original Data','products.csv'), index_col = False)


# In[36]:


df_prods.head(20)


# In[37]:


df_prods.tail(35)


# In[38]:


df_prods.columns


# In[39]:


df_prods.shape


# In[40]:


df_prods.describe()


# In[41]:


df_prods.dtypes


# In[ ]:




