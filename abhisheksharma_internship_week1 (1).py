#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


yearly=pd.read_csv('downloads/yearly_deaths_by_clinic.csv')


# In[7]:


yearly


# In[8]:


yearly['proportion_deaths']=yearly['deaths']/yearly['births']


# In[9]:


yearly


# In[10]:


yearly1=yearly[0:6]
yearly2=yearly[6:12]


# In[11]:


yearly1


# In[12]:


import matplotlib.pyplot as plt

ax=yearly1.plot(x='proportion_deaths',y='year',label='yearly1')
yearly2.plot(x='proportion_deaths',y='year',label='yearly2',ax=ax)


# In[13]:


import pandas as pd
monthly=pd.read_csv('downloads/monthly_deaths.csv',parse_dates=['date'])


# In[14]:


monthly['proportion_deaths']=monthly['deaths']/monthly['births']


# In[15]:


monthly


# In[16]:


monthly.head()


# In[17]:


import matplotlib.pyplot as plt
ax=monthly.plot(x='date',y='proportion_deaths')


# In[18]:


monthly.head()


# In[21]:


import pandas as pd

handwashing_start=pd.to_datetime('1847-06-01')

beforewashing=monthly[monthly['date']<handwashing_start]
afterwashing=monthly[monthly['date']>=handwashing_start]

ax=beforewashing.plot(x='date',y='proportion_deaths',label='before_washing')
afterwashing.plot(x='date',y='proportion_deaths',label='after_washing',ax=ax)


# In[22]:


beforewashing


# In[24]:


before_proportion=beforewashing['proportion_deaths']
after_proportion=afterwashing['proportion_deaths']

meandifference=after_proportion.mean()-before_proportion.mean()
meandifference


# In[25]:


bootmeandiff=[]
for i in range(3000):
    boot_before=before_proportion.sample(frac=1,replace=True)
    boot_after=before_proportion.sample(frac=1,replace=True)
    bootmeandiff.append(boot_after.mean()-boot_before.mean())
   
confidence_interval=pd.Series(bootmeandiff).quantile([0.025,0.975])
confidence_interval


# In[27]:


doctorsshouldwashtheirhand=True


# In[ ]:




