import random
l1=[]
l2=[]
l3=[]
n=int(input("Enter Value =>"))
for i in range(1,n+1):
    y=random.randint(1,100)
    l1.append(y)
print(l1)
y=int(input("Enter Limit =>"))
for x in l1:
    if x>y:
     l2.append(x)

print(l2)
