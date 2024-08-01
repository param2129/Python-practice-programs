import random

L1=[]
c1=0
c2=0
s1=0
s2=0
n=int(input("Enter Value =>"))

for i in range(1,n+1):
    y=random.randint(1,50)
    L1.append(y)
print(L1)
for x in L1:
    if x % 2 == 0:
        print("The value is even:",x)
        c1=c1+1
        s1=s1+x
    else:
        print("The value is odd:",x)
        c2=c2+1
        s2=s2+x

print("Total Even =>",c1)
print("Total Odd =>",c2)
print("Sum of Even =>",s1)
print("sum of Odd =>",s2)



