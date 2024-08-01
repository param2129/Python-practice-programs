list1=["P","A","R","a","m","B","H","A","t","t"]
list2=[]

for x in list1:
    if x.isupper():
        list2.append(x.lower())
    elif x.islower():
        list2.append(x.upper())
print(list1)
print(list2)