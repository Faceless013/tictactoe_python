#FIRST MILESTONE PROJECT IN UDEMY: CREATING AN INTERACTIVE TICTACTOE GAME.
"""
Rules:
1) Two players should be able to play the game.
2) The board should be printed out after every move.
3) You should be able to accept the input of the player position and then place a symbol on the board.
"""

grid = [1,2,3,4,5,6,7,8,9]                                                               

def players():
    while True:
        result = int(input("Player 1: Do you want to be O or X"))
        if result in ("O","X"):
            if result == "X":
                print("Player 1 is X and Player 2 is O")
            else:
                print("Player 1 is O and Player 2 is X")
        else:
            print("Please choose either X or O")

def display(grid):
    print(grid[0:3])
    print(grid[3:6])
    print(grid[6:9])


def player_move(grid, symbol):
    while True:
        try:
            result = int(input(f"Player {symbol}, choose your next position (1-9):"))
            if result not in range(1,10):
                print("That number is not in the required range.")
                continue
            elif grid[result-1] in ["X","O"]:
                print("That position is already taken.")
                continue
            grid[result-1] = symbol
            break
        except ValueError:
            print("Please input a number.")

def finished(grid, symbol):
    winning_list = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
)
    for (a,b,c) in winning_list:
        if grid[a] == grid[b] == grid[c] == symbol:
            return True   
    return False

def keep_playing():
    while finished == True:
        input("Do you want to keep playing ? ")

def run_game():   
    player1_symbol, player2_symbol = players()
    display()
    player_move(player1_symbol)
    display()

if __name__ == "__main__":
    run_game()
