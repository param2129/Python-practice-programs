s=0
c=0
n=int(input("Enter Limit =>"))
for i in range(1,n+1):
    if i % 7 ==0:
        print(i)
        c=c+1
        s=s+i

print("Count = ",c)
print("sum = ",s)