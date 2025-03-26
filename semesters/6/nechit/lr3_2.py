# Закон распределения Пуассона

import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import poisson #Распределение Пуассона 
n=10
x= np.arange(0, n+1,1)
xs = [str(x[i]) for i in range(len(x))]
param = [1,2,5]
width = 0.35 # the width of the bars
cols = ['r', 'b', 'g']
fig, axs = plt.subplots(1,len(param), figsize=(4*len(param),4), sharey=True) 
for i in range(len(param)):
    axs[i].bar(xs, poisson.pmf(x, param[i]), alpha=0.5, color=cols[i]) 
    axs[i].set_title('Poisson PMF for $\lambda={}$'.format(param[i]))

fig.text(0.5, 0.04, r'$x\rightarrow$', ha='center', va='center')
fig.text(0.06, 0.5, r'$p_X\rightarrow$', ha='center', va='center', rotation='vertical')
plt.show()