#  File: ERsim.py
#  Description: homework 7
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 10/30/15
#  Date Last Modified: 10/30/15

#create object for queue 
class Queue(object):

	def __init__(self):

		self.items=[]

	def isEmpty(self):

		return self.items == []

	def enqueue(self,item):

		self.items.insert(0,item)

	def dequeue(self):

		return self.items.pop()

	def size(self):

		return len(self.items)

	def peek(self):

		return self.items[-1]

	def __str__(self):

		return str(self.items)

def main():

	#creates different queuing line 
	fairQ = Queue()
	seriousQ = Queue()
	criticalQ = Queue()

	pList = open("ERsim.txt", "r")
	#loop through each line in the text list and execute according to the command
	for line in pList:
		line =line.rstrip("\n")
		conditions = line.split()
		#add patient according to their condition to the queue
		if(conditions[0] == "add"):

			if(conditions[2] == "Critical"):
				print("Add patient " + conditions[1]+ " to Critical queue")
				criticalQ.enqueue(conditions[1])
			elif(conditions[2] == "Serious"):
				print("Add patient " + conditions[1]+ " to Serious queue")
				seriousQ.enqueue(conditions[1])
			else:
				print("Add patient " + conditions[1]+ " to Fair queue")
				fairQ.enqueue(conditions[1])
		#treat the next most urgent patient
		elif("treat next" in line):

			if(criticalQ.size() != 0):
				print("Treating '"+str(criticalQ.peek())+"' from Critical queue")
				criticalQ.dequeue()
				print("Queue are:")
				print("Critical: "+ str(criticalQ))
				print("Serious: "+ str(seriousQ))
				print("Fair: "+ str(fairQ))
			elif(criticalQ.size() == 0 and seriousQ.size() != 0):
				print("Treating '"+str(seriousQ.peek())+ "' from Serious queue")
				seriousQ.dequeue()
				print("Queue are:")
				print("Critical: "+ str(criticalQ))
				print("Serious: "+ str(seriousQ))
				print("Fair: "+ str(fairQ))
			elif(criticalQ.size() == 0 and seriousQ.size() == 0 and fairQ.size() != 0):
				print("Treating '" +str(fairQ.peek()) + "' from Fair queue")
				fairQ.dequeue()
				print("Queue are:")
				print("Critical: "+ str(criticalQ))
				print("Serious: "+ str(seriousQ))
				print("Fair: "+ str(fairQ))
			elif(criticalQ.size() == 0 and str(seriousQ.size()) == 0 and fairQ.size() == 0):
				print("No patients in queues")
		#treat all of the patient in queue according to their urgency
		elif("treat all" in line):

			while(criticalQ.size() != 0 ):
				print("Treating '"+str(criticalQ.peek())+"' from Critical queue")
				criticalQ.dequeue()
				print("Queue are:")
				print("Critical: "+ str(criticalQ))
				print("Serious: "+ str(seriousQ))
				print("Fair: "+ str(fairQ))
			while(seriousQ.size() != 0):
				print("Treating '"+str(seriousQ.peek())+ "' from Serious queue")
				seriousQ.dequeue()
				print("Queue are:")
				print("Critical: "+ str(criticalQ))
				print("Serious: "+ str(seriousQ))
				print("Fair: "+ str(fairQ))
			while(fairQ.size() != 0):
				print("Treating '" +str(fairQ.peek())+ "' from Fair queue")
				fairQ.dequeue()
				print("Queue are:")
				print("Critical: "+ str(criticalQ))
				print("Serious: "+ str(seriousQ))
				print("Fair: "+ str(fairQ))
			if(fairQ.size() == 0 and seriousQ.size() == 0 and criticalQ.size() == 0):
				continue
		#exit and finish
		elif("exit" in line):
			print("Exit")
main()



