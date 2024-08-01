import random

l1=[]
n=int(input("Enter Value =>"))
for i in range(1,n+1):
    y=random.randint(1,50)
    l1.append(y)
print(l1)
p1=(l1[0])
p2=(l1[-1])

print(p1+p2)