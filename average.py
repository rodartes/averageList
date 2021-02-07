def emptyList(myList):
  if myList == False:
    return True
  else:
    return False

def average(myList):
  if emptyList(myList) == True:
    sum = 0
    for ele in myList:
      sum = sum + ele
      return sum;
  else:
    print("Error")