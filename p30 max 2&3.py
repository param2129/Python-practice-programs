print("Press 1 for Max btw 2")
print("Press 2 for Max btw 3")
op=int(input("Enter opt =>"))
if op==1:
    no1=int(input("Enter your number =>"))
    no2=int(input("Enter your number =>"))
    if no1>no2:
        print("print no1 is greatr")
    else:
        print("no1 is not greater")
elif op==2:
    no1=int(input("Enter your number =>"))
    no2=int(input("Enter your number =>"))
    no3=int(input("Enter your number =>"))
    if no1>no2 and no1>no3:
      print("First value is greater")
    elif no2>no3 and no2>no1:
      print("Second value is greater")
    elif no3>no2 and no3>no1:
     print("Third value is greater")
    else:
      print("Value is equal")
