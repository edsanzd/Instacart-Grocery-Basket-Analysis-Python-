#!/usr/bin/env python
# coding: utf-8

# # 01. Importing libraries

# In[2]:


# Import libraries
import pandas as pd
import numpy as np
import os


# # 02. Importing Data

# In[4]:


path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[5]:


df_prods = pd.read_csv(os.path.join(path, '02 Data', 'Original Data','products.csv'), index_col = False)


# In[6]:


df_ords = pd.read_csv(os.path.join(path, '02 Data', 'Original Data','orders.csv'), index_col = False)


# # 03. Data Wrangling
# 

# In[8]:


# Dropping eval_set Column from orders.csv
df_ords.drop(columns = ['eval_set'])


# In[9]:


df_ords.head()


# In[10]:


df_prods.head()


# In[11]:


df_ords['days_since_prior_order'].value_counts(dropna = False)


# In[12]:


df_ords.rename(columns = {'order_dow' : 'orders_day_of_week'}, inplace = True)


# In[13]:


df_ords.head()


# In[14]:


df_ords['order_id'] = df_ords['order_id'].astype('str')


# In[15]:


df_ords.describe()


# In[16]:


df_ords['order_id'].dtype


# # 04. Importing Data

# In[20]:


# importing dataset departaments.csv
df_dep = pd.read_csv(os.path.join(path, '02 Data', 'Original Data','departments.csv'), index_col = False)


# In[18]:


df_dep.head()


# In[21]:


# transposing df_dep
df_dep.T


# In[22]:


df_dep_t = df_dep.T


# In[23]:


df_dep_t


# In[24]:


df_dep_t.reset_index()


# In[25]:


# take the first row of df_dep_t for the header
new_header = df_dep_t.iloc[0]


# In[26]:


new_header


# In[27]:


df_dep_t_new = df_dep_t[1:]


# In[28]:


# take the data under the header row for a new df
df_dep_t_new = df_dep_t[1:]


# In[29]:


df_dep_t_new


# In[30]:


df_dep_t_new.columns = new_header
# set the header row as the df header


# In[31]:


df_dep_t_new


# # 05. Data Dictionaries

# In[32]:


data_dict = df_dep_t_new.to_dict('index')


# In[33]:


data_dict


# In[34]:


df_prods.head()


# In[35]:


print(data_dict.get('19'))


# # 06. Subsetting

# In[38]:


# subset for df_prods that only contains data from the snacks department
df_snacks =  df_prods[df_prods['department_id']==19]


# In[39]:


# looking for a "department_id" value of 19 within the df_prods
df_prods['department_id']==19


# In[41]:


#indexing code again, wrapped within another instance of df_prods[]
df_prods[df_prods['department_id']==19]


# In[42]:


df_snacks =  df_prods[df_prods['department_id']==19]


# In[43]:


df_snacks.head()


# In[44]:


# with the loc function
df_snacks_2 = df_prods.loc[df_prods['department_id'] == 19]


# In[45]:


# the loc function to look into a list: isin([])
df_snacks_3 = df_prods.loc[df_prods['department_id'].isin([19])]


# # 0.1 Task Procedures

# In[50]:


# 2 Dropping eval_set Column from orders.csv
df_ords.drop(columns = ['eval_set'])


# In[51]:


#3 Rename, without overwriting, a variable with an unintuitive name
df_ords.rename(columns = {'order_dow' : 'orders_day_of_week'}, inplace = True)


# In[47]:


df_ords.describe()


# In[52]:


#4  the busiest hour for placing orders
df_ords['order_hour_of_day'].value_counts(dropna = False)


# In[53]:


#5 df_prods data dictionary
data_dict = df_dep_t_new.to_dict('index')


# In[54]:


data_dict


# In[55]:


# meaning number "4" 
print(data_dict.get('4'))


# In[56]:


#6 subset breakfast item sales
df_breakfast = df_prods[df_prods['department_id']==14]


# In[57]:


df_breakfast


# In[60]:


#7 products that customers might use to throw dinner parties.
df_prods.loc[df_prods['department_id'].isin([5,20,7,12])]


# In[61]:


#8 7650 rows × 5 columns


# In[63]:


#9 Extract all the information about the user_id "1"
user_id_1 =  df_ords[df_ords['user_id']==1]


# In[64]:


user_id_1


# In[65]:


#10 providing some details about this user’s behavior
user_id_1.describe()


# In[68]:


# 12 exporting df_ords dataframe 
df_ords.to_csv(os.path.join(path, '02 Data','Prepared Data', 'orders_wrangled.csv'))


# In[69]:


#13 Exporting df_dep_t_new dataframe
df_dep_t_new.to_csv(os.path.join(path, '02 Data','Prepared Data', 'departments_wrangled.csv'))


# In[ ]:




