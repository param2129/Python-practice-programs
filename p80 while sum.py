n=int(input("Enter Number =>"))
i=1
s=1
while i<=n:
    print(i, end="x")
    s = s * i
    i=i+1
print("\n = ", s)
