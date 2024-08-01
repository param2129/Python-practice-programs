import random

list1=[]
list2=[]
n=int(input("Enter Value =>"))
for i in range(1,n+1):
    y=random.randint(97,122)
    ch=chr(y)
    list1.append(ch)

for x in list1:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        list2.append(x)

for x in list2:
    if x in list1:
        list1.remove(x)
        
print(list1)
print(list2)