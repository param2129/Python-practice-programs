import time
current=time.localtime(time.time())

h=current.tm_hour
if h<12:
    print("Good Morning")   
else:
    print("Good night")