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
music = pd.read_csv("subset1.csv", usecols=["CustID", "Artist", "playscount"],)
user = pd.read_csv("cust.csv", usecols=["CustID", "Gender", "zip", "SignDate"])
#%%

#%%
print(len(cust))
cust.head(3)
#%%
