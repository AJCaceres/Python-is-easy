#I/O
#Files

#File = open("Filename", "r") # "r", "w", "a", "r+" read, write, append, read and write
#File.close()


VacationSpots = ["London", "Paris", "New York", "Iceland"]

VacationFile = open("VacationPlaces", "w")

for Spots in VacationSpots:
	VacationFile.write(Spots + "\n")

VacationFile.close()

VacationFile = open("VacationPlaces", "r")

Firstline = VacationFile.readline()
print(Firstline)
Secondline = VacationFile.readline()
print(Secondline)
for line in VacationFile:
	print(line, end="")
VacationFile.close()

FinalSpot ="Thailand"

VacationFile = open("VacationPlaces", "a")
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces", "r")
for line in VacationFile:
	print(line, end="")
VacationFile.close()

for i in range(5):
	with open("VacationPlaces" +str(i), "r") as VacationFile:
		for line in VacationFile:
			print(line)
