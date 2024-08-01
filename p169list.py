import random
L1=[]
n=int(input("Enter Value =>"))

for i in range(1,n+1):

    y=random.randint(1,50)
    L1.append(y)

print(L1)

for x in L1:
    if x % 2 == 0:
        print("T")
    else:
        print("odd:",x)