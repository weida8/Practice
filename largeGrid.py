def main():

	matrix =[]
	inFile = open("grid.txt", "r")
	for line in inFile:
		line = line.rstrip("\n")
		lineList = line.split()
		matrix.append(lineList)
	#print(matrix)

	finalmax = 0
	position = 1
	for i in range(len(matrix)):
		count = 1
		currentmax = 1
		d=0
		for j in range(len(matrix)-3):
			#print("")
			#print("loop:", j+1)
			if(count <= 4 and int(matrix[i][j]) != 0):
				currentmax *= int(matrix[i][j])
				#print("count:", count)
				#print("currentmax:", currentmax)
				if(count == 4):
					finalmax = currentmax
				count += 1
			elif(int(matrix[i][j]) == 0):
				count = 1
				currentmax = 1 
				d = j+1
			elif(count == 5 and int(matrix[i][j] != 0)):
				currentmax //= int(matrix[i][d])
				currentmax *= int(matrix[i][j])
				d += 1
				if(currentmax>finalmax):
					finalmax = currentmax
			#print("d:", d)
			#print("position:", position)
			#print("finalmax: ", finalmax)
			position += 1

	for i in range(len(matrix)):
		print("")
		print("big loop:", i+1)
		count = 1
		currentmax = 1
		d = 0
		for j in range(len(matrix)-3):
			print("")
			print("loop: ", j+1)
			print("d:", d)
			if(count <= 4 and int(matrix[j][i])!=0):
				currentmax *= int(matrix[j][i])
				if(count == 4 and finalmax<currentmax):
					finalmax = currentmax
				count += 1
			elif(int(matrix[j][i]) == 0):
				count = 1
				currentmax = 1
				d = j+1
			elif(count == 5 and int(matrix[j][i]) != 0):
				currentmax //= int(matrix[d][i])
				currentmax *= int(matrix[j][i])
				d += 1
				if(currentmax>finalmax):
					finalmax = currentmax

	#product of diagonal /
	p=0
	for i in range(3, len(matrix)):
		currentmax = 1 
		for j in range(0, len(matrix)-3):
				x = j+3
				y = i-3
				for k in range(4):
					print("y:", y)
					print("x:", x)
					currentmax *= int(matrix[y][x])
					x -= 1
					y += 1
					print("diagonal CM:", currentmax)
					if(finalmax< currentmax):
						print("***********************************")
						finalmax = currentmax
				currentmax = 1


	#product of diagonal \
	print("start of second diagonal **********************************")
	p=0
	for i in range(3, len(matrix)):
		currentmax = 1 
		for j in range(0, len(matrix)-3):
				x = j
				y = i-3
				for k in range(4):
					print("y:", y)
					print("x:", x)
					currentmax *= int(matrix[y][x])
					x += 1
					y += 1
					print("diagonal CM:", currentmax)
					if(finalmax< currentmax):
						print("***********************************")
						finalmax = currentmax
				currentmax = 1
				

		

	print(finalmax)

main()
