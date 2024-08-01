import random
x=random.randint(1,50)
y=random.randint(1,50)
print("No1=",x," No2=",y)
z=x+y
add=int(input("Enter addition =>"))
if add==z:
    print("The Value Is Correct")
else:
    print("The Value Is Not Correct")

