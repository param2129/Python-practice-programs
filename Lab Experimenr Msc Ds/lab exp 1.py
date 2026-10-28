#Exp = 1; Find median of set of data without using built-in function sort() & median()
l=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    ele=int(input("Enter element: "))
    l.append(ele)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]


print("The sorted list in ascending order is:", l)
print("median of the list is:")
if n%2==0:
    print((l[n//2]+l[n//2-1])/2)
else:
    print(l[n//2])
