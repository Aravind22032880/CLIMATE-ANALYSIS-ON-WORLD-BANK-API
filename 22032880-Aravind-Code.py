#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import wbgapi as wb
import seaborn as sns
import warnings
warnings.filterwarnings("ignore") 


# In[3]:


"""retriving data from world bank api and transpoing data so that we can get countries as coulmns"""
def data(indicator,country_codes, years):
    gen_data = wb.data.DataFrame(indicator, country_codes, mrv=years)
    gen_data_T = gen_data.transpose()
    return gen_data, gen_data_T


# In[4]:


"""as we are dealing with multiple indicators and we need to search world bank resources
   this function helps us to get list of indicators for n keywords"""
def get_indicators(x):
    indicators = wb.search(x)
    return indicators


# In[5]:


countries = ["CHN","IND","USA","RUS","JPN"] # here we have taken top 5 countries wrt pollution


# In[6]:


get_indicators("pollution") # used this function to search all my necessary indicators.


# In[7]:


# comparing co2 and green house gas emissions amoung selected countries
co2 = ["EN.ATM.CO2E.KT"]
ghg = ["EN.ATM.GHGT.KT.CE"]


# In[8]:


# comparing renewable and fossil resource, to understand how we can reduce pollution
renewable = ['EG.FEC.RNEW.ZS']
fossil = ['EG.USE.COMM.FO.ZS']


# In[9]:


#pollution on world data.
pollution = ['EN.ATM.PM25.MC.M3']


# ### Retrieving data

# In[10]:


#getting orginal data and transposed data for co2 and green house gas emissions for latest 15 years data
ret_co2, ret_co2_T = data(co2,countries,15)
ret_ghg, ret_ghg_T = data(ghg,countries,15)


# In[11]:


ret_co2


# In[12]:


ret_ghg


# In[13]:


#describe function
ret_co2_T.describe()


# In[14]:


#retriving data for renewable and fossil engergy from world bank data api
ret_ren, ret_ren_T = data(renewable, countries,5)
ret_fos, ret_fos_T = data(fossil, countries,5)


# In[15]:


ret_ren.describe()


# In[16]:


ret_fos


# In[17]:


#retriving data for pollution, to see how co2 and ghg effects pollution.
pol, pol_T = data(pollution, countries,15)


# In[18]:


pol


# In[19]:


pol_T


# ### plotting graphs.

# In[20]:


plt.figure(figsize=[18,6])
plt.plot(ret_co2_T, marker = 'o',linestyle = "dashed")
plt.legend(labels = ["CHINA","INDIA","JAPAN","RUSSIA","USA"])
plt.xlabel("year")
plt.ylabel("CO2 emissions (kt)")
plt.title("Co2 Emissions")
plt.show()


# In[21]:


#plotting time-series Co2 graph between countries and the world.
plt.figure(figsize=[18,8])
plt.plot(ret_ghg_T, marker = "o", linestyle = "dashed")
plt.legend(labels = ["CHINA","INDIA","JAPAN","RUSSIA","USA"])
plt.xlabel("year")
plt.ylabel("Green house gas emissions")
plt.title("Green house gas Emissions")
plt.show()


# In[22]:


"""as we can see that the index column name is economy, by using this function, we can change the index name
economy to countries"""
def rename(data):
    or_data = data.rename_axis(index = "countries")
    mod_data = or_data.transpose()
    return mod_data


# In[23]:


ren = rename(ret_ren)


# In[24]:


ren


# In[25]:


fos = rename(ret_fos)


# In[26]:


fos


# In[27]:


col = ["brown","pink","gray","olive","cyan"] 
ren.plot(kind='bar', figsize=(8, 8), zorder=2, width=0.5, color = col )


# In[28]:


fos.plot(kind='bar', figsize=(8, 8), zorder=2, width=0.5, color = col )


# In[29]:


#heat map for pollution
corr = pol_T.corr()
corr


# In[30]:


sns.heatmap(corr, annot = True, cmap = "Blues")


# In[ ]:




