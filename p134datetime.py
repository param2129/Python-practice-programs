import time
current=time.localtime(time.time())

h=current.tm_hour
if h<12:
    print("Good Morning")
elif h<16:
    print("Good Afternoon")
elif h<23.59:
    print("Good Evening")
else:
    print("Good night")