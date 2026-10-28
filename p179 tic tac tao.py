"""l1=['_','_','_','_','_','_','_','_','_']
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
            print("Winner is p2")"""


# same program with class and methods


class TicTacToe:
    def __init__(self):
        # Attributes: information this game remembers
        self.board = ["_"] * 9
        self.current_player = "X"

    def show_board(self):
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print(self.board[6], "|", self.board[7], "|", self.board[8])

    def place_mark(self, position):
        # Convert the player's 1–9 choice to a list index from 0–8
        index = position - 1

        if self.board[index] != "_":
            print("Already occupied. Choose another square.")
            return False

        self.board[index] = self.current_player
        return True

    def check_winner(self):
        # Each group of three positions that could win
        winning_lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]

        for a, b, c in winning_lines:
            if self.board[a] != "_" and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]

        return None

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "0"
        else:
            self.current_player = "X"

    def play(self):
        while True:
            self.show_board()
            print(f"Player {self.current_player}'s turn")

            try:
                position = int(input("Choose a position from 1 to 9: "))
            except ValueError:
                print("Please enter a number.")
                continue

            if position < 1 or position > 9:
                print("Choose a number from 1 to 9.")
                continue

            # If the square is taken, retry the same player's turn
            if not self.place_mark(position):
                continue

            winner = self.check_winner()
            if winner:
                self.show_board()
                print(f"Player {winner} wins!")
                break

            if "_" not in self.board:
                self.show_board()
                print("It's a draw!")
                break

            self.switch_player()


# Create one game object and start it
game = TicTacToe()
game.play()