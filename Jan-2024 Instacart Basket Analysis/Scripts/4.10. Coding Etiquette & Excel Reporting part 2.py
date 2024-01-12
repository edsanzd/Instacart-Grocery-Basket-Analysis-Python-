#!/usr/bin/env python
# coding: utf-8

# # Instacart Grocery Basket Analysis (part 2)

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


# # 1. Import data set.
#  ## Import sampl_ords_prod_custo_pii (25% of the original  dataset).
#  ## Import Departments data set.
#   ### rename the index column.
# # 2. Merge the data frames.
# # 3. Create customer profiles and visualizations.
#  ## 3.1. Age group profile.
#  ## 3.2. Income group profile.
#  ## 3.3. Family group profile.
# # 4. Max, Mean, and Min variables on a customer-profile level for usage frequency and expenditure.
# # 5. Compare your customer profiles with regions and departments. Identify a link between them, Customers may demonstrate different behaviors across regions, which could make this information important.
# # 6. Export the data frame.

# In[3]:


# Importing sampl_ords_prod_custo_pii Df
df_sample_custo=pd.read_pickle(os.path.join(path, '02 Data', 'Prepared Data', 'sampl_ords_prod_custo_pii.pkl'))


# In[4]:


df_sample_custo.info()


# In[5]:


# Import Departments data set
df_depts = pd.read_csv(os.path.join(path, '02 Data/Prepared Data/departments_wrangled.csv'),index_col=0)


# In[6]:


df_depts.head(25)


# In[7]:


# rename the index column as department_id
df_depts.index.names = ['department_id']


# In[8]:


df_depts.reset_index()


# # 2. Merge the data frames 

# In[9]:


# Merge the DataFrames on the 'department_id' column and include the indicator column
df_dept_cust_ords = df_sample_custo.merge(df_depts, on='department_id', how='left', indicator=True)

# Display the information about the merged DataFrame
print(df_dept_cust_ords.info())

# Display the first few rows of the merged DataFrame with the indicator column
print(df_dept_cust_ords.head())


# In[10]:


# Check the values in the '_merge' column
merge_counts = df_dept_cust_ords['_merge'].value_counts()

# Print the result
print(merge_counts)


# # 3. Create customer profiles.

# ## 3.1. Age group profile

# In[11]:


# Create age groups
age_bins = [18, 25, 35, 45, 55, 65, 100]
age_labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
df_dept_cust_ords['age_group'] = pd.cut(df_dept_cust_ords['age'], bins=age_bins, labels=age_labels, right=False)


# In[12]:


# Define a mapping from numerical values to day names
day_of_week_mapping = {
    0: 'Saturday',
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday'
}

# Replace numerical values with day names in the 'orders_day_of_week' column
df_dept_cust_ords['orders_day_of_week'] = df_dept_cust_ords['orders_day_of_week'].replace(day_of_week_mapping)


# In[13]:


# Check unique values in the 'orders_day_of_week' column
unique_values = df_dept_cust_ords['orders_day_of_week'].unique()

# Print the unique values
print(unique_values)


# In[14]:


