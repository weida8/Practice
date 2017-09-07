#  File: EasterSunday.py

#  Description: Assignment 2

#  Student Name: Wei-Da Pan

#  Student UT EID: wp3479	

#  Course Name: CS 303E

#  Unique Number:  51630

#  Date Created: 2/8/2015

#  Date Last Modified: 2/18/2015

def main():

	y = eval(input("Enter year: "))


	a = y%19
	b = y//100
	c = y%100
	d = b//4
	e = b%4
	g = (8*b+13)//25
	h = (19*a+b-d-g+15)%30
	j = c//4
	k = c%4
	m = (a+11*h)//319
	r = (2*e+2*j-k-h+m+32)%7
	n = (h-m+r+90)//25
	p = (h-m+r+n+19)%32

	if(n==1):
		month="January"
	if(n==2):
		month="February"
	if(n==3):
		month="March"
	if(n==4):
		month="April"
	if(n==5):
		month="May"
	if(n==6):
		month="June"
	if(n==7):
		month="July"
	if(n==8):
		month="August"
	if(n==9):
		month="September"
	if(n==10):
		month="October"
	if(n==11):
		month="November"
	if(n==12):
		month="December"

	print("In", y, "Easter Sunday is on", p, month)

main()

