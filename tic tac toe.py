l1=['_','_','_','_','_','_','_','_','_']
turn=1
while turn<10:
    if turn % 2==0:
        pos=int(input("Param Enter Your Position =>"))
        l1[pos-1]='X'
    else:
        pos=int(input("Kurunal Enter Your Position =>"))
        l1[pos - 1]='0'
    print("After Turn",turn)
    print(l1[0],'|',l1[1],'|',l1[2])
    print(l1[3],'|',l1[4],'|',l1[5])
    print(l1[6],'|',l1[7],'|',l1[8])
    turn+1
