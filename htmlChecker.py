#  File: htmlChecker.py
#  Description: HW 6
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 10/20/15
#  Date Last Modified:10/22/15
import sys
#creates the stack object 
class Stack(object):

	def __init__(self):

		self.items = []

	def push(self, item):

		self.items.append(item)

	def pop(self):

		return(self.items.pop())

	def peek(self):

		return(self.items[-1])

	def size(self):

		return(len(self.items))

	def __str__(self):

		#make Stack obj a string so it can be printed
		return(str(self.items))

#make a list of all the tags and return the list
#use a cheker boolean to see if the string should be added as a tag
def getTag(dataline):

	checker = False
	tagList = []
	newTag = ""
	for char in range(len(dataline)):
		if(checker == True and dataline[char] != ">" and dataline[char]!= "<"):
			newTag += dataline[char]
			continue
		elif(dataline[char] == ">"):
			checker = False
			tagList.append(newTag)
			newTag = ""
			continue
		elif(dataline[char] == "<"):
			checker = True
	return(tagList)

def main():

	stack = Stack()
	#has exceptions so they dont have to be checked
	exceptions =["br", "meta"]
	finalTagList = []
	inFile = open("htmlfile.txt", "r")
	#calls for each line and append
	for line in inFile:
		line = line.rstrip("\n")
		if(len(line)==0 or "<" not in line):
			continue
		else:
			finalTagList.append(getTag(line))

	#goes through all the tags in the list and push onto stack and check accordingly
	for i in finalTagList:
		for j in i:
			if("/" not in j and j not in exceptions):
				stack.push(j)
				print("Tag is " + stack.peek() + " : pushed: stack is now"+ str(stack))
			elif(j in exceptions or "meta" in j):
				print("Tag is " + j + " : does not need to match: stack is now " + str(stack))
			elif("/" in j and j == "/"+stack.peek()):
				stack.pop()
				print("Tag is " + j + " : matches: stack is now " + str(stack))
				continue
			elif("/" in j and j != stack.peek()):
				print("Error: tag is " + j + " but top stack is " + stack.peek())
				return()
	#if stack is done return message whether there are left over or not
	if(stack.size()>0):
		print("Processing complete. Unmatched tags remain on stack: " + str(stack))
	else:
		print("Processing compelte. No mismatches found.")
	inFile.close()

main()



