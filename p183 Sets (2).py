import random

n=int(input("Enter Your Limit =>"))
set2=set()

for i in range(1,n+1):
    y=random.randint(1,50)
    set2.add(y)
print(set2)