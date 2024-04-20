#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use(style='seaborn')

df=pd.read_csv('all-data.csv',encoding = "ISO-8859-1")
print(df.head())


# In[3]:


df.info()


# In[ ]:




