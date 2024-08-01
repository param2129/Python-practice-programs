s1=0
s2=0
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    if i % 2 ==0:
        print(i*i, end="+")
        s1=s1+i*i
    else:
        print(i*i*i, end="+")
        s2=s2+i*i*i
print("\ncount = ",s1)
print("sum = ",s2)
