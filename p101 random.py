import random
c1=0
c2=0
for i in range(1,6):
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    option=random.randint(1,4)

    print("No1=", x, " No2=", y)

    if option==1:
        op="+"
    elif option==2:
        op="-"
    elif option==3:
        op="*"
    elif option==4:
        op="/"

    if op=="+":
        z = x + y
        add = int(input("Enter addition =>"))
        if add == z:
            c1=c1+1
            print("The Value Is Correct")
        else:
            c2 = c2 + 1
            print("The Value Is Not Correct")

    elif op=="-":

        z = x - y
        add = int(input("Enter Subtraction =>"))
        if add == z:
            c1 = c1 + 1
            print("The Value Is Correct")
        else:
            c2 = c2 + 1
            print("The Value Is Not Correct")

    elif op=="*":

        z = x * y
        add = int(input("Enter Multiplication =>"))
        if add == z:
            c1 = c1 + 1
            print("The Value Is Correct")
        else:
            c2 = c2 + 1
            print("The Value Is Not Correct")

    elif op=="/":

        z = x / y
        add = int(input("Enter Division =>"))
        if add == z:
            c1 = c1 + 1
            print("The Value Is Correct")
        else:
            c2 = c2 + 1
            print("The Value Is Not Correct")

    else:
        print("Wrong Option")

print("Right Answer",c1)
print("Wrong Answer",c2)