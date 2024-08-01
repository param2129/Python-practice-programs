import random
x=random.randint(1,50)
#print(x)
y=0
c=0
while x!=y:
    y=int(input("Enter guess no =>"))
    c=c+1

print("You tried ",c," times")