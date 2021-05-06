##################### Password Generator using the Str & random library ######################################
from termcolor import colored, cprint
import random as r
import string as s

pwdLength = int(input("How long you want your password? "))
pwdValues = int(input("""With letters / Digits / Symbol press 1 : 
Only Digits and letters press 2 :\n"""))

#Using the string library to get all my letters/Digits/punctuation in 3 variable
pwdChar = s.ascii_letters + s.digits + s.punctuation
pwdDigitChar = s.digits + s.ascii_letters

#An empty list to save my Str character per element10
pwd = []

for i in range(pwdLength):
  if pwdValues == 1:
    #If the user press 1 append a char in the empty list
    pwd.append(r.choice(pwdChar))#Randomly choosing a Char in the pwdChar Str
  elif pwdValues == 2:
    #If the user press 2, only append Digit and letters
    pwd.append(r.choice(pwdDigitChar))
  else:
    print("Please select either 1 or 2")
    break

#Shuffle the list before displaying the password
r.shuffle(pwd)

#Print the list in a single String
final_pwd = colored(''.join(pwd), 'cyan', attrs=['bold'])
print(f"Your password is: {final_pwd}")
