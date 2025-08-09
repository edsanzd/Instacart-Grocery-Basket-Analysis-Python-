#!/usr/bin/env python
# coding: utf-8

# # Task procedure part 1.
# 
# ### 3. Import analysis libraries, as well as the new customer data set as a dataframe.

# In[1]:


# Import libraries 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import scipy


# In[2]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[3]:


# Import data 
df_ords_prods_viz=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'orders_products_Visual.pkl'))


# In[4]:


df_ords_prods_viz.info()


# In[5]:


# Import new database as new dataframe
df_cust = pd.read_csv(os.path.join(path, '02 Data', 'Original Data', 'customers.csv'), index_col = False)


# ### 4. Wrangle the data so that it follows consistent logic; for example, rename columns with illogical names and drop columns that don’t add anything to your analysis.
# 
# #### Check new dataframe

# In[6]:


df_cust.head()


# In[7]:


df_cust.shape


# In[8]:


df_cust.describe()


# In[9]:


df_cust.info()


# In[10]:


# rename columns
df_cust.rename(columns = {'First Name':'first_name', 'Surnam':'last_name','Gender':'gender', 'STATE':'state','Age':'age','fam_status':'family_status'}, inplace = True)


# In[11]:


# change type of the column
df_cust['user_id'] = df_cust['user_id'].astype('str')


# In[12]:


# change the column to datetime type
df_cust['date_joined'] = pd.to_datetime(df_cust['date_joined'])


# In[13]:


df_cust.head()


# ### 5. Complete the fundamental data quality and consistency checks:
# 
# ### check for and address missing values and duplicates, and convert any mixed-type data

# In[14]:


# check for columns that have mixed data type
for col in df_cust.columns.tolist():
    weird = (df_cust[[col]].map(type) != df_cust[[col]].iloc[0].apply(type)).any(axis = 1)
    
    if len (df_cust[weird]) > 0:
        print (col)


# #### mixed values for "first_name" column

# In[15]:


# change the column mixed values to 'str' type
df_cust['first_name'] = df_cust['first_name'].astype('str')


# In[16]:


# find columns with missing values
df_cust.isnull().sum()


# #### No missing values found

# In[17]:


# create a subset and find a list of duplicated
df_dups = df_cust[df_cust.duplicated()]
df_dups.shape


# #### No duplicates found

# In[18]:


# Double check if is not null
df_cust[(df_cust['first_name']==1) & (df_cust['first_name'].isnull()==False)]


# ### 6. Combine customer dataframe with the rest of  prepared Instacart dataframe
# 

# In[19]:


# Dropping _merge and aisle_id Columns
df_ords_prods_viz = df_ords_prods_viz.drop(columns=['_merge', 'aisle_id'])


# In[20]:


# change type of the column 
df_ords_prods_viz['user_id'] = df_ords_prods_viz['user_id'].astype('str')


# In[21]:


df_ords_prods_viz.info()


# In[24]:


for col in df_ords_prods_viz.columns:
    if df_ords_prods_viz[col].dtype == "int64":
        for t in ["int8", "int16", "int32"]:
            if (df_ords_prods_viz[col].astype(t) == df_ords_prods_viz[col]).all():
                df_ords_prods_viz[col] = df_ords_prods_viz[col].astype(t)
                break
    elif df_ords_prods_viz[col].dtype == "float64":
        for t in ["float16", "float32"]:
            if np.isnan(df_ords_prods_viz[col]).any() or (df_ords_prods_viz[col].astype(t) == df_ords_prods_viz[col]).all():
                df_ords_prods_viz[col] = df_ords_prods_viz[col].astype(t)
                break


# In[25]:


df_ords_prods_viz.info()


# In[27]:


# Merge the DataFrames
df_ords_prods_viz = df_ords_prods_viz.merge(df_cust, on='user_id', indicator=True)


# In[29]:


# Export Df
df_ords_prods_viz.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'df_ords_prods_cust.pkl'))


# In[ ]:




