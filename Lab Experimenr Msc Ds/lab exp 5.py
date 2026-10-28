#Study Python memory references shallow copy & deep copy
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]  

import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)     

b.append([5, 6])     
b[0].append(99)       

print(a)  
print(b)  

import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(99)

print(a)  
print(b)  