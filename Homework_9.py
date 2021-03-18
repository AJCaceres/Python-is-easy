class Vehicle:
	def __init__(self, m, mo, y, w, nm = False, tsm = 0):
		self.make = m
		self.model = mo
		self.year = y
		self.weight = w
		self.needsMaintenance = nm
		self.tripsSinceMaintenance = tsm
		

	def getMake(self):
		return self.make

	def getModel(self):
		return self.model

	def getYear(self):
		return self.year

	def getWeight(self):
		return self.weight


class Cars(Vehicle):
	def __init__(self, m, mo, y, w, nm= False, tsm= 0, d=False):
		Vehicle.__init__(self, m, mo, y, w, nm, tsm)
		self.isDriving = d

	def Drive(self):
		if self.needsMaintenance == False or self.tripsSinceMaintenance >= 99:
			self.isDriving = True			
		else:
			print("The vehicle "+self.make+" needs maintenance.")
			self.isDriving = False

	def Stop(self):
		self.isDriving = False
		self.tripsSinceMaintenance += 1
		if self.tripsSinceMaintenance == 100:
			self.needsMaintenance = True

	def repair(self):
		self.tripsSinceMaintenance = 0
		self.needsMaintenance = False

	def __str__(self):
		return ("The car "+ self.make+" "+ self.model+" has "+str(self.tripsSinceMaintenance)+" trips since maintenance and switch in "+str(self.needsMaintenance))



Car1 = Cars("Mazda", "3", 2021, 100000)
Car2 = Cars("Fiat", "500", 2021, 86000)
Car3 = Cars("Chevrolet", "Colorado", 2021, 250000) 

for i in range(85):
	Car1.Drive()
	Car1.Stop()
print(Car1)

for i in range(105):
	Car2.Drive()
	Car2.Stop()
print(Car2)

for i in range(201):
	Car3.Drive()
	Car3.Stop()
print(Car3)
