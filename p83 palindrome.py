no=int(input("Enter no = "))
y=0
x=no
while no>0:
    digit=no%10
    y=y*10+digit
    no=no//10
print(y)

if x==y:
    print("Palindrome")
else:
    print("Not palindrome")