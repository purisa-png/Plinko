##PLINKO##
#cd ~/Desktop/Python #python3 PLINKO.py - To run it in terminal

import random
import time

#FUNCTIONS

# Function to create board
def board_builder(n): # n will be the number of rows
    """Builds a board with n number of rows"""
    #empty board
    board = []
    #appends lists into a 2d list, first list has 3 items with number of items in each list increasing by 1 until there are n lists
    for i in range(3,n+3): # n+3 is the number of columns in the last row
       row = ["."]*i
       board.append(row)
    return board # Return the board so that we can use it to create the gameboard later


#Function to print out the board (run it in terminal for best results)
def print_board(board,current_row,current_location):
    print("\n" * 100) # Gives space above the board so we can see it clearly
    max_row_length = len(" ".join(board[-1]))

    for row in range(len(board)):
        row_copy = board[row][:] 
        if row == current_row:
            row_copy[current_location] = "@" # Places ball instead of the item in the current location

        #  Join the items in the current list with a space between them
        row_string = " ".join(row_copy)
        
        # Add the necessary leading spaces so that the board looks like a pyramid
        # Center the length of the last row so that all the other rows above it look centered
        print(row_string.center(max_row_length))
    time.sleep(0.3) # Pause so we can see each step

        
    
#Function to calculate the balls path
def calculate_path(board):
    """Simulates the path of a ball falling through the board with the
help of the random module and returns the final landing column"""
    # Start at the middle of the first row
    current_col = len(board[0]) // 2
    
    # Simulate the drop through each row
  
    for i in range(len(board)):
        #  50/50 bounce off a peg
        direction = random.randint(0, 1)

        
        #In pyramid where each row is 1 wider:
        #staying at the same index = moving left
        #adding 1 to index = moving right
        if direction == 1:
            current_col += 1
        
        
        #Stop the ball going outside the board
        if current_col < 0:
            current_col = 0
        elif current_col >= len(board[i]):
            current_col = len(board[i]) - 1

        print_board(board, i, current_col)  # Bounds check BEFORE printing

            
    return current_col

#Function to calculate the money earned
def calculate_money_earned(game_board, slot,current_money,money_bet):
    """Calculates the money won by the user based on the balls distance from the center slot and returns winnings"""
    center = len(game_board[-1]) // 2
    distance = abs(slot - center) # Absolute value so that we can find the distance from the center

       
    if distance > 5: #Edges (Big Win)
        multiplier = 3
        print("JACKPOT! You landed in slot {}.".format(slot,))
    elif distance >= 2 and distance <= 5: #Mid range
        multiplier = 1.5
        print("Nice drop! Landed in slot {}. ".format(slot))

    else: #Center
        multiplier = 0.2
        print("Ouch, center drop. Landed in slot {}.".format(slot))
    winnings = money_bet * multiplier

#Calculate winnings
    if winnings > money_bet:
        print("You have won ${}".format(winnings))
    elif winnings < money_bet:
        print("You have lost ${}".format(money_bet - winnings))


    return winnings

# Function that identifies whale
def check_marketing_status(profile):
    if profile["lifetime_losses"] > 500:
        profile["target_ads"] = True
        print("VIP message")
    else:
        print("Keep playing to climb the leaderboard!")




## MAIN CODE ##
if __name__ == "__main__":
#Player will start with a certain amount of betting money
    money = 400
    # Build a board of 12 rows
    game_board = board_builder(12)
    print("WELCOME TO PLINKO")
    #Ask for name and location so we can use it in the dictionary
    name = input("Enter your name: ")
    location = input("Enter your location: ")
    player_profile = {"name":name, "location":location, "high_score": 0, "lifetime_losses": 0, "target_ads": False}
    play_again = "yes"

# Loop for game to run while user wants to play and user has money
    while play_again in ["yes", "y"] and money > 0:

    
        print("You have ${} to bet".format(money))

    # Loop for user to enter valid betting amount
        while True:
            try:
                betting_money = int(input("How much would you like to bet? ")) #
                if betting_money > 0 and money - betting_money >= 0: #Expected value 
                    money -= betting_money
                    break
                
                else:
                    print("Invalid bet amount") #User has entered an amount above the current money value or below the minimum betting amount(value has to be > 0)
            except ValueError: 
                print("Please enter a valid number") # User hasn't entered a number

         # Get the final landing slot
        final_slot = calculate_path(game_board)
        # Calculate money earned using the calculate_money_earned function
        winnings = calculate_money_earned(game_board, final_slot,money,betting_money)
        loss_amount = betting_money - winnings
        if loss_amount > 0:
            player_profile["lifetime_losses"] += loss_amount
        money += winnings
        if money > player_profile["high_score"]:
            player_profile["high_score"] = money
        print("You have ${}.".format(money))
        check_marketing_status(player_profile)
            
        # Check if user wants to play again
        while True:
                play_again = input("Would you like to go again? (Y/N) or (Yes/No) ").lower()
                if play_again == "y" or play_again =="yes":
                    break
                elif play_again == "n" or play_again == "no":
                    print("Thanks for playing!")
                    break
                else: #If user hasn't entered 'y','yes', or 'n' then keeps asking until user types expected answer
                    print("Please enter: (Y/N) or (Yes/No)") 

