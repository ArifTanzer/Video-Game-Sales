#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

vgsales = pd.read_csv("C:/vgsales.csv")

vgsales.head(20)


# In[3]:


vgsales.info()


# In[4]:


null_columns=vgsales.columns[vgsales.isnull().any()]
vgsales.isnull().sum()


# In[5]:


vgsales.hist(bins=50,figsize=(10,10), grid=False);


# In[6]:


plt.scatter(vgsales.Year, vgsales.NA_Sales, alpha=0.2)
plt.title("Comparison")


# In[7]:


plt.scatter(vgsales.Year, vgsales.EU_Sales, alpha=0.2)
plt.title("Comparison")


# In[8]:


plt.scatter(vgsales.Year, vgsales.JP_Sales, alpha=0.2)
plt.title("Comparison")


# In[9]:


plt.scatter(vgsales.Year, vgsales.Other_Sales, alpha=0.2)
plt.title("Comparison")


# In[10]:


plt.scatter(vgsales.Year, vgsales.Global_Sales, alpha=0.2)
plt.title("Comparison")


# In[18]:


ax=sns.boxplot(x="Year", y="NA_Sales", data=vgsales)


# In[78]:



ax=sns.stripplot(x="Year", y="NA_Sales", data=vgsales, jitter=True, edgecolor="gray")


# In[12]:


#Feature Engineering

print(vgsales["Genre"].unique())
print(vgsales["Genre"].value_counts())


# In[13]:


#Feature Engineering
#Please go to bottom see all. 
print(vgsales["Publisher"].unique())
print(vgsales["Publisher"].value_counts())


# In[14]:


print(vgsales["Platform"].unique())
print(vgsales["Platform"].value_counts())


# In[15]:


#Feature Engineering
#You can see there is games on multiple platfrom

print(vgsales["Name"].unique())
print(vgsales["Name"].value_counts())


# In[ ]:


plt.scatter(vgsales.Name, vgsales.Genre, alpha=0.2)
plt.title("Comparison")


# In[81]:


#Hypothesis1

sns.set(font_scale=1.4)
vgsales['Year'].plot(kind='hist', figsize=(10, 10));
plt.xlabel("Year", labelpad=14)
plt.ylabel("Sales", labelpad=14)
plt.title("Year Compressive", y=1.015, fontsize=22);


# In[ ]:





# In[ ]:





# In[73]:


#Hyposthesis2

plt.figure(figsize=(30,15))
ax=sns.stripplot(x="Year", y="NA_Sales", data=vgsales, jitter=True, edgecolor="gray")


# In[77]:


#Hyposthesis2

plt.figure(figsize=(30,15))
ax=sns.stripplot(x="Year", y="EU_Sales", data=vgsales, jitter=True, edgecolor="gray")


# In[ ]:


#inferential analytics
#Start from top to work all libraries and at the end work on this


vgsales[["NA_Sales","EU_Sales", "JP_Sales"]].describe()


# In[ ]:


stats.levene(vgsales["NA_Sales"],vgsales["EU_Sales"])


# In[ ]:


vgsales["NA_Sales"].corr(vgsales['EU_Sales'])

