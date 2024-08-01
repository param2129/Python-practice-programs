import random

list=[]
n=int(input("Enter Value =>"))
for i in range(1,n+1):
    y=random.randint(97,122)
    ch=chr(y)
    list.append(ch)

print(list)