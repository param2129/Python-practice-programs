f1=open("abc","r")
f2=open("pqr","w")
f3=open("xyz","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch== "a" or ch== "A" or ch== "e" or ch== "E" or ch== "i" or ch== "I" or ch== "o" or ch== "O" or ch== "u" or ch== "U":
          f2.write(ch)
    else:
      f3.write(ch)
f1.close()
f2.close()
f3.close()
print("copied")