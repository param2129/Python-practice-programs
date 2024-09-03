l1=['_','_','_','_','_','_','_','_','_']
turn=1
while turn<10:
    if turn % 2==0:
        pos=int(input("P1 Enter For param =>"))
        if l1[pos-1]=='_':
            l1[pos-1]='X'
        else:
            print("Already Exist")
            turn=turn-1
    else:
        pos = int(input("P2 Enter For mmihir =>"))
        if l1[pos-1]=='_':
            l1[pos-1]='0'
        else:
            print("Already Exist")
            turn=turn-1
    print("After turn",turn)
    print(l1[0],'|',l1[1],'|',l1[2])
    print(l1[3],'|',l1[4],'|',l1[5])
    print(l1[6],'|',l1[7],'|',l1[8])
    turn+=1

    if l1[0]==l1[1]==l1[2]:
        if l1[0]=='0':
            print("Winner is P1")
            turn=11
        elif l1[0]=='X':
            print("Winner is p2")

    if l1[3]==l1[4]==l1[5]:
        if l1[3]=='0':
            print("Winner is P1")
            turn=11
        elif l1[3]=='X':
            print("Winner is p2")

    if l1[6]==l1[7]==l1[8]:
        if l1[6]=='0':
            print("Winner is P1")
            turn=11
        elif l1[6]=='X':
            print("Winner is p2")

    if l1[0]==l1[3]==l1[6]:
        if l1[0]=='0':
            print("Winner is P1")
            turn=11
        elif l1[0]=='X':
            print("Winner is p2")

    if l1[1]==l1[4]==l1[7]:
        if l1[1]=='0':
            print("Winner is P1")
            turn=11
        elif l1[1]=='X':
            print("Winner is p2")

    if l1[2]==l1[5]==l1[8]:
        if l1[2]=='0':
            print("Winner is P1")
            turn=11
        elif l1[2]=='X':
            print("Winner is p2")

    if l1[0]==l1[4]==l1[8]:
        if l1[0]=='0':
            print("Winner is P1")
            turn=11
        elif l1[0]=='X':
            print("Winner is p2")

    if l1[2]==l1[4]==l1[6]:
        if l1[2]=='0':
            print("Winner is P1")
            turn=11
        elif l1[2]=='X':
            print("Winner is p2")