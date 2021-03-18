


Name = "Legends"
Artist = "Juice WRLD"
Album = "Legends"
Genre = "Hip-hop/ Rap"
DurationInSeconds = 192
YearOfPublish = 2018
SimilarArtists = "Pop Smoke and Lil Peep"
Mood = "Depressive"
Producer = "Russ Chell and Take a Daytrip" 

value = input("Hello, please enter a: \n 'G' if you want the genre \n 'A' if you want the artist or \n 'Y' if you want the year\n")
def information(x):
	if x == "G" or x == "g":
		print(Genre)
	elif x  == "A" or x =="a":
		print(Artist)
	elif x == "Y" or x == "y":
		print(YearOfPublish)
	else:
		print("Invalid character")

information(value)


