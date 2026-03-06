##PLINKO##
#Player will start with a certain amount of betting money
money = 400
import random
print("WELCOME TO PLINKO")
print("You have ${} to bet".format(money))
betting_money = int(input("How much would you like to bet? "))
money -= betting_money

# Possible positions- Peg or empty space
# Number of Pegs(P), Number of Empty spaces (E)  , | E = P-1
#Make the empty list for the board
board = []

#For each row in the board add pegs * row number
for i in range(3,17):
    row = ["P"] * i
    


#For each row, add an "E" in the gap
    #Gaps are all the odd numbers Eg. Row 1 has "E" in place 1 and 3, Row 2 has "E" in 1,3 and 5, etc
    
    j = 1  # between first and second "P"
    while j < len(row):
        row.insert(j, "E")
        j += 2  # add it to the next odd place
    board.append(row)


    


#Time to add the ball now
#Drop ball into the middle column of the first row (so that it hits the first peg)
current_col = 2

#If direction = left(0) then column stays same, if direction = right(1) column +1

for i in range(len(board)):
    direction = random.randint(0,1)
    if direction == 1:
        current_col += 1
    display_row = list(board[i])

#Print out pyramid
    if current_col < len(display_row):
        display_row[current_col] = "@"
    spaces = " " * (len(board) - i )
    row_string = "".join(display_row)
    print(spaces + row_string)


#See how much money the user has won/lost
if current_col < 3 or current_col > 12:
    betting_money = betting_money * 1.75
    print("You won {} money".format(betting_money - (betting_money * .75)))
elif current_col > 3 and current_col < 12:
    betting_money * 0.5
    print("You lost half of your money")

money = money + betting_money

    



   





    

