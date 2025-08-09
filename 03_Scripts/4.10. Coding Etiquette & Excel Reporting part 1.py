#!/usr/bin/env python
# coding: utf-8

# # Instacart Grocery Basket Analysis (part 1)
# 

# ## 1. Import data frame and check.
# 
# ## 2. Drop unnecessary columns and PII data.
# 
# ## 3. Analysis Customer behavior in different geographic areas.
# 
#  ### 3.1.  Create a regional segmentation of the data :
#  
#  ### Create a “Region” column based on the “State” column from your customers data set.
# 
# ###   3.2. Determine whether there’s a difference in spending habits between the different U.S. regions.
# 
# ## 4. Customers who don’t generate much revenue for the app.
# 
# ### 4.1. Create a new column called 'Customer_activity'
# ### 4.2. Creating new data Set Hight-activity Customers
# #### 4.2.1 Create a 25% sample of the original DataFrame
# 
# ### 4.3. Create subset of High-activity customers
# #### 4.3.1. Export new data set for the analysis
# 
# ### 4.4 Export sampled data set 

# In[1]:


# import libraries
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[2]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# ## 1. Import data frame.

# In[3]:


# Import data 
df_ords_prods_custo=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'df_ords_prods_custt.pkl'))


# In[4]:


df_ords_prods_custo.info()


# In[5]:


df_ords_prods_custo.head()


# In[6]:


df_ords_prods_custo.columns


# In[7]:


# check missing values from days_since_prior_order column by creating a crosstab to display in Excel
crosstab = pd.crosstab(df_ords_prods_custo['days_since_prior_order'], df_ords_prods_custo['order_number'], dropna = False)


# In[8]:


crosstab.to_clipboard()


# ### “days_since_prior_order” column crosses with order numbers of 1, we’ll see that the entire column is populated with 0s. This supports the initial assumption about missing values and means it can safely disregard them.

# In[9]:


df_ords_prods_custo[['user_id', 'spend_average']].describe()


# ## 2. Drop unnecessary columns and PII data.

# In[10]:


# dropping unnecessary columns and PII data for analysis
df_ords_prods_custo= df_ords_prods_custo.drop(columns = ['_merge','date_joined','add_to_cart_order','first_name','last_name', ])


# In[11]:


df_ords_prods_custo.info()


# ## 3. Analysis Customer behavior in different geographic areas.

# ### 3.1  Create a regional segmentation of the data.

# In[12]:


# reducing data type
df_ords_prods_custo['days_since_prior_order'] = df_ords_prods_custo['days_since_prior_order'].astype('float16')
df_ords_prods_custo['age'] = df_ords_prods_custo['age'].astype('int8')
df_ords_prods_custo['n_dependants'] = df_ords_prods_custo['n_dependants'].astype('int8')
df_ords_prods_custo['income'] = df_ords_prods_custo['income'].astype('int32')
df_ords_prods_custo['order_frequency'] = df_ords_prods_custo['order_frequency'].astype('int8')


# In[13]:


df_ords_prods_custo.info()


# In[14]:


df_ords_prods_custo.head()


# In[15]:


# add new column 'region' setting Northeast region
df_ords_prods_custo.loc[df_ords_prods_custo['state'].isin(['Maine','New Hampshire','Vermont','Massachusetts', 'Rhode Island','Connecticut','New York','Pennsylvania','New Jersey']), 'region'] = 'Northeast'


# In[16]:


# add new column 'region' setting Midwest region
df_ords_prods_custo.loc[df_ords_prods_custo['state'].isin(['Wisconsin','Michigan','Illinois','Indiana', 'Ohio', 'North Dakota','South Dakota''Nebraska','Kansas''Minnesota','Iowa''Missouri']), 'region'] = 'Midwest'


# In[17]:


# add new column 'region' setting South region
df_ords_prods_custo.loc[df_ords_prods_custo['state'].isin(['Delaware', 'Maryland','District of Columbia''Virginia''West Virginia','North Carolina','South Carolina', 'Georgia','Florida',' Kentucky', 'Tennessee', 'Mississippi', 'Alabama', 'Oklahoma', 'Texas', 'Arkansas', 'Louisiana']), 'region'] = 'South'


# In[18]:


# add new column 'region' setting West region
df_ords_prods_custo.loc[df_ords_prods_custo['state'].isin(['Idaho', 'Montana','Wyoming','Nevada','Utah','Colorado','Arizona','New Mexico','Alaska','Washington','Oregon','California','Hawaii']), 'region'] = 'West'


# In[19]:


df_ords_prods_custo['region'].value_counts(dropna=False)


# In[20]:


# Check there are no null values
df_ords_prods_custo['region'].isnull().sum()


# 

# ### 3.2 Determine whether there’s a difference in spending habits between the different U.S. regions
# 

# In[21]:


# Create Crosstab for region and spending flag
region_crosstab=pd.crosstab(df_ords_prods_custo['region'],df_ords_prods_custo['spending_flag'],dropna=False)

region_crosstab


# ## 4.customers who don’t generate much revenue for the app.
# 
# ### 4.1. creating a new column called 'Customer_activity'
# 
# 
# 
# 

# In[22]:


# creating a new column called 'Customer_activity' based on the value of the 'max_order' column
df_ords_prods_custo.loc[(df_ords_prods_custo['max_order'] < 5), 'Customer_activity'] = "Low-activity"
df_ords_prods_custo.loc[(df_ords_prods_custo['max_order'] >= 5), 'Customer_activity'] = "High-activity"


# In[23]:


df_ords_prods_custo['Customer_activity'].value_counts(dropna=False)


# ### 4.2. Creating new data Set Hight-activity Customers
# 
# #### 4.2.1. Create a 25% sample of the original DataFrame

# In[25]:


# Create a 25% sample of the original DataFrame
sampled_ords_prods_custo = df_ords_prods_custo.sample(frac=0.25, random_state=42)

# Print information about the sample
print("Sample Information:")
sampled_ords_prods_custo.info()


# In[27]:


sampled_ords_prods_custo.head()


# ### 4.3. Create subset of High-activity customers

# In[28]:


# creating subset of High-activity customers
df_ords_prods_custo_high = sampled_ords_prods_custo.query("Customer_activity == 'High-activity'").copy()


# In[30]:


print(df_ords_prods_custo_high.shape)


# ### 4.3.1. Export new data set for the analysis

# In[31]:


# exporting new data set for the analysis 
df_ords_prods_custo_high.to_pickle(os.path.join(path, '02 Data/Prepared Data/high_cust_activ.pkl'))


# ### 4.4 Exporting sampled data set 

# In[32]:


sampled_ords_prods_custo.to_pickle(os.path.join(path, '02 Data/Prepared Data/sampl_ords_prod_custo_pii.pkl'))


# In[ ]:




