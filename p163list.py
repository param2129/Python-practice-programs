L1=[14,15,60,7,8,9,16,3,45,49]
c1=0
c2=0
for x in L1:
    if x%2 ==0:
        print("The value is even:",x)
        c1=c1+1
    else:
        print("The value is odd:",x)
        c2=c2+1
print("Total Even =>",c1)
print("Total Odd =>",c2)