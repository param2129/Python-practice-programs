b1=0
b2=0
while True:
    print("Press 1 for xerox")
    print("press 2 for type")
    print("Press 3 for exit")
    op=int(input("Enter your input =>"))
    if op==1:
        quantity1=int(input("Enter quantity1 =>"))
        if quantity1>50:
            b1=quantity1*3
            print("per page 3 rupees",b1)

        elif quantity1<50:
            b1=quantity1*5
            print("per page 5 rupees",quantity1*5)

    elif op==2:
        quantity2=int(input("Enter quantity2 =>"))
        if quantity2>50:
            b2=quantity2*15
            print("per page 15 rupees",quantity2*15)

        elif quantity2<50:
            b2=quantity2*20
            print("per page 20 rupees and bill ",quantity2*20)
    elif op==3:
        total=b1+b2
        print("total bill = ",total)
        break
    else:
        print("Wrong opt")
     