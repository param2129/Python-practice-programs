Temp=int(input("Enter Temp=>"))
if Temp<0:
    print("Freszing atmosphere")
elif Temp<10:
    print("Very Cold Atmosphere")
elif Temp<20:
    print("Cold Atmosphere")
elif Temp<30:
    print("Normal Atmosphere")
elif Temp<40:
    print("Hot Atmosphere")
else:
    print("Very Hot")