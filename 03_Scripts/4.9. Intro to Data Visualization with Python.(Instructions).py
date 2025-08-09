#!/usr/bin/env python
# coding: utf-8

# # Instructions

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import scipy


# In[2]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[7]:


# Import data pkl format
df_ords_prods_viz=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'orders_products_grouped.pkl'))


# # Creating Bar Charts

# In[8]:


# Create a bar chart 
df_ords_prods_viz['orders_day_of_week'].value_counts().plot.bar()


# In[10]:


# add sort_index() function
bar = df_ords_prods_viz['orders_day_of_week'].value_counts().sort_index().plot.bar()


# In[11]:


# check frequency 
df_ords_prods_viz['orders_day_of_week'].value_counts()


# In[12]:


# check frequency sorting index
df_ords_prods_viz['orders_day_of_week'].value_counts().sort_index()


# In[13]:


# adding a color argument in the plot.bar() function
bar = df_ords_prods_viz['orders_day_of_week'].value_counts().plot.bar(color =['purple', 'red', 'pink', 'orange', 'yellow', 'green', 'blue'])


# In[14]:


# export as image file via the figure.savefig() function
bar.figure.savefig(os.path.join(path, '04 Analysis','Visualizations', 'bar_orders_dow.png'))


# # Creating Histograms and Scatterplots.
# 
# #### Histograms:

# In[16]:


# create Histogram
df_ords_prods_viz['prices'].plot.hist(bins = 25)


# In[17]:


# descriptive statistics for a column.
df_ords_prods_viz['prices'].describe()


# ### checks for each specific statistic

# In[18]:


df_ords_prods_viz['prices'].mean()


# In[19]:


df_ords_prods_viz['prices'].median()


# In[20]:


df_ords_prods_viz['prices'].max()


# #### scatterplot:

# In[22]:


# create a scatterplot 
sns.scatterplot (x = 'prices', y = 'prices', data = df_ords_prods_viz)


# In[ ]:


# check outliers
df_ords_prods_viz.loc[df_ords_prods_viz['prices'] > 100]


# In[24]:


df_ords_prods_viz.loc[df_ords_prods_viz['prices'] >100, 'prices'] = np.nan


# In[25]:


df_ords_prods_viz['prices'].max()


# In[26]:


#  histogram after ad hoc cleaning
hist = df_ords_prods_viz['prices'].plot.hist(bins = 25)


# In[27]:


# increasing the number of bins
hist_2 = df_ords_prods_viz['prices'].plot.hist(bins = 70)


# In[42]:


# export as hist image file via the figure.savefig() function
hist.figure.savefig(os.path.join(path, '04 Analysis','Visualizations', 'hist_orders_dow.png'))


# # Creating Line Charts

# In[43]:


# create subset to save memory
df = df_ords_prods_viz[:2000000]


# ### Sampling Data

# In[44]:


# create sample and a list holding True/False values to the test np.random.rand( <=0.7)
np.random.seed(4)
dev = np.random.rand(len(df_ords_prods_viz)) <= 0.7


# In[45]:


dev


# In[46]:


np.random.rand(10)


# In[47]:


# Store 70% of the sample in the dataframe big
big = df_ords_prods_viz[dev]


# In[48]:


# Store 30% of the sample in the dataframe small 
small = df_ords_prods_viz[~dev]


# In[49]:


len (df_ords_prods_viz)


# In[50]:


len(big) + len(small)


# In[51]:


df_2 = small[['orders_day_of_week','prices']]


# In[52]:


line = sns.lineplot(data = df_2, x = 'orders_day_of_week',y = 'prices')


# In[53]:


# export as line image file via the figure.savefig() function
line.figure.savefig(os.path.join(path, '04 Analysis','Visualizations', 'line_orders_dow.png'))


# In[54]:


# Export 
df_ords_prods_viz.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'orders_products_Visual.pkl'))


# In[ ]:




