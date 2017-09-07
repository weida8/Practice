#  File: Hailstone.py

#  Description: Assignment 5

#  Student Name: Wei-Da Pan

#  Student UT EID: wp3479

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 2/28/15

#  Date Last Modified: 2/28/15
def main():

	s = eval(input("Enter starting number of the range: ")) #asks user for initial input
	e = eval(input("Enter ending number of the range: ")) #asks user for ending input
	while(s<0 or e<0 or e<=s): #make sure s and e follows the rules
		s = eval(input("Enter starting number of the range: "))
		e = eval(input("Enter ending number of the range: "))

	best_i = 0 #set initial i value
	best_n = 0 #set initial n value
	for i in range(s,e+1): #checks for every integer intside the range
		j=i #set a new variable for i so i can stay the same
		n=0
		while(j!=1): #checks to see if j is 1 yet?
			if(j%2 ==0): #even number
				j = j//2
			elif(j%2 ==1): #odd number
				j = 3*j + 1
			n=n+1 #counts final loop counts when j=1
		if(n>best_n): #compares the highest loop count value 
			best_n=n
			best_i=i

	print("The number",best_i,"has the longest cycle length of",str(best_n) + ".") #print answer

main()		
