from termcolor import colored, cprint

currentField = [[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " "]]

#To draw the playing Board
def drawField(field):
  for row in range(13):
    if row%2 == 0:
      practicalRow = int(row/2)
      for column in range(13):
        if column%2 == 0:
          practicalColumn = int(column/2)
          color = "yellow"
          if field[practicalColumn][practicalRow] == "X":
            color = "red"
          pawn = colored(field[practicalColumn][practicalRow], color, attrs=['bold'])
          if column != 12:
            print(pawn,end="")
          else:
            print(pawn)
        else:
          cprint("|",'green',end="")
    else:
      cprint("-------------",'green')


#To update the playing board with X or O starting at last empty row
def updateField(colNum,player):
  column = currentField[colNum]
  indices = ""
  inverseCol = column[::-1]
  for row in inverseCol:
    if row == " ":
      indices = inverseCol.index(row)
      if player == 1:
        inverseCol[indices] = "X"
        break
      else:
        inverseCol[indices] = "O"
        break
  if indices == "":
    return False
  column = inverseCol[::-1]
  currentField[colNum] = column
  drawField(currentField)
  return True

#To check if there is four in a row
def fourInRow():
  winner = False
  for column in currentField:
    counter = 0
    length = len(column)
    for i in range(1, length): #1 - 6
      if column[i - 1] != " " and column[i] != " " and column[i - 1 ] == column[i]:
        counter += 1
      else:
        counter = 0
      if counter == 3:
        winner = column[i - 1]
        return winner    
  return winner

#To check if there is four in a column
def fourInColumn(colMesh):
  winner = False
  for column in colMesh:
    counter = 0
    length = len(column)
    for i in range(1, length): #1 - 6
      if column[i - 1] != " " and column[i] != " " and column[i - 1 ] == column[i]:
        counter += 1
      else:
        counter = 0
      if counter == 3:
        winner = column[i - 1]
        return winner    
  return winner

#To check if there is four in Diagonal
def fourInFwdDiagonal(colMesh, player):
  for i in range(0, len(colMesh)):
    for j in range(0, len(colMesh[i])):
      try:
        if colMesh[i][j] == player and colMesh[i + 1][j - 1] == player and colMesh[1 + 2][j - 2] == player and colMesh[i + 3][j - 3] == player:
          return True
      except IndexError:
        next
  return False

#To check if there is four in Diagonal
def fourInBwdDiagonal(colMesh, player):
  for i in range(0, len(colMesh)):
    for j in range(0, len(colMesh[i])):
      try:
        if colMesh[i][j] == player and colMesh[i + 1][j + 1] == player and colMesh[1 + 2][j + 2] == player and colMesh[i + 3][j + 3] == player:
          return True
      except IndexError:
        next
  return False

#Create a Mesh that maps with our Columns in currentField
def createColMesh():
  colMesh = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "]]
  for i in range(7): #0 - 6
        for j in range(len(currentField[i])): #0 - 6
            colMesh[j][i] = currentField[i][j]

  return colMesh


#To check if the user input the correct number
def correctMove(ColNo):
  if ColNo >=1 and ColNo <=7:
    return True
  else:
    return False


def startGame():
  Player = 1
  noWinner = True
  winner = ""
  while(noWinner):
      askUser = input(f"Player {Player} turn, Please select a column from 1 - 7: ")
      ColNumber = askUser
      if ColNumber:
        ColNumber = int(askUser)
        if correctMove(ColNumber) == False:
          print("Error: Please select a number from 1-7")
        else:
          updateInfo = updateField(ColNumber -1, Player)
          if updateInfo:
            print("")
            actualPlayer = Player
            if Player == 1:
              pawn = "X"
              Player = 2
            else:
              pawn = "O"
              Player = 1
            winner = fourInRow()
            if winner:
              noWinner = False
            else:
              colMesh = createColMesh()
              winner = fourInColumn(colMesh)
              if winner:
                noWinner = False
              elif fourInBwdDiagonal(colMesh, pawn):
                winner = actualPlayer
                noWinner = False
              elif fourInFwdDiagonal(colMesh, pawn):
                winner = actualPlayer
                noWinner = False
          else:
            print("It's not the right move")
      else:
        print("Please do the correct move")
  if winner == "X":
    winner = "1"
    cprint(f"The Winner is PLAYER {winner}",'cyan', attrs=['bold'])
  else:
    winner = "2"
    cprint(f"The Winner is PLAYER {winner}",'cyan', attrs=['bold'])


print("New Game Starting...\n")

drawField(currentField)
startGame()

