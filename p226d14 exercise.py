import random
d1={}
n=int(input("Enter limit =>"))

for i in range(1,n+1):
    k=i
    v=random.randint(1,50)
    d1[k]=v
    if v>16:
        print(k,v,"=>","Pass!")
    else:
        print(k,v,"=>","Fail!")

for key,value in d1.items():
    print()
