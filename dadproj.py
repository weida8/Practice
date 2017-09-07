def main():
	divisor=eval(input("Enter average divisor: "))
	inFile = open("dadproj.txt","r")
	outFile = open("answer.txt","w")
	line = inFile.readline()
	line = line.split()
	#print(line)
	answer =[]
	bigAvg=0
	smallAvg=0
	turnBase=False #if turnbase is false then smallAvg was the last number
	for data in range(len(line)-divisor-1):
		#print("x")
		difference=0 #the difference between bigavg-smallavg
		average = (int(line[data])+int(line[data+1])+int(line[data+2]))/divisor
		if(bigAvg==0 and smallAvg==0):
			if(int(line[data+2])>average):
				smallAvg=int(line[data+2])
			elif(int(line[data+2])<average):
				bigAvg=int(line[data+2])
			continue

		elif(bigAvg==0 and smallAvg!=0):
			if(int(line[data+2])<average):
				bigAvg=int(line[data+2])
				turnBase=True
				difference=bigAvg-smallAvg
				print("differnce =",difference)
				answer.append(difference)
			continue

		elif(bigAvg!=0 and smallAvg==0):
			if(int(line[data+2])>average):
				smallAvg=int(line[data+2])
				difference=bigAvg-smallAvg
				print("differnce =",difference)
				answer.append(difference)
			continue

		elif(bigAvg!=0 and smallAvg!=0 and turnBase==True):
			if(int(line[data+2])>average):
				smallAvg=int(line[data+2])
				difference=bigAvg-smallAvg
				print("differnce =",difference)
				answer.append(difference)
				turnBase=False
				#print("x")
			continue
		elif(bigAvg!=0 and smallAvg!=0 and turnBase==False):
			if(int(line[data+2])<average):
				bigAvg=int(line[data+2])
				difference=bigAvg-smallAvg
				print("differnce =",difference)
				answer.append(difference)
				turnBase=True
				#print("y")
			continue
	for element in answer:
		outFile.write(str(element)+"\n")
	print(answer)
	inFile.close()
	outFile.close()

main()





