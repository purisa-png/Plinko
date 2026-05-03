##PLINKO##
import random

#FUNCTIONS
# Function to create board

def board_builder(n):
    """Builds a board with n number of rows"""
    board = [] 
    for i in range(3,n+3):
       row = ["."]*i
       board.append(row)
    return board


def print_board(board):
    max_row_length = len(" ".join(board[-1]))

    for row in board:
        # 2. Join the "e"s in the current list with a space between them
        row_string = " ".join(row)
        
        # 3. Use .center() to add the necessary leading/trailing whitespace
        print(row_string.center(max_row_length))

        
    
        
     
#Function to calculate the balls path


def calculate_path(board):
    """Simulates the path of a ball falling through the board with the
help of the random module and returns the final landing column"""
    # Start at the middle of the first row
    current_col = len(board[0]) // 2
    
    # Simulate the drop through each row
    for i in range(len(board) - 1):
        #  50/50 bounce off a peg
        direction = random.randint(0, 1)

        
        #In pyramid where each row is 1 wider:
        #staying at the same index = moving left
        #adding 1 to index = moving right
        if direction == 1:
            current_col += 1
        
        #Stop the ball going outside the board
        #for row in board:
        #    if current_col < 0:
        #        current_col = 0
        #    elif current_col >= len(row):
        #        current_col = len(row) - 1
        if current_col < 0:
            current_col = 0
        elif current_col >= len(board[i+1]):
            current_col = len(board[i+1]) - 1
            
    return current_col


def calculate_money_earned(game_board, slot,current_money,money_bet):
    """Calculates the money won by the user based on the balls distance from the center slot and returns winnings"""
    center = len(game_board[-1]) // 2
    distance = abs(slot - center)
        
    if distance > 10: #Edges (Big Win)
        multiplier = 3
        print("JACKPOT! You landed in slot {}.".format(slot,))
    elif distance >= 3 and distance <= 10: #Mid range
        multiplier = 1.5
        print("Nice drop! Landed in slot {}. ".format(slot))

    else: #Center
        multiplier = 0.2
        print("Ouch, center drop. Landed in slot {}.".format(slot))
    winnings = money_bet * multiplier

    if winnings > money_bet:
        print("You have won ${}".format(winnings))
    elif winnings < money_bet:
        print("You have lost ${}".format(money_bet - winnings))


    return winnings



## MAIN CODE ##
if __name__ == "__main__":
#Player will start with a certain amount of betting money
    money = 400
    # Build a board of 12 rows
    game_board = board_builder(12)
    print("WELCOME TO PLINKO")

    play_again = "yes"

    print("Print the board")
    print_board(game_board)

    while play_again in ["yes", "y"] and money > 0:


        print("You have ${} to bet".format(money))
        while True:
            try:
                betting_money = int(input("How much would you like to bet? "))
                if betting_money > 0 and money - betting_money >= 0:
                    money -= betting_money
                    break
                
                
                else:
                    print("Invalid bet amount")
            except ValueError:
                print("Please enter a valid number")

         # Get the final landing slot
        final_slot = calculate_path(game_board)
        # Calculate money earned using the calculate_money_earned function
        winnings = calculate_money_earned(game_board, final_slot,money,betting_money)
        new_total = money+ winnings
        print("You have ${}.".format(new_total))
            


        play_again = input("Would you like to go again? ").lower()
