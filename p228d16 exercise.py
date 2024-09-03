import random
from colorama import Fore, Style, init
c1=0
c2=0
init()
d1={}
n=int(input("Enter limit => "))
for i in range(1,n+1):
    k=i
    v=random.randint(1,50)
    d1[k]=v
    if v>16:
        print(k,v,"=>",Fore.GREEN+"Pass!"+Style.RESET_ALL)
    else:
        print(k,v,"=>",Fore.RED+"Fail!"+Style.RESET_ALL)

