#------ Library -----------
import random as r
import string as s
from worddict import wordList
from getpass import getpass

#-------------------- Drawing Hangman picture ----------
class drawHangman:
  def __init__(self):
    return

  def drawLifeNine(self):
    print("9 lives left!!")
    print("==============")
  
  def drawLifeEight(self):
    print("8 lives left!!")
    print("==============")
    print("       o      ")
  
  def drawLifeSeven(self):
    print("7 lives left!!")
    print("==============")
    print("       o      ")
    print("       |      ")
  
  def drawLifeSix(self):
    print("6 lives left!!")
    print("==============")
    print("       o      ")
    print("       |      ")
    print("      /       ")
  
  def drawLifeFive(self):
    print("5 lives left!!")
    print("==============")
    print("       o      ")
    print("       |      ")
    print("      / \     ")
  
  def drawLifeFour(self):
    print("4 lives left!!")
    print("==============")
    print("      \o      ")
    print("       |      ")
    print("      / \     ")
  
  def drawLifeThree(self):
    print("3 lives left!!")
    print("==============")
    print("      \o/     ")
    print("       |      ")
    print("      / \     ")
  
  def drawLifeTwo(self):
    print("2 lives left!!")
    print("==============")
    print("      \o/ |   ")
    print("       |      ")
    print("      / \     ")
  
  def drawLifeOne(self):
    print("1 live left!! Last chance!")
    print("==============")
    print("      \o/_|   ")
    print("       |      ")
    print("      / \     ")
  
  def drawNoLife(self):
    print("==============")
    print("       o_|    ")
    print("      /|\     ")
    print("      / \     ")

#---------1-player mode hangman game ---------------------
def onePlayerMode():
  word = r.choice(wordList)
  lives = 10
  guessmade = ''
  validLetter = set(s.ascii_lowercase)
  hangmanimg = drawHangman()
  
  while len(word)>0:
    mainWord = ""

    for letter in word:
      if letter in guessmade:
        mainWord += letter
      else:
        mainWord += "_ "
    
    if mainWord == word:
      print("You guess the correct word",mainWord)
      print("You win!!!")
      break

    print("guess the word ", mainWord)
    guess = input()

    if guess in validLetter:
      guessmade += guess
    else:
      print("enter valid character")
      guess = input()
    
    if guess not in word:
      lives -= 1

      if lives == 9:
        hangmanimg.drawLifeNine()
      if lives == 8:
        hangmanimg.drawLifeEight()
      if lives == 7:
        hangmanimg.drawLifeSeven()
      if lives == 6:
        hangmanimg.drawLifeSix()
      if lives == 5:
        hangmanimg.drawLifeFive()
      if lives == 4:
        hangmanimg.drawLifeFour()
      if lives == 3:
        hangmanimg.drawLifeThree()
      if lives == 2:
        hangmanimg.drawLifeTwo()
      if lives == 1:
        hangmanimg.drawLifeOne()
      if lives == 0:
        print("GamerOver! Hangman die")
        print(f"The word is {word}")
        hangmanimg.drawNoLife()
        break

#---------------2-player mode game-----------------
def twoPlayerMode():
  playerWord = []
  playerOne = getpass("Player 1, Please write a word: ") #Using the getpass method to hide the user input
  print("Player 2, Guess the word, Good Luck!")
  print("-----------------------------------------")
  playerWord.append(playerOne) #Append the word to playerTwo list
  word = r.choice(playerWord) #The word that player 2 has written and append to lust playerTwo
  lives = 10
  guessmade = '' #This will take dashes or the valid letter from user input variable guess
  validLetter = set(s.ascii_lowercase) #Create a set of letters which is valid, user cannot input apart from multiple letter
  hangmanimg = drawHangman()
  
  while len(word)>0:
    mainWord = ""

    for letter in word:
      if letter in guessmade:
        mainWord += letter
      else:
        mainWord += "_ "
    
    if mainWord == word:
      print("You guess the correct word",mainWord)
      print("You win!!!")
      break

    print("guess the word ", mainWord)
    guess = input()

    if guess in validLetter:
      guessmade += guess
    else:
      print("enter valid character")
      guess = input()
    
    if guess not in word: # if the user input is not the variable word then the lives -1
      lives -= 1
      #Calling hangman Drawing method
      if lives == 9:
        hangmanimg.drawLifeNine()
      if lives == 8:
        hangmanimg.drawLifeEight()
      if lives == 7:
        hangmanimg.drawLifeSeven()
      if lives == 6:
        hangmanimg.drawLifeSix()
      if lives == 5:
        hangmanimg.drawLifeFive()
      if lives == 4:
        hangmanimg.drawLifeFour()
      if lives == 3:
        hangmanimg.drawLifeThree()
      if lives == 2:
        hangmanimg.drawLifeTwo()
      if lives == 1:
        hangmanimg.drawLifeOne()
      if lives == 0:
        print("GamerOver! Hangman die")
        print(f"The word is {word}")
        hangmanimg.drawNoLife()
        break
    
name = input("Enter your name to start the game: ")
print(f"Welcome to Hangman Game {name}")
mode = int(input("""Press 1 for 1-player mode: 
Press 2 for 2-player mode \n"""))

#Choosing what mode will the player play

if mode == 1:
  print("You have choosen the 1-player mode")
  print("You have 10 lives")
  print("----------------------------------")
  print("Hint: All words is about techs and programming, Good Luck!!")
  print("----------------------------------")
  onePlayerMode()
elif mode == 2:
  print("You have choosen the 2-player mode")
  print("You have 10 lives, You have to guess the player 1 word, Good Luck!")
  twoPlayerMode()
else:
  new_mode = int(input("Please choose 1 or 2: "))
  mode = new_mode
  if mode == 1:
    print("You have choosen the 1-player mode")
    print("You have 10 lives")
    print("----------------------------------")
    print("Hint: All words is about techs and programming, Good Luck!!")
    print("----------------------------------")
    onePlayerMode()
  elif mode == 2:
    print("You have choosen the 2-player mode")
    print("You have 10 lives, You have to guess the player 1 word, Good Luck!")
    twoPlayerMode()