#!/usr/bin/env python
# coding: utf-8

# # Merging Instacart Data (Instructions)

# In[2]:


# Import libraries
import numpy as np
import pandas as pd
import os


# In[3]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[9]:


# Import data
df_ords = pd.read_csv(os.path.join(path, '02 Data','Prepared Data' ,'orders_wrangled.csv'), index_col = False)
df_ords_prior = pd.read_csv(os.path.join(path, '02 Data','Original Data','orders_products_prior.csv'),index_col = False)


# In[6]:


# check the output
df_ords_prior.head()


# In[11]:


df_ords_prior.shape


# In[22]:


df_ords.head()


# In[21]:


df_ords.shape


# In[40]:


df_merged_large = df_ords.merge(df_ords_prior, on = 'order_id', indicator = True)


# In[41]:


df_merged_large.head()


# In[42]:


df_merged_large['_merge'].value_counts()


# In[43]:


df_merged_large.shape


# In[44]:


# Export the merged file in pickle format as “orders_products_combined.pkl”.
df_merged_large.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'orders_products_combined.pkl'))


# In[45]:


# Export the merged file in csv. format as “orders_products_combined.csv”.
df_merged_large.to_csv(os.path.join(path, '02 Data','Prepared Data', 'orders_products_combined.csv'))


# In[ ]:




