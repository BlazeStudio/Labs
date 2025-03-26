# Нормальный закон распределения(отображение функции распределения и плотости вероятности на одном графике)


from scipy.stats import norm 
"""Совместим обе функции cdf pdf на одном графике."""
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize= (14,10)) # зададим размер графика
mean, std=180, 10 # определим среднее значение и СКО
# зададим функции pdf и cdf на оси х
x=np.linspace(mean - 3 * std, mean + 3 * std, 1000)
# при этом возникает проблема: по оси у них разный масштаб 
y1=norm.pdf(x, mean, std) #probability density function
y2=norm.cdf(x, mean, std) #Cumulative Distribution Function
# эту проблему можно решить через функции subplots() и twinx()
fig, ax_left = plt.subplots(nrows = 1, ncols = 1, figsize = (12,8)) # создадим сетку из одной ячейки 
ax_right=ax_left.twinx() # создадим новую ось с правой стороны
# на оси х и левой оси у построим график функции плотности (pdf)
ax_left.plot(x, y1, label = 'P(x)')
# на оси х и правой оси у построим график функции распределения (cdf)
ax_right.plot(x, y2, color = 'orange', label = 'D(x)')
# также построим вертикальную прямую и точку
ax_left.vlines(x = 180, ymin = 0, ymax = 0.040, linewidth = 1, color = 'r', linestyles = '--')
ax_left.plot(180, 0.020, marker = 'o', markersize = 5, markeredgecolor = 'r', markerfacecolor = 'r') 
fig.legend(loc='upper right', # из-за двух осей с легендой придется повозиться
    bbox_to_anchor = (1,1),
    bbox_transform=ax_right.transAxes,
    prop={'size': 15})
plt.show()