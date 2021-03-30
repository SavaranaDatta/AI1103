# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MvL2cDVFvemUakNtr4kvN9nfOVnEAzAn
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

# generating random values of probabilities p an q
p_r = np.random.random(1)
q_r = np.random.random(1)
# simulation length 
simlen = 100000
#generating data for assembly of computers where '1' represents assembles computer is NOT faulty
data_bern_p = bernoulli.rvs(size=simlen,p=(1-p_r))
#generatind data for testing computers where '1' represents testing gives correct result
data_bern_q = bernoulli.rvs(size=simlen,p=q_r)
#addind the two arrays
out = np.add(data_bern_p,data_bern_q) # '1' represents the computer is declared as faulty
#calculating number of computers which are declared as faulty
counts = np.count_nonzero(out == 1)
#calculating  simulated probability of computers being declared as faulty
p_sim = counts/simlen
#calculating theoritical probability of computers being declared as faulty
p_thr = (p_r)*(q_r)+(1-p_r)*(1-q_r)

#plotting
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
t_vs_s = ['thr', 'sim' ]
prob = [p_thr,p_sim]
ax.bar(t_vs_s,prob)
plt.show()
#value of p=0.2724825 q=0.68752064
print(p_r)
print(q_r)
print(data_bern_p)
print(data_bern_q)
print(out)
print(counts)
print(p_sim)
print(p_thr)