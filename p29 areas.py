print("Press 1 for Area of tringle")
print("Press 2 for Area of circle")
op=int(input("Enter opt =>"))
if op==1:
    h=int(input("Enter your number =>"))
    b=int(input("Enter your number =>"))
    print("Areaa of tringle = ",h*b*0.5)
elif op==2:
    r=int(input("Enter your number =>"))
    print("area of circle = ",3.14*r*r)
else:
    print("Wrong opt")