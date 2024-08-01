while True:
    print("Press + for Addition")
    print("Press - for Substraction")
    print("Press * for Multiplication")
    print("Press / for Division")
    print("Press E for exit")
    op=input("Enter opt =>")
    if op=="+":
        no1=int(input("Enter your number =>"))
        no2= int(input("Enter your number =>"))
        print("Addition = ",no1+no2)
    elif op=="-":
        no1=int(input("Enter your number =>"))
        no2=int(input("Enter your number =>"))
        print("Substraction = ",no1-no2)
    elif op=="*":
        no1=int(input("Enter your number =>"))
        no2=int(input("Enter your number =>"))
        print("Multiplication = ",no1*no2)
    elif op=="/":
        no1=int(input("Enter your number =>"))
        no2=int(input("Enter your number =>"))
        print("Division = ",no1/no2)
    elif op=="E":
         break
    else:
        print("Wrong opt")