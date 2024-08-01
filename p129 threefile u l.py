f1=open("abc","r")
f2=open("pqr","w")
f3=open("xyz","w")
u=0
l=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        u=u+1
        f2.write(ch)
    if ch.islower():
        l=l+1
        f3.write(ch)

f1.close()
f2.close()
f3.close()
print("copy")