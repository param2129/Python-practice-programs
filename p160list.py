import random

l1=[]
l2=[]
l3=[]
n=int(input("Enter Value =>"))

for i in range(1,n+1):
    y=random.randint(-10,50)
    l1.append(y)
print(l1)
for x in l1:
    if x<0:
     l2.append(x)
    else:
     l3.append(x)
print(l2)
print(l3)
