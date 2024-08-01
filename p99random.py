import random
c1=0
c2=0
for i in range(1,6):
    x=random.randint(1,50)
    y=random.randint(1,50)
    print("No1=",x," No2=",y)
    z=x+y
    add=int(input("Enter addition =>"))
    if add==z:
        c1=c1+1
        print("The Value Is Correct")
    else:
        c2=c2+1
        print("The Value Is Not Correct")

print("Right answers",c1)
print("Wrong answers",c2)