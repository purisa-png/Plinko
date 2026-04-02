##PLINKO##
import random
#FUNCTIONS
# Function to create board
board = []
def board_builder(n):
    for i in range(5,n):
        row = ["E"]*i
        board.append(row)
    return board

 
     
#Function to calculate the balls path
def calculate_path(board):
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
            
        # Make sure the ball doesn't go out of bounds
        current_col = max(0, min(current_col, len(board[i+1]) - 1))
            
    return current_col
    


## MAIN CODE ##
if __name__ == "__main__":
#Player will start with a certain amount of betting money
    money = 400
    print("WELCOME TO PLINKO")

    play_again = "yes"

    while play_again == "yes" and money > 0:

        print("You have ${} to bet".format(money))
        betting_money = int(input("How much would you like to bet? "))
        money -= betting_money

        # Build a board of 12 rows
        game_board = board_builder(12)
        
        # Get the final landing slot
        final_slot = calculate_path(game_board)

        #Drop ball into the middle column of the first row (so that it hits the first peg)
        current_col = len(board[0]) // 2

        #If direction = left(0) then column stays same, if direction = right(1) column +1

        for i in range(len(board)):     
            direction = random.randint(0,1)
    
            if direction == 0:
                current_col -= 2
            else:
                current_col += 1
    
            display_row = list(board[i])

        #Stop the ball going outside the board
            if current_col < 0:
                current_col = 0
            if current_col >= len(display_row):
                current_col = len(display_row) - 1





        #See how much money the user has won/lost based on distance from center
        center = len(game_board[-1]) // 2
        distance = abs(final_slot - center)
        
        if distance > 4: #Edges (Big Win)
            winnings = beting_money * 3
            print("JACKPOT! You landed in slot {}. Won ${}!".format(final_slot,winnings))
        elif distance > 2: #Mid range
            winnings = betting_money * 1.5
            print("Nice drop! Landed in slot {}. Won ${}!".format(final_slot,winnings))
        else: #Center (House edge)
            winnings = betting_money * 0.2
            print("Ouch, center drop. Landed in slot {}. Retained ${}.".format(final_slot,winnings))

        money = money + winnings

        print("You now have ${}".format(money))

        play_again = input("Would you like to go again? ").lower()
