def emptyList(myList):
  if len(myList) == 0:
    return True
  else:
    return False

def averageList(myList):
  if emptyList(myList) == False:
    sum = 0
    numElements = len(myList)
    for ele in myList:
      sum = sum + ele
    return sum/numElements
  else:
    return "Error"