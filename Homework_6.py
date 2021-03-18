

print("Inserte el número de columnas y filas para el tablero")
numero = int(input())
espacios = numero*2 -1

def drawBoard(numero):
	espacios = numero*2 -1
	
	for x in range(espacios):
		if x %2 == 0:
			for y in range(1,espacios+1):
				if y%2 == 1:
					if y!=espacios:
						print(" ", end="")
					else:
						print(" ")
				else:
					print("|",end="")
		else:
			print("-"*espacios)
	return True		

drawBoard(numero)