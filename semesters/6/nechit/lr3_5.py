# Нормальный закон распределения

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#x-axis ranges from -5 and 5 with .001 steps
x = np.arange (-5, 5, 0.001)
print('x=', x)

#define multiple normal distributions
plt.plot (x, norm.pdf (x, 0, 1), label='μ: 0, σ: 1', color='gold') 
plt.plot (x, norm.pdf (x, 0, 1.5), label='μ:0, σ: 1.5', color='red') 
plt.plot (x, norm.pdf (x, 0, 2), label='μ:0, σ: 2', color='pink')

#add legend to plot 
plt.legend(title='Parameters')

#add axes labels and a title 
plt.ylabel('Density')
plt.xlabel('x')
plt.title('Normal Distributions', fontsize= 14 ) 
plt.show()