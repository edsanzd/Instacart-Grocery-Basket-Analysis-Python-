#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import numpy as np
import pandas as pd
import os


# In[2]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[3]:


# Import data pkl format
df_ords_prods_merged=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'orders_products_merged.pkl'))


# In[4]:


#2 the two busiest days of the week and the two slowest days. Create a new column 
results = []

for value in df_ords_prods_merged["orders_day_of_week"]:
  if value == 0 or value == 1:
    results.append("Busiest days")
  elif value == 4 or value == 3:
    results.append("Least busy days")
  else:
    results.append("Regularly busy days")


# In[5]:


# create new column
df_ords_prods_merged['busiest_days'] = results


# In[6]:


#3  Check the values of this new column for accuracy
df_ords_prods_merged['busiest_days'].value_counts(dropna = False)


# # Regularly busy days are noticeably reduced and the other two variables clearly see their values increased, which shows us a different distribution of the figures with the same total.

# 
# 
# # 4. When too many users make Instacart orders at the same time, the app freezes. The senior technical officer at Instacart wants you to identify the busiest hours of the day. Rather than by hour, they want periods of time labeled “Most orders,” “Average orders,” and “Fewest orders.” Create a new column containing these labels called “busiest_period_of_day.”

# In[7]:


#  printing the frequency of the “order_hour_of_day” column
df_ords_prods_merged['order_hour_of_day'].value_counts(dropna=False)


# In[8]:


# create function 
result1 = []

for value in df_ords_prods_merged["order_hour_of_day"]:
  if value == 10 or value == 11 or value == 14 or value == 15 or value == 13 or value == 12:
    result1.append("Most orders")
  elif value == 3 or value == 4 or value == 2 or value == 5 or value == 1 or value == 0:
    result1.append("Fewest orders")
  else:
    result1.append("Average orders")


# In[9]:


# create new column
df_ords_prods_merged['busiest_period_of_day'] = result1


# In[10]:


#5 Check the frecuency values of this new column for accuracy
df_ords_prods_merged['busiest_period_of_day'].value_counts(dropna = False)


# In[11]:


# Export Data pkl format
df_ords_prods_merged.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'orders_products_merged_new_columns.pkl'))


# In[ ]:




