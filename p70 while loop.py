while True:
    print("Press 1 for square")
    print("Press 2 for cube")
    print("Press 3 for exit")
    op = int(input("Enter opt =>"))
    if op == 1:
        no = int(input("Enter your number =>"))
        print("Square = ", no * no)
    elif op == 2:
        no = int(input("Enter your number =>"))
        print("Cube = ", no * no * no)
    elif op == 3:
        break
    else:
        print("Wrong opt")