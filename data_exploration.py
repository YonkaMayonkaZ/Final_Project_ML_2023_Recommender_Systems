# -*- coding: utf-8 -*-

#%%
# import the usual
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Set the default style for seaborn
sns.set(style="whitegrid")

# Increase the display of maximum columns
pd.set_option('display.max_columns', 500)
#%%


#Import datasets
#%%
df = pd.read_csv('subset1.csv', index_col=0)
userdf = pd.read_csv("cust.csv", usecols=["CustID", "Gender", "zip", "SignDate"])
#%%

#%%
userdf['SignDate'] = pd.to_datetime(userdf['SignDate'],infer_datetime_format=True)
# Display the first few rows of each dataframe
print("userdf:")
print(userdf.head())

print("\ndf:")
print(df.head())
#%%

#Missing Data
#%%
for column in list(df.columns):
   missing_percentage = round(df[column].isnull().sum() * 100 / len(df), 2)
   print("{}% of the data from {} column is missing".format(missing_percentage, column))
#%%

# Most Active Users
#%%
user_count = pd.pivot_table(df, index="CustID", values="playscount", aggfunc="sum").sort_values(by="playscount", ascending=False)
user_count.head()
#%%


#%%
fig = plt.figure(figsize=(10,5))
user_count.head(20).plot(kind='bar')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
plt.ylabel("Plays")
plt.xlabel("(UserIds not shown)")
plt.title("Top 10 most active Listeners")
#%%

#Most Popular Artist
#%%
top_artists = pd.pivot_table(df,index="Artist",values="playscount",aggfunc="sum").sort_values(by="playscount", ascending=False)
#%%

#%%
fig = plt.figure(figsize=(10,5))
top_artists.head(20).plot(kind="bar")
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off')         # ticks along the top edge are off) # labels along the bottom edge are off
plt.ylabel("Plays")
plt.xlabel("Artists")
plt.title("Top 20 most popular Artists")
#%%

#Gender Proportions
#%%
sns.catplot(data=userdf,x='Gender',kind='count',height=5, aspect=2)
#%%

#Locations by zip code
#%%
fig = plt.figure(figsize=(10,5))
userdf.zip.value_counts().sort_values(inplace=False,ascending=False).head(20).plot(kind='bar')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off')         # ticks along the top edge are off) # labels along the bottom edge are off
plt.ylabel("Count")
plt.xlabel("Locations")
plt.title("Top 20 Locations")
#%%

#Sign-up Date
#%%
#Convert to timeseries
userdf['SignDate'] = pd.to_datetime(userdf['SignDate'])
ts = pd.DataFrame(index=userdf['SignDate'],columns=['CustID'])
ts['CustID'] = list(userdf['CustID'])
ts2 = pd.DataFrame(index=userdf['SignDate'],columns=['count'])
ts2['count'] = 1
#%%

#
#%%
#Year-by-year signup
temp = ts2.resample('A').sum()
temp2 = ts2.resample('M').sum()

fig = plt.figure(figsize=(10,5))
plt.plot(temp)
plt.plot(temp2,alpha=0.4,color='blue')
plt.title("Year-by-Year SignUps")


fig, ax1 = plt.subplots(sharex=True, figsize=(10,5))
plt.title("Sign-ups over time")
ax1.plot(temp)
ax1.set_xlabel('time (year)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('yearly sign-ups', color='black')
# ax1.tick_params(temp['count'], colors='black')

ax2 = ax1.twinx()
ax2.plot(temp2,color='red',alpha=0.6)
ax2.set_ylabel('monthly sign-ups', color='red')
# ax2.tick_params(temp2['count'], colors='black')

fig.tight_layout()
plt.show()
#%%
# Sign-up per day of the week
#%%
temp = ts2.groupby(ts2.index.dayofweek).sum()

fig = plt.figure(figsize=(10,5))
plt.bar(temp.index,list(temp['count']),color='b',alpha=0.4)
plt.title("Sign-up per day-of-week")
plt.xticks([i for i in range(7)],["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
plt.xlabel("Day of the Week")
plt.ylabel("Count")
#%%

#%%
temp = ts2.groupby(ts2.index.month).sum()

fig = plt.figure(figsize=(10,5))
plt.bar(temp.index,list(temp['count']),color='purple',alpha=0.4)
plt.title("Sign-up per month")
plt.xticks([i+1 for i in range(0,12)],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
plt.xlabel("Month")
plt.ylabel("Count")
#%%











































