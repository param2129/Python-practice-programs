f1=open("abc","r")
u=0
l=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        u=u+1
    if ch.islower():
        l=l+1
f1.close()
print("Upper =",u)
print("Lower =",l)