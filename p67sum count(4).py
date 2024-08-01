c=0
s=0
n=int(input("Enter Limit =>"))
for i in range(1,n+1):
    print(i*i,end="x")
    c=c+1
    s=s+i*i
print("Cout = ",c)
print("sum = ",s)
