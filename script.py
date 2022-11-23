#All rows in board, represented as a list of cells that can have values [' '], ['X'] or ['O']. row1 represents top row row6 represents bottom. Board will be drawn based on list items.

row1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
row2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
row3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
row4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
row5 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
row6 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

#Board represented as list of row variables.

board = [row1, row2, row3, row4, row5, row6]

#Function drawBoard() is defined.

def drawBoard():
  #Prints the column labels
  print('  1   2   3   4   5   6   7')
  #Draws board row by row.
  for row in board:
    #rowstr cleared each row so correct data is parsed.
    rowstr = ''
    #rowstr made equal to string of what row will be printed as, using parsed row data.
    rowstr = '| ' + row[0] + ' | ' + row[1] + ' | ' + row[2] + ' | ' + row[3] + ' | ' + row[4] + ' | ' + row[5] + ' | ' + row[6] + ' |'
    #Bottom border of row drawn
    print('+---+---+---+---+---+---+---+')
    print(rowstr)
  #Bottom border of board.
  print('+---+---+---+---+---+---+---+')

#GameLogic defined - runs round code when all cells aren't occupied and gameOver state is False. When they're not program terminates.
def gameLogic():
  #gameOver variable, when True game ends.
  gameOver = False
  #OccupiedCells variable, the number of cells on the board occupied.
  oCells = 0
  #String representation of counter pieces. Iterates between 'X' and 'O' each round.
  counterState = 'X'
  #Following code loops each round.
  while gameOver is False and oCells < 42:
    boardChecksum = row1 + row2 + row3 + row4 + row5 + row6
    #Board is drawn each round to show new pieces.
    drawBoard()

    #Validation function, 1st checks if input is an integer then if input is in correct range for board. Loops until input is acceptable.

    passState = False
    while passState == False:
      uInput = input('Which column do you want to place your piece on?\n')
      intChk = False

      try:
        int(uInput)
      except:
        print('Column must be a number 1-7.')
        intChk = True
    
      if intChk == False:
        if uInput == '':
          print('Input cannot be empty.')
        elif int(uInput) < 1 or int(uInput) > 7:
          print('Input out of range 1-7.')
        else:
          print('Placing piece...')
          passState = True

    piecePlace(uInput, counterState)
    boardChecksum2 = row1 + row2 + row3 + row4 + row5 + row6
    #If board at start of round matches board after input, don't update occupiedCells, else update oCells.
    if boardChecksum == boardChecksum2:
        oCells = oCells
    else:
        oCells += 1
    #Code to switch counters each round.
    if counterState == 'X':
        counterState = 'O'
    else:
        counterState =  'X'

    #Win checks  - win only possible after 7 goes so will only be executed once occupiedCells variable reaches 7 (on 7th go.). Before 7th round this code is skipped and loop restarts for next round.
    if oCells >= 7:

      #Horizontal win checks.

      for row in board:
        rowPos = 0
        if row[rowPos] != ' ' and row[rowPos] == row[rowPos + 1] and row[rowPos] == row[rowPos + 2] and row[rowPos] == row[rowPos + 3]:
          cWinner = row[rowPos]
          print(cWinner + ' has won the game!')
          gameOver = True
        elif row[rowPos + 1] != ' ' and row[rowPos + 1] == row[rowPos + 2] and row[rowPos + 1] == row[rowPos + 3] and row[rowPos + 1] == row[rowPos + 4]:
          cWinner = row[rowPos + 1]
          print(cWinner + ' has won the game!')
          gameOver = True
        elif row[rowPos + 2] != ' ' and row[rowPos + 2] == row[rowPos + 3] and row[rowPos + 2] == row[rowPos + 4] and row[rowPos + 2] == row[rowPos + 5]:
          cWinner = row[rowPos + 2]
          print(cWinner + ' has won the game!')
          gameOver = True
        elif row[rowPos + 3] != ' ' and row[rowPos + 3] == row[rowPos + 4] and row[rowPos + 3] == row[rowPos + 5] and row[rowPos + 3] == row[rowPos + 6]:
          cWinner = row[rowPos + 3]
          print(cWinner + ' has won the game!')
          gameOver = True

      #Vertical and diagonal win checks.    

      aCounter = 0

      for i in row1:
        if i != ' ' and i == row2[aCounter] and i == row3[aCounter] and i == row4[aCounter]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter < 3 and i == row2[aCounter + 1] and i == row3[aCounter + 2] and i == row4[aCounter + 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter == 3 and i == row2[aCounter + 1] and i == row3[aCounter + 2] and i == row4[aCounter + 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter == 3 and i == row2[aCounter - 1] and i == row3[aCounter - 2] and i == row4[aCounter - 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter > 3 and i == row2[aCounter - 1] and i == row3[aCounter - 2] and i == row4[aCounter - 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        else:
          aCounter += 1
      
      aCounter = 0

      for i in row2:
        if i != ' ' and i == row3[aCounter] and i == row4[aCounter] and i == row5[aCounter]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter < 3 and i == row3[aCounter + 1] and i == row4[aCounter + 2] and i == row5[aCounter + 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter == 3 and i == row3[aCounter + 1] and i == row4[aCounter + 2] and i == row5[aCounter + 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter == 3 and i == row3[aCounter - 1] and i == row4[aCounter - 2] and i == row5[aCounter - 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter > 3 and i == row3[aCounter - 1] and i == row4[aCounter - 2] and i == row5[aCounter - 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        else:
          aCounter += 1

      aCounter = 0

      for i in row3:
        if i != ' ' and i == row4[aCounter] and i == row5[aCounter] and i == row6[aCounter]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter < 3 and i == row4[aCounter + 1] and i == row5[aCounter + 2] and i == row6[aCounter + 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter == 3 and i == row4[aCounter + 1] and i == row5[aCounter + 2] and i == row6[aCounter + 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif  i != ' ' and aCounter == 3 and i == row4[aCounter - 1] and i == row5[aCounter - 2] and i == row6[aCounter - 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        elif i != ' ' and aCounter > 3 and i == row4[aCounter - 1] and i == row5[aCounter - 2] and i == row6[aCounter - 3]:
          cWinner = i
          print(cWinner + ' has won the game!')
          gameOver = True
        else:
          aCounter += 1




#Function for calculating where to draw piece after column is selected. Finds lowest unoccupied cell in desired column & places 'X' there. Also checks if column is full and redraws board with new piece in. uInput will need to be requested before this function is called.

def piecePlace(uInput, counterState):
  if int(uInput) < 1 or int(uInput) > 7:
    print('Error! Userinput greater than 7 or less than 1 but validity didnt detect, exiting... ps. check validity code ant!!!')
  elif row6[int(uInput) - 1] != ' ' and row5[int(uInput) - 1] != ' ' and row4[int(uInput) - 1] != ' ' and row3[int(uInput) - 1] != ' ' and row2[int(uInput) - 1] != ' ' and row1[int(uInput) - 1] != ' ':
    print('Column full! Please try another.\n')
  elif row6[int(uInput) - 1] != ' ' and row5[int(uInput) - 1] != ' ' and row4[int(uInput) - 1] != ' ' and row3[int(uInput) - 1] != ' ' and row2[int(uInput) - 1] != ' ':
    row1[int(uInput) - 1] = counterState
    drawBoard()
  elif row6[int(uInput) - 1] != ' ' and row5[int(uInput) - 1] != ' ' and row4[int(uInput) - 1] != ' ' and row3[int(uInput) - 1] != ' ':
    row2[int(uInput) - 1] = counterState
    drawBoard()
  elif row6[int(uInput) - 1] != ' ' and row5[int(uInput) - 1] != ' ' and row4[int(uInput) - 1] != ' ':
    row3[int(uInput) - 1] = counterState
    drawBoard()
  elif row6[int(uInput) - 1] != ' ' and row5[int(uInput) - 1] != ' ':
    row4[int(uInput) - 1] = counterState
    drawBoard()
  elif row6[int(uInput) - 1] != ' ':
    row5[int(uInput) - 1] = counterState
    drawBoard()
  else:
    row6[int(uInput) - 1] = counterState
    drawBoard()

#Main Game Code:

#Welcome messages.
print('Connect 4!')
print('Welcome! This is Python Connect 4 by Anton.')
print('X goes first!')

gameLogic()

print('Game Over! Hope you had fun!')

#PlayAgain functionality, doesn't work atm...
#Presents player play again dialouge when False
# while oCells == 42 or gameOver == True:
#   pAgainPass = False
#   while pAgainPass == False:
#     pAgain = input('Would you like to play again y/n:\n')
#     if pAgain == 'y'.upper() or pAgain == 'y':
#       row1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
#       row2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
#       row3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
#       row4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
#       row5 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
#       row6 = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
#       pAgainPass = True
#       gameLogic()
#     elif pAgain == 'n'.upper() or pAgain == 'n':
#       print('Thanks for playing!')
#       pAgainPass = True
#     else:
#       print('Please use y/n for input only.')