import time
current=time.localtime(time.time())

h=current.tm_hour
if h==12.00:
    print("AM")
else:
    print("PM")