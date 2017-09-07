#  File: Turtle.py
#  Description: Homework 2/ Turtle description
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 9/15/15
#  Date Last Modified: 9/15/15
import turtle
import math
def main():

        #drawing the x and y axis 
        ttl = turtle.Turtle()
        screen = turtle.Screen()
        screen.title = "CS 313E Assignment 2"
        screen.setup(900,900)
        ttl.speed(0)
        ttl.penup()
        ttl.goto(-400,0)
        ttl.pendown()
        ttl.forward(800)
        ttl.penup()
        ttl.goto(0,-400)
        ttl.left(90)
        ttl.pendown()
        ttl.forward(800)
        ttl.right(180)
        
        #draw the tick marks and label for x axis
        for i in range(-400, 500, 100):

                if(i==0):
                        continue
                else:
                        ttl.penup()
                        ttl.goto(i,5)
                        ttl.pendown()
                        ttl.forward(10)
                        ttl.penup()
                        ttl.goto(i,-17)
                        ttl.pendown()
                        label = i//100
                        ttl.write(label)

        #draw the tick marks and label for y axis
        ttl.left(90)
        for i in range(-400, 500, 100):
                
                if(i==0):
                        continue
                else:
                        ttl.penup()
                        ttl.goto(-5, i)
                        ttl.pendown()
                        ttl.forward(10)
                        ttl.penup()
                        ttl.goto(17, i)
                        ttl.pendown()
                        label = i//100
                        ttl.write(label)

        #draw the red sin(x) line
        ttl.penup()
        ttl.goto(-math.pi*100 ,0)
        ttl.pendown()
        ttl.pencolor("red")
        x =  -math.pi
        y = math.sin(x)

        while(x <= math.pi):
                x = x+.001
                y = math.sin(x)
                ttl.goto(100*x, 100*y)

        #draw the blue cos(x) line
        ttl.penup()
        ttl.goto(-math.pi*100,0)
        ttl.pendown()
        ttl.pencolor("blue")
        x = -math.pi
        y = math.cos(x)

        while(x <= math.pi):
                x = x+.001
                y = math.cos(x)
                ttl.goto(100*x, 100*y)

        #draw the green x^2 - 4 line
        ttl.penup()
        ttl.goto(-math.pi*100,0)
        ttl.pendown()
        ttl.pencolor("green")
        x = -math.pi
        y = (x*x)-4

        while(x <= math.pi):
                x = x+.001
                y = (x*x)-4
                ttl.goto(100*x, 100*y)

        #draw the orange x^3 * x^2 +3 line
        ttl.penup()
        ttl.goto(-math.pi*100,0)
        ttl.pendown()
        ttl.pencolor("orange")
        x = -math.pi
        y = (x*x*x)*(x*x)+3

        while(x <= math.pi):
                x = x+.001
                y = (x*x*x)*(x*x)+3
                ttl.goto(100*x, 100*y)

main()


