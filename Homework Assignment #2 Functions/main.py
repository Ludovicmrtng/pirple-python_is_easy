#Function to describe alicia keys song's attribute

#Song attribute Variables
ArtistName, Year, Duration = "Alicia Keys", 2003, 3.48

#Define Artist
def Artist():
  if ArtistName == "Alicia Keys":
    print(ArtistName)
  else:
    print(False)

#Define year of publishment
def PublishedYear():
  if Year == 2003:
    print(Year)
  else:
    print(False)

#Define the duration of song in minutes
def DurationInMinutes():
  if Duration == 3.48:
    print(Duration)
  else:
    print(False)

Artist()
PublishedYear()
DurationInMinutes()