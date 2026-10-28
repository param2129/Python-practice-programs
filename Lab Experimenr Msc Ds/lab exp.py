import numpy as np
ra=int(input("Enter the number of rows: "))
ca=int(input("Enter the number of columns: "))
l=[]
for i in range(ra*ca):
    element=int(input(f"Enter element [{i//ca}][{i%ca}]: "))
    l.append(element)
arr=np.array(l).reshape(ra,ca)
print("The array is:")
print(arr) 