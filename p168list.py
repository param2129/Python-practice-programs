import random
l1=[]
l2=[]
n=int(input("Enter Value =>"))
for i in range(1,n+1):
    y=random.randint(-1,50)
    l1.append(y)
print(l1)
for x in l1:
     l2.append(-x)
print(l2)
