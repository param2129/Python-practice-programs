while True:
    print("Press 1 for Addition")
    print("Press 2 for Substraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("press 5 for exit")
    op=int(input("Enter opt =>"))
    if op==1:
        no1=int(input("Enter your number1 =>"))
        no2= int(input("Enter your number2 =>"))
        print("Addition = ",no1+no2)
    elif op==2:
        no1=int(input("Enter your number1 =>"))
        no2=int(input("Enter your number2 =>"))
        print("Substraction = ",no1-no2)
    elif op==3:
        no1=int(input("Enter your number1 =>"))
        no2=int(input("Enter your number2 =>"))
        print("Multiplication = ",no1*no2)
    elif op==4:
        no1=int(input("Enter your number1 =>"))
        no2=int(input("Enter your number2 =>"))
        print("Division = ",no1/no2)
    elif op==5:
        break
    else:
        print("Wrong opt")