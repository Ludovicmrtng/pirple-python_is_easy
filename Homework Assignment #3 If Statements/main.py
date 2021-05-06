#It's a function to describe how much money I can withdraw

BankAc = "4000"
Savings = "10000"
WithDraw = "Pending"

if int(BankAc) < 5000 and int(Savings) < 8000:
  WithDraw = "None"
elif int(BankAc) == 5000 or int(Savings) >= 8000:
  WithDraw = int(Savings) - int(BankAc)
else:
  WithDraw = int(Savings) + int(BankAc)

print(WithDraw)
