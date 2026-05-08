# PLINKO #
"""Plinko game - bet an amount of money and see how much you win."""
# cd ~/Desktop/Python #python3 PLINKO.py - To run it in terminal

import random
import time

# FUNCTIONS


def board_builder(n):
    """Build a board with n number of rows."""
    board = []
    # Appends lists into 2D list
    # 3 columns in first row to n+3 columns in the last row
    for i in range(3, n+3):
        row = ["."] * i
        board.append(row)
    # Return the board so that we can use it to create the gameboard later
    return board


def print_board(board, current_row, current_location):
    """Print out the board."""
    # Gives space above the board so we can see it clearly
    print("\n" * 100)
    max_row_length = len(" ".join(board[-1]))

    #
    for row in range(len(board)):
        row_copy = board[row][:]
        if row == current_row:
            # Place ball instead of item in the current location
            row_copy[current_location] = "@"

        #  Join the items in the current list with a space between them
        row_string = " ".join(row_copy)

        # Add necessary leading spaces so board looks like a pyramid
        # Center length of last row so all other rows above it look centered
        print(row_string.center(max_row_length))
    # Pause so we can see each step
    time.sleep(0.3)


def calculate_path(board):
    """Simulate the path of a ball falling through the board with the

    help of the random module and returns the final landing column."""
    # Start at the middle of the first row
    current_col = len(board[0]) // 2

    # Simulate the drop through each row
    for i in range(len(board)):
        #  50/50 bounce off a peg
        direction = random.randint(0, 1)

        # In pyramid where each row is 1 wider:
        # Staying at the same index = moving left
        # Adding 1 to index = moving right
        if direction == 1:
            current_col += 1

        #Stop the ball going outside the board
        if current_col < 0:
            current_col = 0
        elif current_col >= len(board[i]):
            current_col = len(board[i]) - 1

        # Bounds check BEFORE printing
        print_board(board, i, current_col)  

    return current_col



def calculate_money_earned(game_board, slot, current_money, money_bet):
    """Calculate the money won by the user based on the balls distance from the center slot and returns winnings."""
    center = len(game_board[-1]) // 2
    distance = abs(slot - center) # Absolute value so that we can find the distance from the center
    #Edges (Big Win)
    if distance > center - center//4: 
        multiplier = 3
        print("JACKPOT! You landed in slot {}.".format(slot,))
    #Mid range
    elif distance >= center - center//.8 and distance <= center - center//4:
        multiplier = 1.5
        print("Nice drop! Landed in slot {}. ".format(slot))
    #Center
    else:
        multiplier = 0.2
        print("Ouch, center drop. Landed in slot {}.".format(slot))
    winnings = money_bet * multiplier

    # Calculate winnings
    if winnings > money_bet:
        print("You have won ${}".format(winnings))
    elif winnings < money_bet:
        print("You have lost ${}".format(money_bet - winnings))

    return winnings


def check_marketing_status(profile):
    """Check if the player is a "Whale" or not."""
    if profile["lifetime_losses"] > 500:
        profile["target_ads"] = True
        print("VIP message")
    else:
        print("Keep playing to climb the leaderboard!")


## MAIN CODE ##
if __name__ == "__main__":
    # Player will start with a certain amount of betting money
    money = 400
    # Build a board of 12 rows
    game_board = board_builder(12)
    print("WELCOME TO PLINKO")
    # Ask for name and location so we can use it in the dictionary
    # geeksforgeeks.org is where I learned how to input in dictionaries
    player_profile = {"name": input("Enter your name: "), "location": input("Enter your location: "), "high_score": 0, "lifetime_losses": 0, "target_ads": False}
    play_again = "yes"

    # Loop for game to run while user wants to play and user has money
    while play_again in ["yes", "y"] and money > 0:
        print("You have ${} to bet".format(money))

        # Loop for user to enter valid betting amount
        while True:
            try:
                betting_money = int(input("How much would you like to bet? "))
                # Expected value
                if betting_money > 0 and money - betting_money >= 0: 
                    money -= betting_money
                    player_profile["lifetime_losses"] += betting_money
                    break

                # User has entered an amount above the current money value or below the minimum betting amount(value has to be > 0)
                else:
                    print("Invalid bet amount") 
            # User hasn't entered a number
            except ValueError:
                print("Please enter a valid number") 

        # Get the final landing slot
        final_slot = calculate_path(game_board)
        # Calculate money earned using the calculate_money_earned function
        winnings = calculate_money_earned(game_board, final_slot, money, betting_money)
        money += winnings
        if money > player_profile["high_score"]:
            print("You beat your highscore of: ${} with your score of: ${}! Great job!".format(player_profile["high_score"], money))
            player_profile["high_score"] = money
        print("You have ${}.".format(money))
        check_marketing_status(player_profile)

        # Check if user wants to play again
        while True:
            play_again = input("Would you like to go again? (Y/N) or (Yes/No) ").lower()
            if play_again == "y" or play_again == "yes":
                break
            elif play_again == "n" or play_again == "no":
                print("Thanks for playing!")
                break
            # If user hasn't entered 'y','yes', or 'n' then keeps asking until user types expected answer
            else:
                print("Please enter: (Y/N) or (Yes/No)")
