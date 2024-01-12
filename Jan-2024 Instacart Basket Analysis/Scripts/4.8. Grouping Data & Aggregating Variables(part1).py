#!/usr/bin/env python
# coding: utf-8

# # Instructions

# In[2]:


# Import libraries
import numpy as np
import pandas as pd
import os


# In[3]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[27]:


# Import data pkl format
df_ords_prods_merge=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'orders_products_merged_new_columns.pkl'))


# In[28]:


# create subset first million rows
df = df_ords_prods_merge[:1000000]


# In[29]:


# check shape
df.shape


# In[30]:


df.head(10)


# In[31]:


# dropping columns
df= df.drop(columns = ['_merge'])


# In[32]:


df.head(10)


# 
# # Grouping Data with pandas

# In[33]:


# first step of the workflow
df.groupby('product_name')


# # Aggregating Data with agg()
# 

# In[34]:


# second step, Performing a Single Aggregation
df.groupby('department_id').agg({'order_number': ['mean']})


# In[35]:


# without agg() and dot notation
df.groupby('department_id')['order_number'].mean()


# In[36]:


# dot notation without square brackets
df.groupby('department_id').order_number.mean()


# In[37]:


#3 Performing Multiple Aggregations using agg().
df.groupby('department_id').agg({'order_number': ['mean', 'min', 'max']})


# # Aggregating Data with transform()

# In[38]:


# creating a loyalty flag for customers with many orders.(3 steps in 1 code)
df_ords_prods_merge['max_order'] = df_ords_prods_merge.groupby(['user_id'])['order_number'].transform(np.max)


# In[39]:


df_ords_prods_merge.head(15)


# In[40]:


df_ords_prods_merge.head(100)


# In[41]:


# not to assign any options regarding the maximum number of rows to display
pd.options.display.max_rows = None


# In[42]:


# now will show all the first 100 rows 
df_ords_prods_merge.head(100)


# # Deriving Columns with loc()
# 

# In[44]:


df_ords_prods_merge.loc[df_ords_prods_merge['max_order'] > 40, 'loyalty_flag']='Loyal customer'


# In[46]:


df_ords_prods_merge.loc[(df_ords_prods_merge['max_order'] <= 40) & (df_ords_prods_merge['max_order'] > 10), 'loyalty_flag'] = 'Regular customer'


# In[48]:


df_ords_prods_merge.loc[df_ords_prods_merge['max_order'] <= 10, 'loyalty_flag'] = 'New customer'


# In[49]:


df_ords_prods_merge['loyalty_flag'].value_counts(dropna = False)


# In[50]:


df_ords_prods_merge[['user_id', 'loyalty_flag', 'order_number']].head(60)


# In[51]:


# Export Data pkl format
df_ords_prods_merge.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'orders_products_merged_new_columns1.pkl'))


# In[ ]:




