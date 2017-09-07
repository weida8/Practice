#  File: geometry.py
#  Description: HW 5
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 10/12/15
#  Date Last Modified: 10/15/15

import math

#create point objects
class Point:

	 def __init__(self, x, y):

	 	self.x = x
	 	self.y = y

	 #find distance between two points
	 def dist(self, other):

	 	distX = self.x - other.x
	 	distY = self.y - other.y
	 	pointDist = (distX**2 + distY**2)**0.5
	 	return(pointDist)

	 def __str__(self):

	 	return("("+str(self.x)+", "+ str(self.y)+")")

	 def __eq__(self, other):

	 	return(self.x == other.x and self.y == other.y)

	 def __int__(self):

	 	return(int(self))

#create line object
class Line:

	def __init__(self, p1, p2):

		self.p1 = p1
		self.p2 = p2

	#find slope of the line
	def slope(self):

		slope = (self.p1.x-self.p2.x) / (self.p1.y-self.p2.y)
		return(slope)

	#check to see the line is horizontal
	def isHorizontal(self):

		return(self.p1.y == self.p2.y)

	#check to see if the line is vertical
	def isVeritcal(self):

		return(self.p1.x == self.p2.x)

	#find the x intercept of the line
	def xIntercept(self):

		if(self.isHorizontal()):
			return(float('inf'))
		else:
			b = (self.p1.y-(self.slope()*self.p1.x))
			return(-b/self.slope())

	#find the y interceopt of the line
	def yIntercept(self):

		if(self.isVeritcal()):
				return(float('inf'))
		else:
			return((self.p1.y-(self.slope()*self.p1.x)))

	#check to see if the two lines are parallel to each other
	def isParallel(self, other):

		return(self.slope() == other.slope() and self.yIntercept() != other.yIntercept())

	#check to see if the two lines are perpendicular to each other
	def isPerpendicular(self, other):

		return(self.slope() == -(1/other.slope()))

	#check to see if the point is on the line
	def isOnLine(self, pt):

		return(self.slope()*pt.x + self.yIntercept() == pt.y)

	#find the distance between the point and the line
	def perpDist(self, pt):

		radian = math.atan((self.slope()))
		xLinePt = (pt.y - self.yIntercept())/self.slope()
		xDistance = math.abs(pt.x - xLinePt)
		distanceToLine = xDistance*math.sin(radian)
		return(distanceToLine)

	#find the point of intersect
	def intersectionPoint(self, other):

		eq1 = [self.slope(), other.yIntercept()]
		eq2 = [other.slope(), other.yIntercept()]
		x = (eq2[1]-eq1[1])/(eq1[0]-eq2[0])
		y = eq1[0]*x + eq1[1]
		return(Point(x, y))

	def __str__(self):

		if(self.isHorizontal):
			return("y = "+ str(self.p1.y))
		elif(self.isVeritcal):
			return("x = "+ str(self.p1.x))
		else:
			return("y = " + str(self.slope())+"x "+ str(self.yIntercept()))

#create a circle object
class Circle: 

	def __init__(self, center, radius):

		self.c = center
		self.r = radius

	def circumference(self):

		return(2*math.pi*self.r)

	def area(self):

		return(math.pi*(self.r**2))

	#check to see if the point is in the circle or not
	def containsPoint(self, pt):

		return(((pt.x-self.c.x)**2 + (pt.y-self.c.y)**2) <= (self.r**2))

	#check to see if the line is tanget to the circle
	def hasTangentLine(self, line):

		return((line.p1.x - self.c.x)**2 + (line.p1.y - self.c.y)**2 == self.r**2 and not (line.p1.x - self.c.x)**2 + (line.p1.y - self.c.y)**2 < self.r**2)

	def __str__(self):

		return("Circle:\n"+"Radius = ".rjust(12) + str(self.r)+"\nCenter = ".rjust(12)+"("+str(self.c.x)+", "+str(self.c.y)+")")

def main():

	#open the input file and read them into a 2-D list 
	inFile = open("geometry.txt", "r")
	lineList = []
	for line in inFile:
		line = line.rstrip("\n")
		numList = [float(n) for n in line.split()]
		lineList.append(numList)

	pointA = Point(lineList[0][0], lineList[0][1])
	pointB = Point(lineList[1][0], lineList[1][1])

	print(pointA)
	print(pointB)
	print("{:0.4f}".format(Point.dist(pointA, pointB)))

	lineAB = Line(pointA, pointB)
	print("{:0.4f}".format(Line.slope(lineAB)))
	print("{:0.4f}".format(Line.xIntercept(lineAB)))
	print("{:0.4f}".format(Line.yIntercept(lineAB)))

	pointC = Point(lineList[2][0], lineList[2][1])
	pointD = Point(lineList[3][0], lineList[3][1])
	lineCD = Line(pointC, pointD)

	print(lineAB)
	print(lineCD)

	if(Line.isParallel(lineAB, lineCD)):
		print("The two lines are parallel")
	else:
		print(Line.intersectionPoint(lineAB, lineCD))

	if(Line.isPerpendicular(lineAB, lineCD)):
		print("The two lines are perpendicular")
	else:
		print("The two lines are not perpendicular")

	circle1 = Circle(Point(lineList[4][1], lineList[4][2]), lineList[4][0])
	circle2 = Circle(Point(lineList[5][1], lineList[5][2]), lineList[5][0])

	pointP = Point(lineList[6][0], lineList[6][1])
	pointQ = Point(lineList[7][0], lineList[7][1])

	if(Circle.containsPoint(circle1, pointP)):
		print("point P is inside the circle")
	else:
		print("point P is not inside the circle")

	if(Circle.containsPoint(circle1,pointQ)):
		print("Point Q is inside the circle")
	else:
		print("point Q is not inside the circle")

	if(Circle.hasTangentLine(circle2, lineCD)):
		print("line CD is tanget to circle 2")
	else:
		print("line CD is not tanget to circle 2")


main()







