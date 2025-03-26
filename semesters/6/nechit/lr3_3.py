# Равномерный закон распределения

import matplotlib.pyplot as plt 
import numpy as np 
import random
import seaborn as sns
import datetime # подключаем модуль datetime
start=datetime.datetime.now() # фиксируем и выводим время старта работы кода
print('Время старта: '+ str(start))

rolls=[random.randrange(1, 7) for i in range(60000)]
"""Ключевой аргумент return_counts=True приказывает unique подсчитать количество вхождений каждого уникального значения. В данном случае unique
возвращает кортеж из двух одномерных коллекций ndarray, содержащих отсортированные уникальные значения и их частоты соответственно. Коллекции
ndarray из кортежа распаковываются в переменные values и frequencies.
Если аргумент return_counts равен False, то возвращается только список
уникальных значений"""
values, frequencies=np.unique(rolls, return_counts=True)
"""Форматная строка включает количество бросков кубика в заголовок гистограммы. Спецификатор «,» (запятая) в {len(rolls):,} 
выводит число с разделителями групп разрядов - таким образом, значение 60000 будет выведено в виде 60,000. """
title= f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style("whitegrid")
#строит диаграмму частот при помощи функции Seaborn barplot 
axes=sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency') #добавляет метки на оси

axes.set_ylim(top=max(frequencies)* 1.10) #Чтобы выделить место для текста
# над столбцами масштабирует ось у на 10%.
""" выводит значение частоты каждого столбца и процент от общего количества бросков Команда for использует функцию zip для перебора элементов patches и соответствующих им значений frequency. Каждая итерация распаковывает в bar и frequency
один из кортежей, возвращенных zip. """
for bar, frequency in zip(axes.patches, frequencies):
    """ вычисляет координату х центра области для вывода текста. Она вычисляется как сумма 
координаты х левого края столбца (bar.get_x()) и половины ширины столбца (bar.get_width() / 2.0) """
    text_x=bar.get_x()+bar.get_width()/2.0
    """ получает координату у области для вывода текста - значение bar.get_y() представляет верх столбца """
    text_y=bar.get_height()
    """ создает двустрочную строку, содержащую частоту этого
столбца и соответствующий процент от общего количества бросков"""
    text=f'{frequency:,}\n{frequency/len(rolls):.3%}'
    """ вызывает метод text объекта Аxes для вывода текста над столбцом.
Первые два аргумента метода задают позицию текста х-у,
а третий аргумент - выводимый текст. Ключевой аргумент һа задает горизонтальное выравнивание""" 
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
finish=datetime.datetime.now() #фиксируем и выводим время окончания работы кода
print('Время окончания: '+ str(finish))
print('Время работы: '+ str(finish - start)) # вычитаем время старта из времени окончания 
plt.show()