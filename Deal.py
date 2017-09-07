`
# File: Deal.py

# Description: Assignment 4

# Student Name: Wei-Da Pan

# Student UT EID: wp3479

# Course Name: CS 303E

# Unique Number: 51630

# Date Created: 2/21/2015

# Date Last Modified: 2/21/2015

def main():

	import random

	numberplay = eval(input("Enter number of times you want to play: "))

	print("  Price    Guess    View    New Guess")
	timeplayed = 0 
	switched = 0

	while(timeplayed <numberplay):

		price = random.randint(1,3)
		guess = random.randint(1,3)

		view = random.randint(1,3)
		while(view == guess or view == price):
			view = random.randint(1,3)

		newGuess = random.randint(1,3)
		while(newGuess == view or newGuess == guess):
			newGuess = random.randint(1,3)
		
		print("   ",price,"      ", guess,"     ", view, "        ", newGuess)
		if(newGuess == price):
			switched = switched+1

		timeplayed=timeplayed+1
				
	probability_switched = switched/numberplay
	probability_stayed = (numberplay-switched)/numberplay

	print("")
	print("Probability of winning if you switch = ", "%.2f" %round(probability_switched,3))
	print("Probability of winning if you do not switch = ", "%.2f" %round(probability_stayed,3))

main()