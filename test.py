#!/usr/bin/env python
import numpy as np

def calculate_z_score(arr):
    mean = np.mean(arr)
    std_dev = np.std(arr)
    z_scores = [(s - mean) / std_dev for s in arr]
    return z_scores

gpa={
    'a':4.0,
    'a-':3.7,
    'b+':3.3,
    'b':3.0,
    'b-':2.7,
    'c+':2.3,
    'c':2.0,
    'c-':1.7,
    'd+':1.3,
    'd':1.0,
    'd-':0.7,
    'f':0
}

num = int(input("How many students took your course? : "))
print ("What was the grade for each student?: ")
convert = []

for i,n in enumerate(range(num)):
    mark=input(f'Student {i+1}: ').lower()
    try:
        convert.append(gpa[mark])
    except KeyError:
        convert.append(0)

result = calculate_z_score(convert)
print(result)