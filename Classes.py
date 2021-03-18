class Team:
	def __init__(self, Name ="Name",Origin = "Origin"):
		self.TeamName = Name
		self.TeamOrigin = Origin

	def DefineTeamName(self, Name):
		self.TeamName = Name

	def DefineTeamOrigin(self, Origin):
		self.TeamOrigin = Origin

Team1 = Team("Tiburones","Guatemala")
Team2 = Team("Venados","Chimaltenango")

class Player(Team):
	def __init__(self,PlayerName, PPoints, TeamName, TeamOrigin):
		Team.__init__(self,TeamName,TeamOrigin)
		self.PlayerName = PlayerName
		self.PlayerPoints = PPoints

	def ScoredPoints(self):
		self.PlayerPoints += 1

	def setName(self,Name):
		self.PlayerName = Name

	def __str__(self):
		return self.PlayerName + " has scored: "+str(self.PlayerPoints) +" points"



Player1 = Player("Alvaro", 0, "Tiburones","Guatemala")
print(Player1)


class Pet:
	def __init__(self, n, a, h, p):
		self.name = n
		self.age = a
		self.hunger = h
		self.playful = p
#getters
	def getName(self):
		return self.name	

	def getAge(self):
		return	self.age

	def getHunger(self):
		return	self.hunger

	def getPlayful(self):
		return	self.playful
#setters
	def setName(self, name):
		self.name = name

	def setAge(self, Age):
		self.age = Age

	def setHunger(self, hunger):
		self.hunger = hunger

	def setPlayful(self, play):
		self.playful = play

	def __str__(self):
		return (self.name + " is " + str(self.age) +" years old")

Pet1 = Pet("Coco", 4, False, True)
print(Pet1.getName())
print(Pet1.getPlayful())
Pet1.setName("Snowball")
Pet1.setPlayful(False)
print(Pet1.getName())
print(Pet1.getPlayful())

class Dog(Pet):
	def __init__(self,name,age,hungry,playful,breed,favoriteToy):
		Pet.__init__(self,name,age,hungry,playful)
		self.breed = breed
		self.favoriteToy = favoriteToy

	def wantsToPlay(self):
		if self.playful == True:
			return("Dog wants to play with " + self.favoriteToy)
		else:
			return("The dog doesn't want to play")

class Cat(Pet):
	def __init__(self, name, age, hunger, playful, place):
		Pet.__init__(self,name,age,hunger, playful)
		self.FavoritePlaceToSit = place

	def wantsToSit(self):
		if self.playful == False:
			print("The cat wants to sit in "+ self.FavoritePlaceToSit)
		else:
			print("The cat wants to play")

	def __str__(self):
		return (self.name+ "'s favorite place to sit is "+self.FavoritePlaceToSit)

class Human:
	def __init__(self,name,Pets):
		self.name = name
		self.Pets = Pets

	def hasPets(self):
		if len(self.Pets) != 0:
			return "yes"
		else:
			return "no"

huskyDog = Dog("Leo",5,False,True,"Husky","Stick")
Play = huskyDog.wantsToPlay()

print(Play)

typicalCat= Cat("Mew",4,False,False,"above the stereo")
typicalCat.wantsToSit()

print(typicalCat)

yourAverageHuman = Human("Manuel",[huskyDog,typicalCat])

hasPet = yourAverageHuman.hasPets()
print(hasPet)
print(yourAverageHuman.Pets[1])