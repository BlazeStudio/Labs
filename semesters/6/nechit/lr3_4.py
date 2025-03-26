# Показательный (экспоненциальный) закон распределения

import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import expon 
la = [0.2, 0.5, 1]
x = np.arange(0, expon.ppf(0.99, scale = 1/min(la)), 0.01)
fig, ax = plt.subplots(1,2,figsize=(4.8*2,4), sharey=True)
for i in range(len(la)):
    rv = expon(scale = 1/la[i])
    ax[0].plot(x, rv.pdf(x), alpha=0.5, label='Expo$(\lambda={})$'.format(la[i]))
    ax[1].plot(x, rv.cdf(x), alpha=0.5)
    ax[0].set_title('PDF of Exponential') 
    ax[1].set_title('CDF of Exponential') 
    ax[1].grid()
    ax[0].legend(bbox_to_anchor=(2.2, 1.0), loc='upper left')

fig.text(0.5, 0.04, r'$x\rightarrow$', ha='center', va='center')
fig.text(0.08, 0.5, r'$f_X\rightarrow$', ha='center', va='center', rotation='vertical') 
fig.text(0.52, 0.5, r'$F_X\rightarrow$', ha='center', va='center', rotation='vertical') 
plt.show()