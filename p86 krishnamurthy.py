import math

no=int(input("Enter no = "))
y=0
x=no
while no>0:
    digit=no%10
    y=y+math.factorial(digit)
    no=no//10
print(y)
if x==y:
    print("The numbers is krishnamurthy")
else:
    print("The number is not krishnamurthy")