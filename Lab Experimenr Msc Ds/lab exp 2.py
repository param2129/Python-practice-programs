# Exp = 2; Implement central tendencies using python data structures 
import numpy as pd 
import statistics as stats
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter element: ")))
print("Mean is:", pd.mean(l))
print("Median is:", pd.median(l))
print("mode is:", stats.mode(l))