import copy
import sys
class State:
	#create objects 
	def __init__(self, jugs, steps, history): 
		self.jugs = copy.copy(jugs)
		self.steps = steps
		self.history = copy.copy(history)
		self.solution = False 
		

#check to see if the jug is empty
def isEmpty(index, jugs):
	return jugs[index] == 0

#check to see if the jug is full
def isFull(index, jugs, capacity):
	return jugs[index] == capacity[index]

#check to see the current state is the solution
def isGoal(state, jugNumber, amount): #amount is the integer for the number of gallon in desired jug
	if(state.jugs[jugNumber] == amount):
		state.solution = True
		return True 
	else:
		return False

#recusively check through all the options per level
def successors(states, capacity, amount, jugNumber):
	branchList=[]
	#loop through all the states
	for state in states:
		#fill the jug if it's not full
		for index in range(len(state.jugs)):
			if not isFull(index, state.jugs, capacity):
				newState = State(state.jugs, state.steps, state.history)
				newState.jugs[index] = capacity[index]
				newState.steps += 1
				if newState.jugs in newState.history:
					continue
				else:
					newState.history.append(newState.jugs)
					branchList.append(newState)
					
		#empty the jug if it's not empty
		for index in range(len(state.jugs)):
			if not isEmpty(index, state.jugs):
				newState = State(state.jugs, state.steps, state.history)
				newState.jugs[index] = 0
				newState.steps += 1
				if newState.jugs in newState.history:
					continue
				else:
					newState.history.append(newState.jugs)
					branchList.append(newState)

		#pour from one jug to another using a nested loop so it will take turn to pour into the other jugs
		for index in range(len(state.jugs)):
			if not isEmpty(index, state.jugs):
				for index_2 in range(len(state.jugs)):
					if(index != index_2):
						newState = State(state.jugs, state.steps, state.history)
						if(newState.jugs[index] <= (capacity[index_2] - newState.jugs[index_2])):
							newState.jugs[index_2] += newState.jugs[index]
							newState.jugs[index] = 0
						else:
							newState.jugs[index] -= (capacity[index_2]-newState.jugs[index_2])
							newState.jugs[index_2] = capacity[index_2]
						newState.steps += 1
						if newState.jugs in newState.history:
							continue
						else:
							newState.history.append(newState.jugs)
							branchList.append(newState)

	#check to see which state saved inside all the current level are solutions
	#it is a solution then return the state, if we are at step 50+ then return did not find solution
	for state in branchList:
		if(isGoal(state, jugNumber, amount) ):
			return(state)
		elif state.steps > 50:
			print("Did not find solution")
			sys.exit(0)
	return(successors(branchList, capacity, amount, jugNumber))

def main():

	#read in file
	inFile = open("test.txt", "r")
	jugs = inFile.readline().rstrip("\n")
	jugList = jugs.split()
	capacity =[]
	for jug in jugList:
		capacity.append(int(jug))

	boundary = inFile.readline().rstrip("\n")
	boundList = boundary.split()
	rules = []
	for i in boundList:
		rules.append(int(i))

	#set the rule for the final solution
	amount = rules[1]
	jugNumber = rules[0]-1

	#initiating the initial capacity 
	initial = [0]*len(capacity)
	steps = 0
	history =[]
	s = [State(initial, steps, history)]
	result = successors(s, capacity, amount, jugNumber)

	#print out the solution one row at a time
	if(result.solution):
		for i in result.history:
			print(i)
	else:
		print("Did not find solution")


	inFile.close()

main()






