f1=open("abc","r")
c=0
while True:
    ch=f1.read(1).lower()
    if not ch:
        break
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        c=c+1
f1.close()
print("Count ",c)