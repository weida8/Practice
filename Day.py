#  File: Day.py

#  Description: Assignment 3

#  Student Name: Wei-Da Pan	

#  Student UT EID: wp3479

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 2/15/2015

#  Date Last Modified: 2/15/2015

def main():

	year = eval(input("Enter year: "))
	while(year < 1900 or year > 2100):
		year = eval(input("Enter year: "))

	month = eval(input("Enter month: "))
	while(month <1 or month >12):
		month = eval(input("Enter month: "))

	day = eval(input("Enter day: "))
	if(month == 1,3,5,7,8,10,12 ):
		while(day < 1 or day > 31):
			day = eval(input("Enter day: "))
	if(month == 4,6,9,11):
		while(day < 1 or day > 30):
			day = eval(input("Enter day: "))
	if(month == 2):
		if(year%4 != 0 or (year%100 == 0 and year%400 != 0)):
			while(day < 1 or day > 28):
				day = eval(input("Enter day: "))
		else:
			while(day < 1 or day > 29):
				day = eval(input("Enter day: "))

	if(month == 1):
		a = 11
		year = year-1
	if(month == 2):
		a = 12
		year = year-1
	if(month == 3):
		a=1
	if(month == 4):
		a=2
	if(month == 5):
		a=3
	if(month == 6):
		a=4
	if(month == 7):
		a=5
	if(month == 8):
		a=6
	if(month == 9):
		a=7
	if(month == 10):
		a=8
	if(month == 11):
		a=9
	if(month == 12):
		a=10

	b = day
	c = year%100
	d = year//100	

	w = (13*a -1) //5
	x = c//4
	y = d//4
	z = w+x+y+b+c-2*d	
	r = z%7
	r = (r+7)%7

	if(r==0):
		weekday = "Sunday"		
	if(r==1):
		weekday = "Monday"
	if(r==2):
		weekday = "Tuesday"
	if(r==3):
		weekday = "Wednesday"
	if(r==4):
		weekday = "Thursday"
	if(r==5):
		weekday = "Friday"
	if(r==6):
		weekday = "Saturday"

	print("The day is",weekday,end="")
	print(".")

main()