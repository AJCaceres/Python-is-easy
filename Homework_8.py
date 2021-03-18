import os.path
from os import path

file = input("Please enter the name of the file ")


if os.path.exists(file)== True:
	
	while True:
		action = str(input("\nPlease enter: \na R if you want to read a file\na D if you want to delete the file and start over or \nan A if you want to append the file \n"))
		print(action)

		if action == "r" or action =="R":
			readFile = open(file, "r")
			for line in readFile:
				print(line, end="")
			readFile.close()
		elif action == "d" or action == "D":
			print("This is the delete method")
			newFile = open(file,"w")
			newData = []
			while(True):
				tempData = []
				tf = 1
				dataLine =input("Please type the new text\n")
				tempData.append(dataLine)
				newData.append(tempData)
				tf = int(input("Type 0 to end the program or 1 to add an extra line\n"))
				if tf == 0:
					for data in newData:
						newFile.write(str(data))
						newFile.write(" \n")
					newFile.close()
					break
		elif action == "a" or action =="A":
			print("This is the append method\n")
			appendFile =open(file,"a")
			newData = []
			while True:
				tempData = []
				dataLine =input("Please type the new text\n")
				tempData.append(dataLine)
				newData.append(tempData)
				tf = input("Type 0 to end the program or another character to add an extra line\n")
				if tf == "0":
					for data in newData:
						appendFile.write(str(data))
						appendFile.write(" \n")
					appendFile.close()
					break

		else:
			break
