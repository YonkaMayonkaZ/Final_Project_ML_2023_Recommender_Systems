# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:16:58 2024

@author: DaNi
"""

#Installing ydata_profiling
!pip install ydata_profiling

#%%
# Import Packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt  # Add this line to import matplotlib for plotting


from ydata_profiling import ProfileReport
# Set options
pd.set_option('display.max_columns', 500)
#%%

#%%
df = pd.read_csv("subset1.csv")
#%%

#%%
# Convert the 'ZipCode' column to categorical
df['zip'] = df['zip'].astype('category')
#%%

#Explonatory Data Analysis
#%%
profile = ProfileReport(df)
profile.to_file("profile_output.html")
#%%

#%%
profile = ProfileReport(merged_data)
profile.to_file("profile_merged_data.html")
#%%

#%%
# Convert 'zip' column to strings
df['zip'] = df['zip'].astype(str)

# Count the number of 4-digit ZIP codes
count_4_digit_zip = df['zip'][df['zip'].str.len() == 4].count()

print(f"Number of 4-digit ZIP codes: {count_4_digit_zip}")
#%%

#%%
zip_frequency = df['zip'].value_counts()
df['ZipCode_Frequency'] = df['zip'].map(zip_frequency)
#%%

#%%
profile = ProfileReport(df)
profile.to_file("profile_output2.html")
#%%

#%%
userdf.Gender.describe()
#%%

#%%
# Use value_counts to count the occurrences of each zip code
zip_counts = userdf['zip'].value_counts()

# Display the most frequent zip code and the max times it appears
print(zip_counts.idxmax())
print(zip_counts.max())
#%%

#%%
#signupdate
userdf.loc['SignDate'] = pd.to_datetime(userdf['SignDate'])
userdf.SignDate.describe()
#%%

#%%
for column in list(userdf.columns):
    print ("{}% of the data from {} column is missing".format(round(userdf[column].isnull().sum() * 100 / len(userdf[column]),3), column))
#%%

#%%
summary_stats = userdf.describe()
missing_values = userdf.isnull().sum
print(missing_values)
#%%

#%%
missing_values = df.isnull().sum()
#%%

# Listening Data
#%%
data = pd.read_csv('subset1.csv', usecols=['CustID', 'Artist', 'playscount'])
#%%

#%%
data[['CustID', 'Artist']].describe()

#%%

#%%
#%%

#%%
#%%