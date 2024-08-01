print("Press xerox for xerox")
print("press type for type")
print("Press both for both")
op=input("Enter your input =>")
if op=="xerox" or op=="XEROX":
    quantity=int(input("Enter quantity =>"))
    if quantity>50:
        print("per page 3 rupees",quantity*3)

    elif quantity<50:
        print("per page 5 rupees",quantity*5)

elif op=="type" or op=="TYPE":
    quantity=int(input("Enter quantity =>"))
    if quantity>50:
        print("per page 15 rupees",quantity*15)

    elif quantity<50:
        print("per page 20 rupees",quantity*20)

elif op=="both" or op=="BOTH":
    b1=0
    b2=0
    quantity1 = int(input("Enter quantity of xerox =>"))
    if quantity1 > 50:
        b1=quantity1*3
        print("per page 3 rupees", quantity1 * 3)
    elif quantity1 < 50:
        b1=quantity1*5
        print("per page 5 rupees", quantity1 * 5)

    quantity2= int(input("Enter quantity type =>"))
    if quantity2 > 50:
        b2=quantity2*15
        print("per page 15 rupees", quantity2 * 15)

    elif quantity2 < 50:
        b2=quantity2*20
        print("per page 20 rupees", quantity2 * 20)

    totalquantity=quantity1+quantity2
    totalamount=b1+b2

    print("totalquantity ",totalquantity)
    print("totalamount ",totalamount)
else:
    print("Wrong opt")
