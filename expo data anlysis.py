#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('max_columns', 200)


# In[2]:


df = pd.read_csv('cost.csv')


# In[3]:


df.shape


# In[4]:


df.head(5)


# In[5]:


df.columns


# In[6]:


df.dtypes


# In[7]:


df.describe()


# In[8]:


# Example of dropping columns
# df.drop(['Opening date'], axis=1)


# In[9]:


df = df[['coaster_name',
    # 'Length', 'Speed',
    'Location', 'Status',
    # 'Opening date',
    #   'Type',
    'Manufacturer',
#     'Height restriction', 'Model', 'Height',
#        'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
#        'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
#        'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
#        'Track layout', 'Fastrack available', 'Soft opening date.1',
#        'Closing date',
#     'Opened', 
    # 'Replaced by', 'Website',
#        'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
#        'Single rider line available', 'Restraint Style',
#        'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced',
        'latitude', 'longitude',
    'Type_Main',
       'opening_date_clean',
    #'speed1', 'speed2', 'speed1_value', 'speed1_unit','speed_mph', 
    #'height_value', 'height_unit',
    'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()


# In[10]:


df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])


# In[11]:


# Rename our columns
df = df.rename(columns={'coaster_name':'Coaster_Name',
                   'year_introduced':'Year_Introduced',
                   'opening_date_clean':'Opening_Date',
                   'speed_mph':'Speed_mph',
                   'height_ft':'Height_ft',
                   'Inversions_clean':'Inversions',
                   'Gforce_clean':'Gforce'})


# In[12]:


df.isna().sum()


# In[13]:


df.loc[df.duplicated()]


# In[14]:


df.loc[df.duplicated(subset=['Coaster_Name'])].head(5)


# In[15]:


df.query('Coaster_Name == "Crystal Beach Cyclone"')


# In[16]:


df.columns


# In[17]:


df['Year_Introduced'].value_counts()


# In[18]:


ax = df['Year_Introduced'].value_counts()     .head(10)     .plot(kind='bar', title='Top 10 Years Coasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')


# In[22]:


df['Type_Main'].value_counts()


# In[ ]:





# In[ ]:




