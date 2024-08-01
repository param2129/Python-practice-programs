import time
current=time.localtime(time.time())

y=current.tm_year

print(y,":")

if y%4==0:
    print("This year is not leap year")
else:
    print("This year is leap year")