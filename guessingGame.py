
import time
from random import randint, random

randVal = randint(0,100)

# while(True):
# 	guess = int(input("Please enter your guess number: "))
# 	if guess == randVal:
# 		break
# 	elif guess < randVal:
# 		print("Your guess number is too low")
# 	else:
# 		print("Your guess is too high")

# print("You guessed correctly with:", guess)

randVal2 = random()

print(randVal2)

upper = 1.0
lower = 0.0

guess = 0.5
startTime = time()
while(True):
	if guess == randVal2:
		break
	elif guess < randVal2:
		lower = guess
	else:
		upper = guess
	guess = (upper+lower)/2

endTime = float(time.gmtime())
totalTime = endTime-startTime
print(guess)
print("It took us:",totalTime,"seconds to guess the number")