print("press c for area of circle")
print("press @ for area of traingle")
op=input("enter opt =>")
if op=="c" or op=="C":
    r = int(input("enter your radius =>"))
    print("addition = ",3.14*r*r)
elif op=="@":
    h = int(input("enter your number1 =>"))
    b = int(input("enter your number1 =>"))
    print("triangle = ",h*b*0.5)
else:
    print("wrong opt")