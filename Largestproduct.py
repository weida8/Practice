def main():

	inFile = open("inputFile.txt", "r")
	matrix =[]
	finalmax = 0
	currentmax = 1
	count = 1
	d = 0	
	for line in inFile:
		line = line.rstrip("\n")
		matrix.append(list(line))

	#horizontal
	for i in range(len(matrix)):
		#d = 0 #front divisor count to replace j
		#count =1 #count the number of elements we have multiplied
		#currentmax = 1
		for j in range(len(matrix[i])):
			if(count <= 13):
				if(int(matrix[i][j]) != 0):
					currentmax *= int(matrix[i][j])
					count += 1
					#print("tempmax: ", currentmax)
					print(matrix[i][j])
				else:
					currentmax = 1
					count = 1
					d = j+1
					continue
			elif(count == 14):
				if(int(matrix[i][j]) != 0):
					currentmax //= int(matrix[i][d])
					currentmax *= int(matrix[i][j])
					d += 1 
					print(matrix[i][j])
					print("currentmax:",currentmax)
					if(currentmax>finalmax):
						finalmax = currentmax
						#currentmax = 1
						print("final max:", finalmax)
					else:
						continue
				else:
					currentmax = 1
					count = 1
					d = j+1
					continue

					
	print(finalmax)

			
main()
