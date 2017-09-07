#  File: MagicSquare.py

#  Description: Assignment 10

#  Student Name: Wei-Da Pan

#  Student UT EID:wp3479

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 4/8/15

#  Date Last Modified: 4/9/15

def main(): 
	result_file=open("results.txt","w") #open and create a file to be written in 
	in_file=open("squares.txt", "r") #open data file
	line=in_file.readline() #read first line
	line=line.strip() #strip away all empty space around it
	num_square=int(line) #convert it into an interger so it can be used 
	line=in_file.readline() #skip a blank line
	final_result="" #create an empty string to store a string of everything

	for i in range(num_square): #loop through the total amount of squares given
		magic_string="" #empty string to store each square
		line=in_file.readline()
		line=line.strip()
		dim=int(line) #read dimension so it can be used for loop 
		squares=[] #create empty list to store the 2-D list
		for j in range(dim): #create a loop to store each row into the list 
			line=in_file.readline()
			magic_string=magic_string+line
			line=line.strip()
			row=line.split()

			for k in range(len(row)): #add each list into 2-D list 
				row[k]=int(row[k])
			squares.append(row)
		if(isMagic(squares)): #check to see if the square is a magic square by calling function
			squares_val="valid"
		else:
			squares_val="invalid"
		square_result="\n"+str(dim)+" "+squares_val+"\n"+magic_string #using the string to store results

		line=in_file.readline()

		final_result=final_result+square_result
	result_file.write(str(num_square)+"\n"+final_result) #write results into the created file
	
	print("The output has been written to results.txt")	
	
	in_file.close()	 #close files
	result_file.close()	
	
def isMagic(b):
	magic_state=True #use true/false switch to determine whether the magic square is true
	n=len(b)
	magic_num=(n*(n**2 +1)//2) #all the given conditions
	magic_range=n**2
	cross_sum_for=0
	cross_sum_back=0
	for i in b: #calls each row in the 2-D list
		if not magic_state:
			break
		row_sum=0
		for j in i:	
			if(j<1 or j>magic_range): #check to see if the numbers in the list is valid
				magic_state=False
				break
			row_sum=row_sum+j
		if(row_sum!=magic_num): #check to see if each row add up to the number it needs
			magic_state=False

	for i in range(n):
		magic_column_sum=0
		for j in range(n):
			magic_column_sum=magic_column_sum+b[j][i] 
		if(magic_column_sum!=magic_num): #check to see if each column add up to the number it needs
			magic_state=False
			break
		cross_sum_for=cross_sum_for+b[i][i] #adding up diagonal
		cross_sum_back=cross_sum_back+b[i][-(i+1)] #adding up 2nd diagonal

	if(cross_sum_back!=magic_num): #check for diagonal 
		magic_state=False
	elif(cross_sum_for!=magic_num):
		magic_state=False
				

	return(magic_state) #return whether it is a magic square or not

main()				
