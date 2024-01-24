# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 01:06:32 2024

@author: DaNi
"""

#%%
import pandas as pd

# Import the datasets
tracks = pd.read_csv("tracks.csv")
cust = pd.read_csv("cust.csv")
music = pd.read_csv("music.csv")

# Make the correct data format
# Merge datasets
merged_data = pd.merge(tracks, music, on='TrackId', how='left')
merged_data = pd.merge(merged_data, cust, on='CustID', how='left')

# Group by customer id and artist id, and calculate playscount
playscount_data = merged_data.groupby(['CustID', 'Artist']).size().reset_index(name='playscount')

# Select relevant columns from cust dataset
result_data = cust[['CustID', 'Gender', 'Address', 'zip', 'SignDate']]

# Merge playscount data with result data
result_data = pd.merge(result_data, playscount_data, on='CustID', how='left')

# Fill NaN values with 0 in playscount column
result_data['playscount'] = result_data['playscount'].fillna(0).astype(int)

# Print or save the result_data dataframe as needed
subset1 = result_data.drop(columns='Address')
print(result_data)

# Make a csv file to pass to spark
csv_file_path = 'subset1.csv'
subset1.to_csv(csv_file_path, index=False)
#%%