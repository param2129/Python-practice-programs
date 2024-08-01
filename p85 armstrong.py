no=int(input("Enter no = "))
y=0
x=no
while no>0:
    digit=no%10
    y=y+digit**3
    no=no//10
print(y)
if x==y:
    print("Armstrong")
else:
    print("Not Armstrong")