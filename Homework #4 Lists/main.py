#A function to add seasoning to the list, if same seasoning will be add to Leftovers

myUniqueList = []
myLeftovers = []

def AddToList(lists):
  if lists in myUniqueList:
    myLeftovers.append(lists)
  else:
    myUniqueList.append(lists)

AddToList("Salt")
AddToList("Pepper")
AddToList("Salt")
AddToList("Sugar")
AddToList("Rosemary")
AddToList("Basil")
AddToList("Cumin")
AddToList("Bayleaf")
AddToList("Sugar")
AddToList("Cardamom")
AddToList("Cumin")
AddToList("Celery")
AddToList("Pepper")


print(myUniqueList)
print(myLeftovers)