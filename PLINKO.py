##PLINKO##
# Possible positions- Peg or empty space
# Number of Pegs(P), Number of Empty spaces (E)  , | E = P-1
#Make the empty list for the board
board = []

#For each row in the board add pegs * row number
for i in range(3,10):
    row = ["P"] * i
    


#For each row, add an "E" in the gap
    #Gaps are all the odd numbers Eg. Row 1 has "E" in place 1 and 3, Row 2 has "E" in 1,3 and 5, etc
    
    j = 1  # between first and second "P"
    while j < len(row):
        row.insert(j, "E")
        j += 2  # add it to the next odd place
    board.append(row)
print(board)

#Time to add the ball now



 

    

