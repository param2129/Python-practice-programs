s=0
n=int(input("Enter Limit =>"))
for i in range(n,0,-1):
    print(i,end="x")
    s=s+i
print("\nsum = ",s)