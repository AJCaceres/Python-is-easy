"""
Homework no. 1
Variables

This lesson is to know how to use variables.
I need to list the characteristics of my favorite song.

"""

Name = "Legends"
Artist = "Juice WRLD"
Album = "Legends"
Genre = "Hip-hop/ Rap"
DurationInSeconds = 192
YearOfPublish = 2018
SimilarArtists = "Pop Smoke and Lil Peep"
Mood = "Depressive"
Producer = "Russ Chell and Take a Daytrip" 

# print(Name)
# print(Artist)
# print(Album)
# print(Genre)
# print(DurationInSeconds)
# print(YearOfPublish)
# print(SimilarArtists)
# print(Mood)
# print(Producer)

FavoriteSong = {"name": Name, "artist": Artist,"album": Album, "genre": Genre,
"duration": DurationInSeconds, "year": YearOfPublish, "similarities": SimilarArtists,
"mood": Mood, "producer":Producer}

for i in FavoriteSong:
	print("Key: {}, Value: {}".format(i,FavoriteSong[i]))

Key = input("\nType a key\n")
Value = input("Type a value\n")


def Guess(key, value):
	if key in FavoriteSong:
		print("Correct key")
		for info, i in FavoriteSong.items():
			if i == value:
				print("Correct value")
				return True
				break
	else:
		return false

Guess(Key,Value)