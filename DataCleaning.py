# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:16:58 2024

@author: DaNi
"""

#%%
# Import Packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt  # Add this line to import matplotlib for plotting

# Set options
pd.set_option('display.max_columns', 500)
#%%

#%%
userdf = pd.read_csv("cust.csv", usecols=["CustID", "Gender", "zip", "SignDate"])
#%%

#%%
userdf.Gender.describe()
#%%

#%%
userdf.zip.describe()
#%%

#%%
#%%

#%%
#%%

#%%
#%%

#%%
#%%

#%%
#%%

#%%
#%%

#%%
#%%

#%%
#%%