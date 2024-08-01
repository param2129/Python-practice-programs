import random

x = random.randint(1, 50)
y = random.randint(1, 50)

print("No1=", x, " No2=", y)

print("Press + for Addition")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Division")

op=input("Enter Your Option =>")

if op=="+":
    z = x + y
    add = int(input("Enter addition =>"))
    if add == z:
        print("The Value Is Correct")
    else:
        print("The Value Is Not Correct")

elif op=="-":

    z = x - y
    add = int(input("Enter Subtraction =>"))
    if add == z:
        print("The Value Is Correct")
    else:
        print("The Value Is Not Correct")

elif op=="*":

    z = x * y
    add = int(input("Enter Multiplication =>"))
    if add == z:
        print("The Value Is Correct")
    else:
        print("The Value Is Not Correct")

elif op=="/":

    z = x / y
    add = int(input("Enter Division =>"))
    if add == z:
        print("The Value Is Correct")
    else:
        print("The Value Is Not Correct")

else:
    print("Wrong Option")