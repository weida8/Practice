#  File: TreeConvert.py
#  Description: HW 9 
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 11/19/15
#  Date Last Modified: 11/20/15

#class that create a binary tree 
class BinaryTree(object):

	def __init__(self, initVal):

		self.data = initVal
		self.left = None
		self.right = None

	def getLeftChild(self):

		return self.left

	def getRightChild(self):

		return self.right

	def setRootVal(self, value):

		self.data = value

	def getRootVal(self):

		return(self.data)

	def insertLeft(self, newVal):

		n = BinaryTree(newVal)
		n.left = self.left
		self.left = n

	def insertRight(self, newVal):

		n = BinaryTree(newVal)
		n.right = self.right
		self.right = n

	#staticmethod is needed that in order to make sure 
	#that it not the first argument taken in
	@staticmethod
	def convert(pyList):

		if(pyList == []):
			return(None)
		else:
			#recursively converting the list into the binary tree
			newTree = BinaryTree(pyList[0])
			newTree.left=BinaryTree.convert(pyList[1])
			newTree.right=BinaryTree.convert(pyList[2])
			return(newTree)

	@staticmethod
	#reordering the list into and printing it out in inorder order
	def inorder(tree):

		if(tree != None):
			BinaryTree.inorder(tree.getLeftChild())
			print(tree.getRootVal(), end = " ")
			BinaryTree.inorder(tree.getRightChild())

	#reordering the list into and printing it out in preorder order
	@staticmethod
	def preorder(tree):

		if(tree):
			print(tree.getRootVal(), end = " ")
			BinaryTree.preorder(tree.getLeftChild())
			BinaryTree.preorder(tree.getRightChild())

	#reordering the list into and printing it out in postorder order
	@staticmethod
	def postorder(tree):

		if(tree != None):
			BinaryTree.postorder(tree.getLeftChild())
			BinaryTree.postorder(tree.getRightChild())
			print(tree.getRootVal(), end = " ")

	def __str__(self):

		return(str(self.data))




def main():

	#take in line to line and calling each order method to print it out
	inFile = open("treedata.txt", "r")
	for line in inFile: 
		newList = eval(line)
		print("\nlist: " + str(newList))
		newTree = BinaryTree.convert(newList)
		print("inorder: " )
		BinaryTree.inorder(newTree)
		print("\npreorder: ")
		BinaryTree.preorder(newTree)
		print("\npostorder: ")
		BinaryTree.postorder(newTree)
		print("\n")

main()