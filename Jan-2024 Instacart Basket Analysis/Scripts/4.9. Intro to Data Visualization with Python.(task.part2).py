#!/usr/bin/env python
# coding: utf-8

# # Task procedure part 2.
# 
# ### 1. Import analysis libraries, as well the most up-to-date project data set as a dataframe.

# In[4]:


# Import libraries 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import matplotlib as mpl


# In[5]:


# Set path
path = r'C:\Users\gered\OneDrive\Desktop\Python.CF\06-11-2023 Instacart Basket Analysis'


# In[6]:


# Import data 
df_ords_prods_cust=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'df_ords_prods_cust.pkl'))


# ### 3. Descriptive findings about sales

# In[7]:


# Create a histogram of the “order_hour_of_day” column
hist_ohod = df_ords_prods_cust['order_hour_of_day'].plot.hist(bins = 24, xlabel = 'hours of day', ylabel='number of orders')


# ### It can be seen in the histogram how the number of orders increases starting at 9 am, having a constant sales peak between 10 am and 3 pm, where the number of orders gradually begins to decrease.

# In[8]:


# export as hist image file via the figure.savefig() function
hist_ohod.figure.savefig(os.path.join(path, '04 Analysis','Visualizations', 'hist_orders_hod.png'))


# In[9]:


df_ords_prods_cust['order_hour_of_day'].value_counts()


# ### 4. Distribution of orders among customers in terms of loyalty

# In[10]:


# Creating a horizontal bar chart from the “loyalty_flag” column
bar_loyal=df_ords_prods_cust['loyalty_flag'].value_counts().plot.barh()

# Customize the chart as needed
plt.title('Customer Loyalty')
plt.xlabel('Number of Orders')
plt.ylabel('Loyalty Level')
bar_loyal.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x,pos: format(x/1000000,'1.0f')+'M'))
plt.show()


# In[11]:


# check frequency 
df_ords_prods_cust['loyalty_flag'].value_counts()


# In[12]:


# Export bar chart 
bar_loyal.figure.savefig(os.path.join(path, '04 Analysis','Visualizations', 'bar_loyalty.png'))


# In[13]:


# checking the proportion for each loytalty type of customer
print("Regular Customer: " + str((15876776 / (15876776+10284093+6243990)*100)) + "%")
print("Loyal Customer: " + str((10284093 / (15876776+10284093+6243990)*100)) + "%")
print("New Customer: " + str((6243990 / (15876776+10284093+6243990)*100)) + "%")


# ### We can observe that regular customers are almost half of the total, which tells us the dominant trend, as for loyal customers, they are a third of the total, leaving new customers to a lesser extent, which makes it convenient to analyze how we could move this type of customers at a level more satisfactory for the company

# ### 5. Check whether there’s a difference in expenditure (the “prices” column) depending on the hour of the day

# ### set the conditions for derived columns

# In[14]:


# create sample and a list holding True/False values to the test np.random.rand( <=0.7)
np.random.seed(4)
dev = np.random.rand(len(df_ords_prods_cust)) <= 0.7


# In[15]:


# randomizing True and False values
dev


# In[16]:


# produces a list of random numbers between 0 and 1
np.random.rand(10)


# In[17]:


# Store 70% of the sample in the dataframe big
big = df_ords_prods_cust[dev]

# Store 30% of the sample in the dataframe small
small = df_ords_prods_cust[~dev]


# In[18]:


len (df_ords_prods_cust)


# In[19]:


len(big) + len(small)


# In[20]:


# reducing samples to only those columns necessary for the chart
df_ohod_prices = small[['order_hour_of_day','prices']]


# In[21]:


df_ohod_prices.info()


# In[23]:


df_ohod_prices['prices'] = df_ohod_prices['prices'].astype('float32')


# In[24]:


# create the line Chart 
line2 = sns.lineplot(data = df_ohod_prices, x = 'order_hour_of_day',y = 'prices')


# ### It can be observed in the early morning hours, high value sales compared with the sales around 10 a.m.

# In[25]:


# export as image file 
line2.figure.savefig(os.path.join(path, '04 Analysis','Visualizations', 'line_ohod_price.png'))


# ### 6. Conduct some exploratory analysis of customer demographics to inform the targeted marketing campaigns.
# ### Determine whether there’s a connection between age and family situation by creating a line chart exploring the connections between age and number of dependents

# In[26]:


# Extract necessary columns into a dataframe
df_age_dependants = df_ords_prods_cust[['age','n_dependants']]


# In[27]:


df_age_dependants.info()


# In[28]:


# create the line chart 
line3 = sns.lineplot(data=df_age_dependants, x='age', y='n_dependants')
plt.title('Connection Age vs Number of dependants')
line3.set(xlabel='Age', ylabel='Number of dependants')


# ### There is no correlation between the variables, the differences found are very random.

# In[29]:


# export the chart as image file 
line3.figure.savefig(os.path.join(path, '04 Analysis/Visualizations/line_age_ndependants.png'))


# ### 7. Explore whether there’s a connection between age and spending power (income).
# 

# In[30]:


# Extract age and income into a separate dataframe
df_age_income = df_ords_prods_cust[['age', 'income']]
df_age_income.info()


# In[31]:


# visualize the relationship, creating a scatterplot
scatter_age_income = sns.scatterplot(x='age', y='income', data=df_age_income)
plt.title('Connection Age vs Income')


# In[32]:


# export the chart as image file 
scatter_age_income.figure.savefig(os.path.join(path, '04 Analysis', 'Visualizations','scatter_age_income.png'))


# In[34]:


# export Df
df_ords_prods_cust.to_pickle(os.path.join(path, '02 Data','Prepared Data', 'df_ords_prods_custt.pkl'))


# In[ ]:




