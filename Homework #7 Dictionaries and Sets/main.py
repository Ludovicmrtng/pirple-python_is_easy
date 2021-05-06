songAttributes = {"Title":"If I Ain't Got You", "Artist":"Alicia Keys", "Genre":"Rhythm and Blues", "Album":"Diary of Alicia Keys", "PublishedYear":2003, "Label":"J Records"}

for attribute, songAttribute in songAttributes.items():
  print(attribute, songAttribute)


def guessAttribute(key, value):
  if value in songAttributes.values() and key in songAttributes.keys():
    print("You are right")
  else:
    print("Wrong Answer!")

guessAttribute("Artist", "Alicia Keys")