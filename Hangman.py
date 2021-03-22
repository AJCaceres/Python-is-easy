def drawHangman(errors):
	if errors == 0:
		print("___\n|\n|\n|")
	elif errors==1:
		print("___O\n|\n|\n|")
	elif errors==2:
		print("___O\n|  |\n|\n|")
	elif errors==3:
		print("___O\n| /|\n|\n|")
	elif errors==4:
		print("___O\n| /|\\\n|\n|")
	elif errors==5:
		print("___O\n| /|\\\n| /\n| ")
	else:
		print("___O\n| /|\\\n| / \\\n| ")
		return False



Player = 1
endGame = 0
while(endGame == 0):
	word = str(input("Please enter a word to play Hangman "))
	numberWord =len(word)
	errors = 0
	corrects = 0
	space = "_ "*(numberWord-1)
	space = space +"_"
	spaceArray = space.split(" ")
	print(spaceArray)
	drawHangman(errors)
	while(errors !=6):
		counter = 0
		letter = str(input("Please enter a letter "))
		for i in range(numberWord):
			if letter == word[i]:
				counter +=1
				spaceArray[i] = letter
				corrects += 1
				print(spaceArray)
		if counter == 0:
			errors += 1
			print(spaceArray)
			drawHangman(errors)
		if errors  == 6:
			print("GAME OVER")
		if corrects == numberWord:
			print("YOU WIN! :)")
			endGame =1
			break
	

