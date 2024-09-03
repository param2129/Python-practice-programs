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
        d1 = random.randint(1, 6)
        print("Player 1, your dice rolls:", d1)
        p1 = p1 + d1
        print("Now Player 1 is at position", p1)

        if p1 in snake1:
            print("In Snake p1 ",p1)
            p1 = snake2[snake1.index(p1)]
            print("Snake bites! Now Player 1 is on", p1)
        elif p1 in ladder1:
            print("In ladder p1 ",p1)
            p1 = ladder2[ladder1.index(p1)]
            print("Hurray! Ladder! Now Player 1 is on", p1)
    else:
        d2 = random.randint(1, 6)
        print("Player 2, your dice rolls:", d2)
        p2 = p2 + d2
        print("Now Player 2 is at position", p2)

        if p2 in snake1:
            print("In Snake p2 ",p2)
            p2 = snake2[snake1.index(p2)]
            print("Snake bites! Now Player 2 is on", p2)
        elif p2 in ladder1:
            print("In Ladder p2 ",p2)
            p2 = ladder2[ladder1.index(p2)]
            print("Hurray! Ladder! Now Player 2 is on", p2)

    input("Press Enter to play")
    turn = turn + 1

if p1 >= 101:
    print("Player 1 is the winner!")
elif p2 >= 101:
    print("Player 2 is the winner!")
