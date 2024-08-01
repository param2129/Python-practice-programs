import random

L1=[]
c1=0
c2=0
s1=0
s2=0
n=int(input("Enter Value =>"))

for i in range(1,n+1):
    y=random.randint(-10,50)
    L1.append(y)
print(L1)
for x in L1:
    if x<0:
        print("The value is Negative:",x)
        c1=c1+1
        s1=s1+x
    else:
        print("The value is positive:",x)
        c2=c2+1
        s2=s2+x

print("Total Negative =>",c1)
print("Total Positive =>",c2)
print("Sum of Negative =>",s1)
print("sum of Positive =>",s2)



