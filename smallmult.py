def main():

	check = False
	start = 20
	while(check == False):
		for i in range(1, 21):
			if(start%i != 0):
				start +=1
				#print(start)
				check = False
				break
			elif(start%1 == 0):
				check = True
	print(start)

main()
