list = ["P","A","R","a","m","B","H","A","t","t"]
u=0
l=0
for x in list:
    if x.isupper():
        x.islower()
        u=u+1
    elif x.islower():
        x.isupper()
        l=l+1

print("Upper =",u)
print("Lower =",l)