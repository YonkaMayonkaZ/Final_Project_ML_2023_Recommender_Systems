# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:19:02 2024

@author: DaNi
"""

### Installing pyspark
!pip install pyspark

#%%
from numpy import array
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
#%%

#%%
sc = SparkSession.builder.config("spark.executor.memory", "2g").appName("Clustering").getOrCreate()
spark = sc.sparkContext
#%%

#%%
# Load and parse the data
data = spark.textFile('subset1.csv')
data.take(2)
#%%

#%%
# Extract header
header = data.first()

# Broadcast the header variable
header_broadcast = spark.broadcast(header)

# Filter out the header from the data
data = data.filter(lambda row: row != header)

# Now you can proceed with your clustering analysis using 'data'
print("Length of uncleaned data -", data.count())
#%%

#%%
#Filter the data
data3 = data.filter(lambda x: len(x[1]) == 1 )
data3.count()

#%%

#%%
sc.stop()
#%%
