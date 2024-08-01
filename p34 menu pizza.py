print("Press pizza for pizza")
print("dosa dosa for dosa")
op=input("Enter input =>")
if op=="pizza" or op=="PIZZA":
    quantity=int(input("Enter quantity =>"))
    print("Quantity => ",quantity*300)
elif op=="dosa" or op=="DOSA":
    quantity=int(input("Enter quantity =>"))
    print("Quantity => ",quantity*250)
else:
    print("wrong opt")