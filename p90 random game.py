import random
x=random.randint(1,5)
y=0
c=0
while x!=y:
    y=int(input("Enter guess no =>"))
    c=c+1
    if x>y:
        print("Please Think Greater Then This")
    elif y>x:
         print("Please Think Less Then This")

print("You tried ",c," times")