# Define the order of days of the week
days_order = ['Saturday','Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


# In[15]:


# Set the style for the plot
sns.set(style="whitegrid")

# Plot a grouped bar chart to show the distribution of orders for each age group across days of the week
plt.figure(figsize=(12, 6))
sns.countplot(x='orders_day_of_week', hue='age_group', data=df_dept_cust_ords, order=days_order, palette='viridis')
plt.title('Distribution of Orders Across Days of the Week by Age Group')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.legend(title='Age Group')
plt.show()


# In[16]:


# Export the chart as an image file
plt.savefig(os.path.join(path, '04 Analysis', 'Visualizations', 'bar_DOW.png'))


# ### There are distinct patterns in ordering behavior throughout the week, weekdays and weekends show different ordering behaviors.Each age group contributes uniquely to the overall distribution of orders. and the 65+ age groups exhibit notable peaks on specific days

# In[17]:


# Create a count plot to show the distribution of orders across hours of the day for each age group
plt.figure(figsize=(12, 6))
sns.countplot(x='order_hour_of_day', hue='age_group', data=df_dept_cust_ords, palette='viridis')
plt.title('Distribution of Orders Across Hours of the Day by Age Group')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.legend(title='Age Group')
plt.show()


# ### There is a noticeable increase in orders during the morning hours (8 AM - 10 AM) across all age groups.The 25-34, 35-44, and 45-54 age groups show peaks in orders during typical lunch hours (12 PM - 2 PM).There is a decrease in orders during the early afternoon, followed by a pickup in the evening (5 PM - 7 PM).

# In[18]:


# Export the chart as an image file
plt.savefig(os.path.join(path, '04 Analysis', 'Visualizations', 'countplot_ords_hod_age.png'))


# ## 3.2. Income group profile

# In[19]:


# Print the maximum and minimum values in the "income" column
max_income = df_dept_cust_ords['income'].max()
min_income = df_dept_cust_ords['income'].min()

print(f"Maximum Income: {max_income}")
print(f"Minimum Income: {min_income}")


# In[20]:


# Create income groups based on ranges
income_bins = [min_income, 50000, 100000, 150000, 200000, 250000, max_income]
income_labels = ['0-49k', '50k-99k', '100k-149k', '150k-199k', '200k-250k', '250k+']

# Add an 'income_group' column to the DataFrame
df_dept_cust_ords['income_group'] = pd.cut(df_dept_cust_ords['income'], bins=income_bins, labels=income_labels, right=False)

# Check unique values in the 'income_group' column excluding NaN
unique_income_groups = df_dept_cust_ords['income_group'].dropna().unique()

# Print the unique values
print(unique_income_groups)


# In[21]:


# Set the style for the plot
sns.set(style="whitegrid")

# Plot a grouped bar chart to show the distribution of orders_day_of_week across income groups
plt.figure(figsize=(12, 8))
sns.countplot(x='income_group', hue='orders_day_of_week', data=df_dept_cust_ords, order=income_labels, palette='viridis')

# Set plot labels and title
plt.xlabel('Income Group')
plt.ylabel('Number of Orders')
plt.title('Order Distribution Across Income Groups and Days of the Week')

# Show the plot
plt.legend(title='Day of Week', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()


# ### There are variations in the distribution of orders across different income groups, Some income groups exhibit higher order counts on specific days of the week. Middle-income groups show consistent order counts during week,  Lower-income groups exhibit varied order counts across all days of the week.Upper-income groups consistently place higher orders during weekdays

# In[22]:


# Export the chart as an image file
plt.savefig(os.path.join(path, '04 Analysis', 'Visualizations', 'bar_income_DOW.png'))


# In[23]:


# Define time intervals
time_intervals = {
    'Night': [0, 1, 2, 3, 4, 5],
    'Morning': [6, 7, 8, 9, 10, 11],
    'Afternoon': [12, 13, 14, 15, 16, 17],
    'Evening': [18, 19, 20, 21, 22, 23]
}

# Map each hour to a time interval
df_dept_cust_ords['time_interval'] = pd.cut(df_dept_cust_ords['order_hour_of_day'], bins=[-1, 5, 11, 17, 23], labels=['Night', 'Morning', 'Afternoon', 'Evening'], right=False)

# Set the style for the plot
sns.set(style="whitegrid")

# Plot a grouped bar chart to show the distribution of orders for each time interval across income groups
plt.figure(figsize=(12, 8))
sns.countplot(x='income_group', hue='time_interval', data=df_dept_cust_ords, order=income_labels, palette='viridis')

# Set plot labels and title
plt.xlabel('Income Group')
plt.ylabel('Number of Orders')
plt.title('Order Distribution Across Income Groups and Time Intervals')

# Show the plot
plt.legend(title='Time Interval', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()


# ### Observe that the Afternoon and Evening time intervals have higher order counts. are particular income groups that tend to place more orders during specific time intervals.For instance,if there is a consistent peak in orders during the Evening time interval, consider targeting marketing efforts during that time and consumers with higher income might have different work schedules or preferences for when they place their orders.

# In[24]:


# Export the chart as an image file
plt.savefig(os.path.join(path, '04 Analysis', 'Visualizations', 'bar_income_time.png'))


# ## 3.3. Family Group profile

# In[25]:


# Check the unique values in the 'family_status' column
unique_family_status = df_dept_cust_ords['family_status'].unique()

# Print the unique values
print(unique_family_status)


# In[26]:


# Define a custom function to determine family_groups
def determine_family_groups(row):
    if row['family_status'] == 'married' and row['n_dependants'] == 0:
        return 'Married_no_kids'
    elif row['family_status'] == 'married' and row['n_dependants'] >= 1:
        return 'Married_kids'
    elif row['family_status'] == 'single' and row['n_dependants'] >= 1:
        return 'Single_kids'
    elif row['family_status'] == 'single' and row['n_dependants'] == 0:
        return 'Single_no_kids'
    elif row['family_status'] == 'divorced/widowed' and row['n_dependants'] == 0:
        return 'Divorced/widowed_no_kids'
    elif row['family_status'] == 'divorced/widowed' and row['n_dependants'] >= 1:
        return 'Divorced/widowed_kids'
    elif row['family_status'] == 'living with parents and siblings' and row['n_dependants'] == 0:
        return 'Living with family_no_kids'
    elif row['family_status'] == 'living with parents and siblings' and row['n_dependants'] >= 1:
        return 'Living with family_kids'
    else:
        return 'Other'

# Apply the custom function to create the 'family_groups' column
df_dept_cust_ords['family_groups'] = df_dept_cust_ords.apply(determine_family_groups, axis=1)

# Checking for NaN values
df_dept_cust_ords['family_groups'].value_counts(dropna=False)


# In[27]:


# Set the style for the plot
sns.set(style="whitegrid")

# Plot a grouped bar chart to show the distribution of orders_day_of_week across family groups
plt.figure(figsize=(12, 8))
sns.countplot(x='family_groups', hue='orders_day_of_week', data=df_dept_cust_ords, palette='viridis')

# Set plot labels and title
plt.xlabel('Family Group')
plt.ylabel('Number of Orders')
plt.title('Order Distribution Across Family Groups and Days of the Week')

# Show the plot
plt.legend(title='Day of Week', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()


# ### Observing the bars corresponding to Married_kids and Single_no_kids for each day of the week, identify which days have higher order volumes for each family group.
# ### Married_kids tend to order more on Saturdays and Single_no_kids on weekdays, the marketing team can strategize promotions or targeted advertising to maximize engagement on these days.

# In[28]:


# Calculate the most frequent department for each user
most_frequent_department = df_dept_cust_ords.groupby('user_id')['department'].agg(lambda x: x.value_counts().idxmax())


# In[29]:


# Get the sorted order of departments based on frequency
sorted_departments = most_frequent_department.value_counts().index

# Set the style for seaborn
sns.set(style="whitegrid")

# Create a horizontal bar plot for the most frequent department, ordered in descending order
plt.figure(figsize=(10, 8))
sns.countplot(y=most_frequent_department, order=sorted_departments, palette='viridis')
plt.title('Most Frequent Department for Each User (Ordered)')
plt.xlabel('Count')
plt.ylabel('Most Frequent Department')
plt.show()


# ### We can see the departments with the greatest demand for ordered products, or that allows us to take measures in the departments with the greatest commercial movement for instacart

# # 4. Aggregate the max, mean, and min variables on a customer-profile level for usage frequency and expenditure.

# In[44]:


# Create an empty DataFrame to store the aggregated results
aggregated_profiles = pd.DataFrame()

# Iterate over each user profile
for profile_column in ['income_group', 'age_group', 'family_groups']:
    
    # Group by the current user profile and calculate max, mean, and min for order_frequency and spend_average
    current_profile_agg = df_dept_cust_ords.groupby(profile_column).agg({
        'order_frequency': ['max', 'mean', 'min'],
        'spend_average': ['max', 'mean', 'min']
    }).reset_index()

    # Rename columns for clarity
    current_profile_agg.columns = [profile_column, 
                                   'order_frequency_max', 'order_frequency_mean', 'order_frequency_min',
                                   'spend_average_max', 'spend_average_mean', 'spend_average_min']

    # Append the current profile aggregation to the overall results
    aggregated_profiles = pd.concat([aggregated_profiles, current_profile_agg], axis=1)

# Display the resulting DataFrame
print(aggregated_profiles)


# In[46]:


# aggregated Data from Dataset for age_group 
df_dept_cust_ords.groupby('age_group').agg({'max_order': ['mean','max','min'], 'prices': ['sum','mean','max','min']})


# In[47]:


# aggregated Data from  Dataset for income_group 
df_dept_cust_ords.groupby('income_group').agg({'max_order': ['mean','max','min'], 'prices': ['sum','mean','max','min']})


# In[48]:


# aggregated Data from Dataset for family_groups 
df_dept_cust_ords.groupby('family_groups').agg({'max_order': ['mean','max','min'], 'prices': ['sum','mean','max','min']})


# In[50]:


# Set the style for seaborn
sns.set(style="whitegrid")

# Define the user profiles
user_profiles = ['income_group', 'age_group', 'family_groups']

# Iterate over each user profile
for profile_column in user_profiles:
    # Create a subset of the aggregated data for the current profile
    current_profile_data = aggregated_profiles[[profile_column, 
                                                'order_frequency_max', 'order_frequency_mean', 'order_frequency_min',
                                                'spend_average_max', 'spend_average_mean', 'spend_average_min']]

    # Melt the DataFrame for easier plotting
    current_profile_data_melted = current_profile_data.melt(id_vars=[profile_column], var_name='Metric', value_name='Value')

    # Create a bar plot using Seaborn
    plt.figure(figsize=(12, 6))
    sns.barplot(x=profile_column, y='Value', hue='Metric', data=current_profile_data_melted, log=False)
    plt.title(f'Aggregated Metrics for {profile_column}')
    plt.xlabel(profile_column)
    plt.ylabel('Value')
    plt.legend(title='Metric')
    plt.show()


# ### Although the differentiation is not very clear, we can deduce that the descriptions can show us a relationship between the low-income groups, with those of younger age, and in turn those who are divorced or widowed without children, showing a low activity compared to the other grouped profiles

# # 5. Compare your customer profiles with regions and departments. Identify a link between them, Customers may demonstrate different behaviors across regions, which could make this information important.

# In[51]:


# Create a cross-tabulation for customer profiles and regions
cross_tab_region = pd.crosstab(index=df_dept_cust_ords['income_group'], columns=df_dept_cust_ords['region'])

# Display the cross-tabulation
print(cross_tab_region)


# In[52]:


# Create a cross-tabulation for customer profiles  and departments
cross_tab_department = pd.crosstab(index=df_dept_cust_ords['income_group'], columns=df_dept_cust_ords['department'])

# Display the cross-tabulation
print(cross_tab_department)


# In[53]:


# Export the crosstab table of customer profiles and regions to Excel
cross_tab_region.to_excel('crosstab_region.xlsx')

# Export the crosstab table of customer profiles and departments to Excel
cross_tab_department.to_excel('crosstab_department.xlsx')


# In[57]:


# Visualize the crosstab for Income group profiles and regions
plt.figure(figsize=(10, 8))
sns.heatmap(cross_tab_region, annot=True, cmap='coolwarm', fmt='d', cbar=True)
plt.title('Heatmap of Customer Profiles by Region')
plt.xlabel('Region')
plt.ylabel('Income Group')
plt.show()



# ### In this heat map, we can see the regions with the most income, having a noticeable difference in the southern and western areas, showing in those regions the high margins created by the income groups between 50k-99k and 100k-150k.

# In[61]:


# Calculate the crosstab for Income Group profiles and departments, normalized by columns
cross_tab_department_normalized = pd.crosstab(df_dept_cust_ords['income_group'], df_dept_cust_ords['department'], normalize='columns')

# Visualize the crosstab for Income Group profiles and departments with percentages, swapping axes
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab_department_normalized.T, annot=True, cmap='viridis', fmt='.2%', cbar=True, annot_kws={"size": 8})
plt.title('Heatmap of Customer Profiles by Department (Percentages)')
plt.xlabel('Income Group')
plt.ylabel('Department')
plt.show()


# ### patterns in the heatmap that indicate strong relationships and concentrations of yellow cells indicate that a 50k-99k income group is more likely to purchase from all departments. low percentage purple cells indicate that a 200k above income group is less likely to purchase from all departments.  the marketing team can tailor promotions and campaigns to that group in order to boost sales. Additionally, understanding cross-departmental patterns can help in developing more targeted and effective marketing strategies

# In[62]:


# Department by Age Group
cross_tab_age = pd.crosstab(df_dept_cust_ords['age_group'], df_dept_cust_ords['department'], normalize='columns')

# Visualize the crosstab for customer profiles and departments with percentages
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab_age.T, annot=True, cmap='viridis', fmt='.2%', cbar=True, annot_kws={"size": 8})
plt.title('Heatmap of Customer Profiles by Department (Age Group)')
plt.xlabel('Age Group')
plt.ylabel('Department')
plt.show()


# ### We can see the relationship between the age groups, the younger groups attend less than the groups of people over 65, who represent a higher percentage in all departments.

# In[65]:


# Department by Family Group
cross_tab_family = pd.crosstab(df_dept_cust_ords['family_groups'], df_dept_cust_ords['department'], normalize='columns')

# Visualize the crosstab for customer profiles and departments with percentages
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab_family.T, annot=True, cmap='viridis', fmt='.2%', cbar=True, annot_kws={"size": 8})
plt.title('Heatmap of Customer Profiles by Department (Family Group)')
plt.xlabel('Family Group')
plt.ylabel('Department')
plt.show()


# ### There is a relationship from the group "Married_Kids". a high percentage of consumption, with the "living with family_kids" group showing a relatively lower percentage

# In[63]:


# Department by Region
cross_tab_region = pd.crosstab(df_dept_cust_ords['region'], df_dept_cust_ords['department'], normalize='columns')

# Visualize the crosstab for regions and departments with percentages
plt.figure(figsize=(12, 8))
sns.heatmap(cross_tab_region.T, annot=True, cmap='viridis', fmt='.2%', cbar=True, annot_kws={"size": 8})
plt.title('Heatmap of Customer Profiles by Department (Region)')
plt.xlabel('Region')
plt.ylabel('Department')
plt.show()


# ### The relationship found between the different regions of high demand by department, more than half of the total are distributed in the southern and western regions.

# In[66]:


# Profile Income Group
plt.figure(figsize=(12, 8))
sns.countplot(x='region', hue='income_group', data=df_dept_cust_ords, palette='viridis')
plt.title('Distribution of Income Groups by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.show()


# ### When observing the regions by income groups, as the 50k-99k group had been identified, and the 100k-150k group, they show high consumption in all regions, highlighting the aforementioned high consumption regions, south and west, that is relatively proportional in all regions

# In[67]:


# Profile Age Group
plt.figure(figsize=(12, 8))
sns.countplot(x='region', hue='age_group', data=df_dept_cust_ords, palette='viridis')
plt.title('Distribution of Age Groups by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.show()


# ### The groups of older adults can clearly be distinguished, they have a higher level of consumption in all regions, at the same time we notice that the groups of younger people show a lower level, leaving the other groups in uniformity for each region

# In[69]:


# Profile Family Group
plt.figure(figsize=(12, 8))
sns.countplot(x='region', hue='family_groups', data=df_dept_cust_ords, palette='viridis')
plt.title('Distribution of Family Groups by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.show()


# ### Analyzing the different regions with respect to family groups, we can see a large proportion of "married_kids" users for each region, "living with family_kids" lower attendance, leaving the other groups relatively uniform in each region.

# # 6. Export the data frame.

# In[73]:


df_dept_cust_ords.to_pickle(os.path.join(path, '02 Data/Prepared Data/df_ords_prod_custo_end_pii.pkl'))


# In[ ]:




