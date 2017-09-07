#  File: ISBN.py

#  Description: Assignment 9

#  Student Name: Wei-Da Pan

#  Student UT EID: wp3479

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 4/4/15

#  Date Last Modified: 4/4/15

def main():

	a = open("isbn.txt", "r") #opening isbn.txt and to read it
	fulltext=a.readlines()
	a.close()
	a = open("isbnOut.txt", "w") #open and create a isbnOut.txt so each line can be written to it

	for isbn1 in fulltext: #read line by line and strip off the end and make all upper case
		isbn=isbn1.strip().upper()
		stringvalue=0
		valid = True #setup a True/False switch
		newlist = [] #create an empty list to allow valid integers to be added to it

		for i in isbn: #loops through each character in the string and ord() them to check for if it's within 0-9 and have an X at the end
			ord_i=ord(i)
			if(ord_i>=48 and ord_i<=57):
				stringvalue=stringvalue+1
				newlist.append(int(i))
			elif(ord_i==45):
				stringvalue=stringvalue+0
			elif(stringvalue==9 and ord_i==88):
				stringvalue=stringvalue+1
				newlist.append(10)
			else:
				valid=False
				break

		if(stringvalue!=10): #check to see if the string is longer than 10 
			valid=False
		if(valid):  #run through the test of partial sum twice
			partialsum(newlist)
			partialsum(newlist)
			if(newlist[-1]%11==0):
				valid=True
			else:
				valid=False

		if(valid): #output each line into file 
			a.write(isbn+ " valid\n") 
		else:
			a.write(isbn+ " invalid\n")

	a.close() #closing the output file


def partialsum(x): #loops through each number and have them add each other as partialsum
	Csum=0
	for i in range(1,len(x)):
		x[i]=x[i]+x[i-1]


main()
