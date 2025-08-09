#!/usr/bin/env python
# coding: utf-8

# #  Instructions 

# In[ ]:


# Import libraries
import numpy as np
import pandas as pd
import os


# In[ ]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[ ]:


# Import data pkl format
df_ords_prods_merged=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'orders_products_merged.pkl'))


# In[ ]:


# create subset first million rows
df = df_ords_prods_merged[:1000000]


# In[ ]:


# check shape
df.shape


# # If-Statements with User-Defined Functions

# In[ ]:


# create and assign flag according to price by user-defined function
def price_label(row):
  if row['prices'] <= 5:
    return 'Low-range product'
  elif (row['prices'] > 5) and (row['prices'] <= 15):
    return 'Mid-range product'
  elif row['prices'] > 15:
    return 'High range product'
  else: return 'Not enough data'


# In[ ]:


# Apply the Function
df['price_range'] = df.apply(price_label, axis=1)


# In[ ]:


df['price_range'].value_counts(dropna=False)


# In[ ]:


# check maximum values
df['prices'].max()


# # If-Statements with the loc() Function

# In[ ]:


df.loc[df['prices'] > 15, 'price_range_loc']='High range product'


# In[ ]:


df.loc[(df['prices'] <= 15) & (df['prices'] > 5), 'price_range_loc']='Mid-range product'


# In[ ]:


df.loc[df['prices'] <= 5, 'price_range_loc'] = 'Low-range product'


# In[ ]:


df['price_range_loc'].value_counts(dropna=False)


# In[ ]:


df_ords_prods_merged.loc[df_ords_prods_merged['prices'] > 15, 'price_range_loc']='High range product'


# In[ ]:


df_ords_prods_merged.loc[(df_ords_prods_merged['prices'] <= 15) & (df_ords_prods_merged['prices'] > 5), 'price_range_loc'] = 'Mid-range product'


# In[ ]:


df_ords_prods_merged.loc[df_ords_prods_merged['prices'] <= 5, 'price_range_loc'] = 'Low-range product'


# In[ ]:


df_ords_prods_merged['price_range_loc'].value_counts(dropna = False)


# # If-Statements with For-Loops

# In[ ]:


#  printing the frequency of the “orders_day_of_week” column
df_ords_prods_merged['orders_day_of_week'].value_counts(dropna=False)


# In[ ]:


result = []

for value in df_ords_prods_merged["orders_day_of_week"]:
  if value == 0:
    result.append("Busiest day")
  elif value == 4:
    result.append("Least busy")
  else:
    result.append("Regularly busy")


# In[ ]:


result


# In[ ]:


# create new column
df_ords_prods_merged['busiest_day'] = result


# In[46]:


df_ords_prods_merged['busiest_day'].value_counts(dropna = False) 


# In[ ]:


# Export Data pkl format
df_ords_prods_merged.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'orders_products_merged_new columns.pkl'))

