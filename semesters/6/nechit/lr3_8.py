'''Код Python для процента студентов, набравших более 70 баллов''' 
from scipy.stats import norm
#import numpy as np

#Given information 
mean = 78
std_dev = 25
total_students = 100
score = 70
# Calculate z-score for 70
z_score = (score - mean) / std_dev
# Calculate the probability of getting a less than 70
prob = norm.cdf(z_score) #¶унк распраделения - Сumulative Distribution Function 
print("Percentage of students who got less than 70 marks: ", round(prob* 100, 2),"%") 
# Calculate the percentage of students who got more than 70 marks
percent = (1-prob)* 100
# Print the result
print("Percentage of students who got more than 70 marks: ", round(percent, 2), "%")