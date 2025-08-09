#!/usr/bin/env python
# coding: utf-8

# # Task procedure

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
df_ords_prods_merge=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'orders_products_merged_new_columns1.pkl'))


# In[4]:


#2 find the aggregated mean of the “order_number” column grouped by “department_id
df_ords_prods_merge.groupby('department_id').agg({'order_number': ['mean']})


# # 3. We can observe the entire series of department identifiers, from ID# 1 to ID# 21, since it covers the entire dataframe.

# # 5. Difference between the spending habits of the three types of customers. Determine is whether the prices of products purchased by loyal customers differ from those purchased by regular or new customers.

# In[5]:


#use the loyalty flag and check statistics of the product prices for each loyalty category
df_ords_prods_merge.groupby('loyalty_flag').agg({'prices': ['mean', 'min', 'max']})


# # 6. looking at the prices of the items people are buying. Create a spending flag for each user based on the average price across all their orders using the following criteria:

# # a. If the mean of the prices of products purchased by a user is lower than 10, then flag them as a “Low spender.” 

# # b. If the mean of the prices of products purchased by a user is higher than or equal to 10, then flag them as a “High spender.”

# In[6]:


# creating the flag
df_ords_prods_merge['spend_average'] = df_ords_prods_merge.groupby(['user_id'])['prices'].transform('max')


# In[ ]:


# checking and erasing the output shown for save memory
df_ords_prods_merge.head(15)


# In[9]:


#a. Create column with spender flag using the criteria
df_ords_prods_merge.loc[df_ords_prods_merge['spend_average'] < 10,'spending_flag'] = 'Low spender'


# In[10]:


#b.
df_ords_prods_merge.loc[df_ords_prods_merge['spend_average'] >= 10,'spending_flag'] = 'High spender'


# In[11]:


# check the frecuency
df_ords_prods_merge['spending_flag'].value_counts(dropna = False)


# In[ ]:


# checking and erase for save memory
df_ords_prods_merge.head()


# # In order to send relevant notifications to users within the app (for instance, asking users if they want to buy the same item again), the Instacart team wants you to determine frequent versus non-frequent customers. Create an order frequency flag that marks the regularity of a user’s ordering behavior according to the median in the “days_since_prior_order” column. The criteria for the flag should be as follows:
# # a. If the median of “days_since_prior_order” is higher than 20, then the customer should be labeled a “Non-frequent customer.”
# # b. If the median is higher than 10 and lower than or equal to 20, then the customer should be labeled a “Regular customer.”
# # c. If the median is lower than or equal to 10, then the customer should be labeled a “Frequent customer.”

# In[14]:


# creating the flag
df_ords_prods_merge['order_frequency'] = df_ords_prods_merge.groupby(['user_id'])['days_since_prior_order'].transform('max')


# In[16]:


#a. Create column with order_frequency_flag using the criteria
df_ords_prods_merge.loc[df_ords_prods_merge['order_frequency'] > 20,'order_frequency_flag']='Non-frequent customer'


# In[17]:


#b.
df_ords_prods_merge.loc[(df_ords_prods_merge['order_frequency'] > 10 ) & (df_ords_prods_merge['order_frequency'] <= 20), 'order_frequency_flag'] = 'Regular customer'


# In[18]:


#c
df_ords_prods_merge.loc[df_ords_prods_merge['order_frequency'] < 10,'order_frequency_flag']='Frequent customer'


# In[19]:


df_ords_prods_merge['order_frequency_flag'].value_counts(dropna = False)


# In[20]:


# Export 
df_ords_prods_merge.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'orders_products_grouped.pkl'))


# In[ ]:




