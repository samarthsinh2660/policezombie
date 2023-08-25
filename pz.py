import random

# Define the game board
board = [[' ' for i in range(10)] for j in range(10)]

# Place the player in the center of the board
player_x = 5
player_y = 5
board[player_x][player_y] = 'P'

# Place the zombies randomly on the board
num_zombies = 10
for i in range(num_zombies):
    zombie_x = random.randint(0, 9)
    zombie_y = random.randint(0, 9)
    while board[zombie_x][zombie_y] != ' ':
        zombie_x = random.randint(0, 9)
        zombie_y = random.randint(0, 9)
    board[zombie_x][zombie_y] = 'Z'

# Define the function to print the game board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Main game loop
while True:

    # Display the game board
    print_board(board)

    # Get the player's move
    move = input("Enter your move (w, a, s, d): ")

    # Update the player's position
    if move == 'w':
        player_y -= 1
    elif move == 'a':
        player_x -= 1
    elif move == 's':
        player_y += 1
    elif move == 'd':
        player_x += 1

    # Check if the player has won
    if board[player_x][player_y] == 'Z':
        print("You lose!")
        break

    # Check if the player has lost
    if player_x < 0 or player_x > 9 or player_y < 0 or player_y > 9:
        print("You lose!")
        break

    # Update the board
    board[player_x][player_y] = 'P'

    # Move the zombies
    for i in range(num_zombies):
        zombie_x = random.randint 