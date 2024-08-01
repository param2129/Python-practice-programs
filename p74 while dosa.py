p1=0
p2=0
while True:
    print("Press pizza for pizza")
    print("press dosa for dosa")
    print("press E for exit")
    op=input("Enter input =>")
    if op=="pizza":
        quantity=int(input("Enter quantity =>"))
        p1=quantity*300
        print("Quantity => ",p1)
    elif op=="dosa":
        quantity=int(input("Enter quantity =>"))
        print("Quantity => ",p2)
        p2=quantity*250
    elif op=="e":
        total=p1+p2
        print("Total bill = ",total)
        break
    else:
        print("wrong opt")