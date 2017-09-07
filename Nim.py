#  File: Nim.py
#  Description: Homework 1
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 9/9/15
#  Date Last Modified:

def main():

	inFile = open("nim.txt", "r")
	dim = inFile.readline()
	dim = dim.strip()
	dim = int(dim)

	for i in range(dim):
		newnim = inFile.readline()
		newnim = newnim.strip()
		gamelist = newnim.split()
		#print(gamelist)

		int_gamelist = []
		for k in gamelist:
			num = int(k)
			int_gamelist.append(num)
		print(int_gamelist)


main()

