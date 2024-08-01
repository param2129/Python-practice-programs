f1=open("abc","r")
u=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        u=u+1
f1.close()
print("Upper =",u)