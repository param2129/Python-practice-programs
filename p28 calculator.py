print("Press 1 for Addition")
print("Press 2 for Substraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
op=int(input("Enter opt =>"))
if op==1:
    no1=int(input("Enter your number =>"))
    no2= int(input("Enter your number =>"))
    print("Addition = ",no1+no2)
elif op==2:
    no1=int(input("Enter your number =>"))
    no2=int(input("Enter your number =>"))
    print("Substraction = ",no1-no2)
elif op==3:
    no1=int(input("Enter your number =>"))
    no2=int(input("Enter your number =>"))
    print("Multiplication = ",no1*no2)
elif op==4:
    no1=int(input("Enter your number =>"))
    no2=int(input("Enter your number =>"))
    print("Division = ",no1/no2)
else:
    print("Wrong opt")