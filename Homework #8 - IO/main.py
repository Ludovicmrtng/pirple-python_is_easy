existingFilename = ["cryptocurrency.txt", "bestcurrency.txt"]

fileName = input("What file do you want to open: ")
fileName += ".txt"

if fileName in existingFilename:
  todo = input("Press r to read, Press w to overwrite or Press a to append to the file or Press d to replace a line: ")
  if todo == "r":
    File = open(fileName, "r")
    readFile = File.read()
    print(readFile)
  if todo == "w":
    overwriteFile = open(fileName, "w")
    contentFile = input("You can now write your new content: ")
    overwriteFile.write(contentFile)
    print("Your new content has been written sucessfully")
  if todo == "a":
    appendFile = open(fileName, "a")
    appendContent = input("Append your new content: ")
    content = appendFile.write("\n")
    content = appendFile.write(appendContent)
    appendFile.close()
    print("Your new content has been append sucessfully")
  if todo == "d":
    lineNumber = int(input("Which line do you want to replace?: "))
    lineContent = input("Write your new line content: ")
    lineFile = open(fileName, "r")
    listLines = lineFile.readlines()
    listLines[lineNumber] = f"{lineContent} \n"
    lineFile = open(fileName, "w")
    lineFile.writelines(listLines)
    lineFile.close()
    print(f"the line {lineNumber} has been replace sucessfully")
else:
  newFile = open(fileName, "w")
  existingFilename.append(fileName)
  newFile.close()
  print(f"A new file name has been created with the name of {fileName}")
