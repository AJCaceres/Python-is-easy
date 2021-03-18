"""
While loops

while(condition):
	Action
	Action2
	Action3
"""

counter = 1
while(counter<=10):
	#print(counter)
	counter += 1

height = 5000
velocity = 50
time= 0

while(height>0):
	height-= velocity
	time +=1

print(height)
print(time)

"""
Breaking and continuing
"""

Participants = ["Jen","Alex","Tina","Joe","Ben"]

position = 1
for name in Participants:
	if name == "Tina":	
		break
	position += 1

print(position)