no=int(input("Enter no = "))
y=0
x=no
while no>0:
    digit=no%10
    y=y+digit
    no=no//10
print(y)