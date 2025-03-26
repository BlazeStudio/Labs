
'''Предположим, в классе 100 учеников, и в одном из тестов по математике средняя оценка mean = 78, а стандартное отклонение std_dev = 25
Код Python для определения процента студентов, получивших менее 60 баллов scipy.stats.norm() — это обычная непрерывная случайная величина.'''
from scipy.stats import norm
import numpy as np
# Given information 
mean = 78
std_dev = 25
total_students = 100 
score = 60
# Calculate z-score for 60
z_score = (score - mean) / std_dev
# Calculate the probability of getting a score less than 60 
prob = norm.cdf(z_score) 
# #Cumulative Distribution Function
# Calculate the percentage of students who got less than 60 marks 
percent = prob* 100
# Print the result
print("Percentage of students who got less than 60 marks:", round(percent, 2), "%")