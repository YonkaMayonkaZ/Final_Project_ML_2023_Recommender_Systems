# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:30:51 2024

@author: DaNi
"""

#%%
#Import Packages

import pandas as pd
import numpy as np
#%%

#%%
musicdf = pd.read_csv("subset1.csv", usecols=["CustID", "Artist", "playscount"],)
userdf = pd.read_csv("cust.csv", usecols=["CustID", "Gender", "zip", "SignDate"])
#%%

#%%
print(len(userdf))
userdf.head(3)
#%%

#%%
print(len(musicdf))
musicdf.head(2)
#%%
#Merge the data
#%%
data = pd.merge(musicdf, userdf, on="CustID", how='left')
len(data)
data.head(5)
#%%
#Subset
#%%
userdf2 = data.loc[np.random.choice(data.index, size = 10000, replace=False)]
print(data.shape)
print(userdf.shape)
print(userdf2.shape)
#%%