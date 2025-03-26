# Биномиальный закон распределения

import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import binom 
n=10
x = np.arange(0,n+1,1)
xs = [str(x[i]) for i in range(len(x))]
p=[0.3,0.5,0.7]
width = 0.35 # the width of the bars
cols = ['r', 'b', 'g']
fig, axs = plt.subplots(1, len(p), figsize=(3*len(p), 3), sharey=True)
for i in range(len(p)):
    axs[i].bar(xs, binom.pmf(x, n, p[i]), alpha=0.5, color=cols[i]) 
    axs[i].set_title('Bernoulli PMF for '+r'$p={}$'.format(p[i])) 
fig.text(0.5, 0.04, r'$x\rightarrow$', ha='center', va='center')
fig.text(0.06, 0.5, r'$p_X\rightarrow$', ha='center', va='center', rotation='vertical')
plt.show()