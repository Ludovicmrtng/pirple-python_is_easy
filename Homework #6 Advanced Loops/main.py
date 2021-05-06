#This is a function to draw a playing board in respect of width and length so that it don't wrap

def DrawBoard(rows, col):
  if rows <= 50 and col <= 50: #rows and columns fit into terminal without wrapping
    if rows%2 == 1 and col%2 == 0: #Pattern must be rows odd Number and col even Number
      for row in range(rows):
        if row%2 == 0:
          for column in range(1, col):
            if column%2 == 1:
              if column != col-1:
                print(" ",end="")
              else:
                print(" ")
            else:
              print("|",end="")
        else:
          print("-" * col)
    else:
      print("rows must be Odd and col must be Even")
  else:
    print("Rows and Column must be maximum 50")


DrawBoard(19, 20)


