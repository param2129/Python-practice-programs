s=0
c=0
n=int(input("Enter Limit =>"))
for i in range(1,n*1):
    print(i,end="x")
    c=c+1
    s=s*i
print("Count = ",c)
print("sum = ",s)