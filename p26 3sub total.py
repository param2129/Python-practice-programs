hindi=int(input("enter your marks =>"))
english=int(input("enter your marks =>"))
maths=int(input("enter your marks =>"))

total=hindi+english+maths

print("total",total)

if total<50:
    print("grade is c")
elif total<100:
    print("grade is b")
else:
    print("grade a")