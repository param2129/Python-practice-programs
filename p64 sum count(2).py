s1=0
c1=0
s2=0
c2=0
n=int(input("Enter Limit =>"))
for i in range(1,n+1):
    if i % 2 ==0:
        print(i,"Number id even")
        c1=c1+1
        s1=s1+i
    else:
        print(i,"Number id odd")
        c2=c2+1
        s2=s2+i
print("count of even = ",c1)
print("sum if even = ",s1)
print("count of odd = ",c2)
print("sum of odd = ",s2)