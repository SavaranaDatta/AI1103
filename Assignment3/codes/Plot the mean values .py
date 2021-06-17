# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18bWXrtT0ZvZOE-EKPeCAflvoQQ443CaF
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

#Calculated from the probability  density function
mean_of_sample = 0.25
stdev_of_sample =0.19364916
target1 = 0.125 
target2=0.375

#generating 10,000 samples having 15 values in each
mean_of_sample + np.random.normal()*stdev_of_sample
surveys = np.zeros((10000,15))
for i in range(surveys.shape[0]):
    for j in range(surveys.shape[1]):
        surveys[i,j] = mean_of_sample + np.random.normal()*stdev_of_sample


# Histogram that shows the distribution for the mean of all surveys
fig, ax = plt.subplots(figsize=(8,8))
sns.distplot(np.mean(surveys,axis=1), 
             kde=False, label='Mean Value')

ax.set_xlabel("Mean of the randomly selected 15 samples",fontsize=16)
ax.set_ylabel("Frequency",fontsize=16)
plt.axvline(target1, color='red')
plt.axvline(target2, color='red')
plt.legend()
plt.tight_layout()