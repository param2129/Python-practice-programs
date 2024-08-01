n=int(input("Enter Number =>"))
i=n
s=1
while i>=1:
    print(i, end="x")
    s = s * i
    i=i-1
print("\n = ", s)
