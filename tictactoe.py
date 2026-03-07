#FIRST MILESTONE PROJECT IN UDEMY: CREATING AN INTERACTIVE TICTACTOE GAME.
"""
Rules:
1) Two players should be able to play the game.
2) The board should be printed out after every move.
3) You should be able to accept the input of the player position and then place a symbol on the board.
"""
#Function that attributes X and O to each of the players:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
player1_symbol = ""
player2_symbol = ""

grid = [1,2,3,4,5,6,7,8,9]                                                                #Assigning the grid.

def players():
    result = ""
    symbol = ["O","X"]

    while result not in symbol:                                                            #Asking the user to choose his symbol:
        result = input("Player 1: Do you want to be the O or X:")

    if result == "X":                                                                          #Assigning the symbol to each player:  
        player1_symbol = "X"
        player2_symbol = "O"
        print("Player 1 is X and Player 2 is O")
    elif result == "O":
        player1_symbol = "O"
        player2_symbol = "X"
        print("Player One is O and Player Two is X")
    
    return player1_symbol, player2_symbol

#Function that displays the grid:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def display():
    print(grid[0:3])
    print(grid[3:6])
    print(grid[6:9])

#Function that takes Player 1's move and modifies the board accordiingly:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def player_move(player1_symbol):
    while True:
        try:
            result = int(input("Choose your next position (1-9):"))
            if result not in range(1,10):
                print("That number is not in the required range.")
                continue
            elif grid[result-1] in ["X","O"]:
                print("That position is already taken.")
                continue
            grid[result-1] = player1_symbol
            break
        except ValueError:
            print("Please inout a number.")

#Function that detects if the game is finished:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#Function that asks the player if he wants to keep playing after the game is over:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def keep_playing():
    pass

#Executing the functions in order:
    player1_symbol, player2_symbol = players()
    display()
    player_move1(player1_symbol)
    display()
    player_move2(player2_symbol)
