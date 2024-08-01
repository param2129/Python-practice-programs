price=300
quantity=int(input("Enter your quantity =>"))

total=price*quantity
print("total amount",total)

if total>1500:
    print("10% discount given")
    dis=total*0.10
    print("Discounted amount = ",dis)
    print("After discount bill = ",total-dis)
else:
    print("discount should not given")