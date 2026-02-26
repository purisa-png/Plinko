##PLINKO##
#Make the empty list for the board
board = []
#Add the rest of rows to the list
for i in range (16):
    board.append([i]) 

# Add the gaps to the list
#(code will check each nested list and add 2 + the first nested list number to that list
print(board)
for row_number in board: #For each list in the board
     row_number.insert(1, row_number+2) #Insert (2+the row number) in the 2nd place of that list
print(board)
