no=int(input("Enter Your number =>"))
y=0
while no>0:
    digit=no%10
    y=y*10+digit
    no=no//10
print(y)