print("Press s for square")
print("Press c for cube")
op=input("Enter input =>")
if op=="s" or op=="S":
    r = int(input("enter your radius =>"))
    print("square = ",r*r)
elif op=="c" or op=="C":
    r = int(input("enter your number1 =>"))
    print("cube = ",r*r*r)
else:
    print("wrong opt")