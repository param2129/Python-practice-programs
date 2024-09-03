import random 

snake1 = [98, 95, 93, 87, 62, 64, 54, 17]
snake2 = [79, 75, 73, 36, 19, 60, 34, 7]

ladder1 = [1, 4, 9, 21, 28, 51, 72, 80]
ladder2 = [38, 14, 31, 42, 84, 67, 91, 98]

p1 = 0
p2 = 0
turn = 1

while p1 < 100 and p2 < 100:
    if turn % 2 == 0:
        d1 = random.randint(1 , 6)
        print("Your dice rolls = ", d1)
        p1 = p1 + d1
        print("Player Your Position is at = ", p1) 
    
        if p1 in snake1:
            print("In snake p1 ", p1)
            p1 = snake2[snake1.index(p1)]   
            print("Ohh!! snake bites now player1 is at = ", p1)

        elif p1 in ladder1:
            print("In ladder p1 ", p1)
            p1 = ladder2[ladder1.index(p1)]
            print("Yeah!! You Got Ladder now player1 is at ", p1)
    
    else:
        if p2 in snake1:
            print("In snake p1 ", p2)
            p2 = snake2[snake1.index(p2)]   
            print("Ohh!! snake bites now player1 is at = ", p2)

        elif p2 in ladder1:
            print("In ladder p1 ", p2)
            p2 = ladder2[ladder1.index(p2)]
            print("Yeah!! You Got Ladder now player1 is at ", p2)
            

    input("Press Enter to play!")
    turn = turn + 1

if p1 >= 100:
    print("Player1 is the winner!!")

elif p2 >= 100:
    print("Player2 is the winner!!")
 