"""import random
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
"""

# visualization of the game

import random
import matplotlib.pyplot as plt
import pandas as pd


# Snake starting squares and ending squares
snake1 = [98, 95, 93, 87, 62, 64, 54, 17]
snake2 = [7, 75, 73, 36, 19, 60, 34, 7]

# Ladder starting squares and ending squares
ladder1 = [1, 4, 9, 21, 28, 51, 72, 80]
ladder2 = [38, 14, 31, 42, 84, 67, 91, 98]

# Starting positions
p1 = 0
p2 = 0
turn = 1

# Game analysis variables
total_turns = 0
p1_rolls = 0
p2_rolls = 0
snakes_used = 0
ladders_used = 0

# Lists for storing movement history
turn_numbers = []
player_names = []
roll_values = []
positions = []
events = []

# Interactive Matplotlib mode allows the board to change during the game.
plt.ion()

while p1 < 100 and p2 < 100:
    input("\nPress Enter to roll the dice...")

    # Roll the dice for the current player.
    dice = random.randint(1, 6)
    total_turns = total_turns + 1

    if turn == 1:
        player = "Player 1"
        p1_rolls = p1_rolls + 1
        old_position = p1
        new_position = p1 + dice
    else:
        player = "Player 2"
        p2_rolls = p2_rolls + 1
        old_position = p2
        new_position = p2 + dice

    event = "Normal move"

    # A player must land exactly on square 100.
    if new_position > 100:
        new_position = old_position
        event = "Needed an exact roll"

    # Check whether the player landed on a snake.
    if new_position in snake1:
        snake_number = snake1.index(new_position)
        snake_end = snake2[snake_number]
        new_position = snake_end
        snakes_used = snakes_used + 1
        event = "Snake: moved down"

    # Check whether the player landed on a ladder.
    elif new_position in ladder1:
        ladder_number = ladder1.index(new_position)
        ladder_end = ladder2[ladder_number]
        new_position = ladder_end
        ladders_used = ladders_used + 1
        event = "Ladder: moved up"

    # Save the new position.
    if turn == 1:
        p1 = new_position
    else:
        p2 = new_position

    turn_numbers.append(total_turns)
    player_names.append(player)
    roll_values.append(dice)
    positions.append(new_position)
    events.append(event)

    print(player, "rolled", dice)
    print(player, "moved from", old_position, "to", new_position)
    print("Event:", event)

    # Clear the previous board.
    plt.clf()

    # Draw the 100 board squares.
    for square in range(1, 101):
        row = (square - 1) // 10
        position_in_row = (square - 1) % 10

        # Every second row runs in the opposite direction.
        if row % 2 == 0:
            column = position_in_row
        else:
            column = 9 - position_in_row

        if square % 2 == 0:
            colour = "lightyellow"
        else:
            colour = "lightblue"

        plt.scatter(column, row, color=colour, s=850, edgecolors="black")
        plt.text(column, row, str(square), ha="center", va="center", fontsize=8)

    # Draw ladders in green.
    for number in range(len(ladder1)):
        start = ladder1[number]
        end = ladder2[number]

        start_row = (start - 1) // 10
        start_place = (start - 1) % 10
        end_row = (end - 1) // 10
        end_place = (end - 1) % 10

        if start_row % 2 == 0:
            start_column = start_place
        else:
            start_column = 9 - start_place

        if end_row % 2 == 0:
            end_column = end_place
        else:
            end_column = 9 - end_place

        plt.plot([start_column, end_column], [start_row, end_row],
                 color="green", linewidth=3)

    # Draw snakes in red.
    for number in range(len(snake1)):
        start = snake1[number]
        end = snake2[number]

        start_row = (start - 1) // 10
        start_place = (start - 1) % 10
        end_row = (end - 1) // 10
        end_place = (end - 1) % 10

        if start_row % 2 == 0:
            start_column = start_place
        else:
            start_column = 9 - start_place

        if end_row % 2 == 0:
            end_column = end_place
        else:
            end_column = 9 - end_place

        plt.plot([start_column, end_column], [start_row, end_row],
                 color="red", linewidth=3)

    # Find the coordinates for Player 1.
    if p1 == 0:
        p1_row = -1
        p1_column = -0.4
    else:
        p1_row = (p1 - 1) // 10
        p1_place = (p1 - 1) % 10
        if p1_row % 2 == 0:
            p1_column = p1_place - 0.15
        else:
            p1_column = 9 - p1_place - 0.15

    # Find the coordinates for Player 2.
    if p2 == 0:
        p2_row = -1
        p2_column = 0.4
    else:
        p2_row = (p2 - 1) // 10
        p2_place = (p2 - 1) % 10
        if p2_row % 2 == 0:
            p2_column = p2_place + 0.15
        else:
            p2_column = 9 - p2_place + 0.15

    # Draw the player tokens.
    plt.scatter(p1_column, p1_row, color="blue", s=300, label="Player 1")
    plt.scatter(p2_column, p2_row, color="purple", s=300, label="Player 2")

    plt.title("Snake and Ladders | {} rolled {} | {}".format(player, dice, event))
    plt.xlim(-1, 10)
    plt.ylim(-1, 10)
    plt.xticks([])
    plt.yticks([])
    plt.legend(loc="upper right")
    plt.pause(0.5)

    # Check for a winner.
    if p1 == 100 or p2 == 100:
        break

    # Change the turn.
    if turn == 1:
        turn = 2
    else:
        turn = 1


if p1 == 100:
    winner = "Player 1"
else:
    winner = "Player 2"

print("\n", winner, "is the winner!")

# Create a pandas table containing the complete game history.
game_history = pd.DataFrame({
    "Turn": turn_numbers,
    "Player": player_names,
    "Dice Roll": roll_values,
    "Position After Move": positions,
    "Event": events
})

print("\nCOMPLETE GAME HISTORY")
print(game_history.to_string(index=False))

# Create a pandas table containing final analysis.
analysis = pd.DataFrame({
    "Player": ["Player 1", "Player 2"],
    "Final Position": [p1, p2],
    "Number of Rolls": [p1_rolls, p2_rolls],
    "Winner": ["Yes" if winner == "Player 1" else "No",
               "Yes" if winner == "Player 2" else "No"]
})

print("\nGAME ANALYSIS")
print(analysis.to_string(index=False))
print("\nTotal turns:", total_turns)
print("Snakes used:", snakes_used)
print("Ladders used:", ladders_used)

# Keep the final board visible.
plt.ioff()
plt.show()

# Show a simple analytical chart after the board is closed.
analysis.plot(
    x="Player",
    y="Number of Rolls",
    kind="bar",
    color=["blue", "purple"],
    legend=False,
    title="Number of Dice Rolls per Player"
)
plt.ylabel("Number of rolls")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
    