# List homework

myUniqueList = []
myLeftovers = []

def addToList(n):
	if n in myUniqueList:
		addToList2(n)
	else:
		myUniqueList.append(n)


def addToList2(m):
	myLeftovers.append(m)


addToList(1)
addToList(32)
addToList(7)
addToList(26)
addToList(9)
addToList(12)
addToList(36)
addToList(1)

print(myUniqueList)
print(myLeftovers)