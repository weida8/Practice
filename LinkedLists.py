#  File: LinkedLists.py
#  Description: HW 8
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479 
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 11/11/15
#  Date Last Modified: 11/13/15

#creates class to create Node object
class Node(object):

   def __init__(self, initdata):

   	self.data = initdata
   	self.next = None

   def getData(self):

   	return self.data

   def getNext(self):

   	return self.next

   def setData(self, newdata):

   	self.data = newdata

   def setNext(self, newnext):

   	self.next = newnext

   def __str__(self):

      return(str(self.data))

#create a linked list object 
class LinkedList(object):

   def __init__(self):

   	self.head = None

   #get the length of the linked list
   def getLength(self):

   	current = self.head
   	count = 0 
   	while(current != None):
   		count += 1
   		current = current.getNext()
   	return(count)

   #add a new Node to the front of the list
   def addFirst(self, item):

   	temp = Node(item)
   	temp.next = self.head
   	self.head = temp

   #add a new Node to the back of the list
   def addLast(self, item):

      current = self.head
      previous = None
      if(current == None):
         self.head = Node(item)
      else:
         while(current != None):
            previous = current
            current = current.getNext()
         temp = Node(item)
         previous.next = temp

   #goes through the linked list that is ordered and add the new Node to
   #right place according to the order in the list
   def addInOrder(self, item):

      current = self.head
      previous = None
      temp = Node(item)
      if(current == None):
         self.head = Node(item)
      elif(temp.getData()<self.head.getData()):
         temp.next = self.head
         self.head = temp

      else:
         while(current != None and temp.getData()>current.getData()):
            previous = current
            current = current.getNext()
         previous.next = temp
         temp.next = current

   #check in an unordered list to see if the item is in one of the node in the list
   def findUnordered(self, item):

      current = self.head
      found = False
      while(current != None and not found):
         if(current.getData() == item):
            return(not found)
         else:
            current = current.getNext()
      return(found)

   #check in a ordered list to see if the item is in one of the node in the list
   def findOrdered (self, item): 

      current = self.head
      found = False
      while(current != None and not found and item>=current.getData()):
      	if(current.getData() == item):
            return(not found)
      	else:
      		current = current.getNext()
      return(found)

   #find and delete the item in the list
   def delete (self, item):

      current = self.head
      previous = None
      found = False
      if(current.getData() == item):
         current.next = current.getNext()
         found = True
      while(current != None and not found):
      	if(current.getData() == item):
      		found = True
      		previous.next = current.next
      	else:
      		previous = current
      		current = current.getNext()
      return(found)

   #create a string of the list 
   def __str__ (self):

      current = self.head
      count = 0
      newstring = ""
      while(current != None):
         if(count<=10):
            newstring += str(current.getData())+"  "
            current = current.getNext()
         else:
            count = 0 
            newstring += "\n"+str(current.getData)+"  "
            current = current.getNext()
      return(newstring)

   #copy the linked list over to another list 
   def copyList (self):

      current = self.head
      newList = LinkedList()
      newList.head = Node(current.data)
      current = current.getNext()
      if(current == None):
         return(newList)
      else:
         while(current != None):
            if(current.getNext() == None):
               newList.addLast(current.data)
               return(newList)
            else:
               newList.addLast(current.data) 
               current = current.getNext() 

   #reverse the list and return it 
   def reverseList (self): 

      current = self.head
      revList = LinkedList()
      revList.head = Node(current.getData())
      while(current != None):
         current = current.getNext()
         if(current.getNext() == None):
            revList.addFirst(current.getData())
            return(revList)
         else:
            revList.addFirst(current.getData())

   #sort the linked list in ascending order
   def sortList (self): 

      current = self.head
      sortedList = LinkedList()
      sortedList.head = Node(current.data)
      current = current.getNext()
      while(current != None):
         newListCurrent = sortedList.head
         if(newListCurrent == None):
            sortedList.head = Node(current.data)
            break
         previous = None
         while(newListCurrent != None):
            if(current.data<newListCurrent.data):
               if(previous == None):
                  previous = sortedList.head
                  sortedList.head = Node(current.data)
                  sortedList.head.next = previous
               else:
                  previous.next = Node(current.data)
                  previous.next.next = newListCurrent
               break
            else:
               previous = newListCurrent
               newListCurrent = newListCurrent.getNext()
               if (newListCurrent == None):
                  previous.next = Node(current.data)
                  break
         current = current.getNext()
      return(sortedList) 

        # Return a new linked list that contains the elements of the
        #    original list, sorted into ascending (alphabetical) order.
        #    Do NOT use a sort function:  do this by iteratively
        #    traversing the first list and then inserting copies of
        #    each item into the correct place in the new list.

   #loop through each of the node in the list to see if it is sorted
   def isSorted (self):

      current = self.head
      previous = None
      checker = True
      while(current != None):
         if(current.getNext() == None):
            return(checker)
         if(previous == None):
            previous = current 
            current = current.getNext()
         else:
            previous = current
            current = current.getNext()
         if(current.data<previous.data):
            return(not checker)
      return(checker)

   #check to see if the list is empty
   def isEmpty (self): 

      return(self.head == None)

   #take a new linked list and merge it into the original list
   def mergeList (self, b): 

      current1 = self.head
      current2 = b.head
      mergedList = LinkedList()
      mergedList.head = Node(current1.data)
      while(current1 != None):
         if(current1.getNext() == None):
            break
         else:
            current1 = current1.getNext()
            mergedList.addInOrder(current1.data)
      while(current2 != None):
         if(current2.getNext() == None):
            return(mergedList)
         else:
            mergedList.addInOrder(current2.data)
            current2 = current2.getNext()

   #loop through both lists and check nodes at the same position 
   #of each list and see if they are the same
   def isEqual (self, b):

      current1 = self.head
      current2 = b.head
      checker = True
      if(self.getLength() != b.getLength()):
         return not checker
      elif(self.getLength() == 0 and b.getLength() == 0):
         return checker
      else:
         while(current1 != None and current2 != None):
            if(current1.getNext() == None):
               if(current1.getData() != current2.getData()):
                  return not checker
               else:
                  return checker
            elif(current1.getData() != current2.getData()):
               return not checker
            current1 = current1.getNext()
            current2 = current2.getNext()

   #check to see if there're any duplicates, if there is, remove it
   def removeDuplicates (self):

      current = self.head
      previous = None
      while(current != None):
         if(current.getNext() == None):
            return(self)
         else:
            checkCurrent = current.getNext()
         while(checkCurrent != None):
            if(current.data == checkCurrent.data):
               previous.next = current.next
               checkCurrent = checkCurrent.getNext()
            checkCurrent = current.getNext()
         previous = current
         current = current.getNext()
      return(self)

        # Modify a list, keeping only the first occurrence of an element
        #    and removing all duplicates.  Do not change the order of
        #    the remaining elements.    

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of sortList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto!")
   
   print ("   Original list:")
   print (planets)
   print ("   Sorted list:")
   sortedPlanets = planets.sortList()
   print (sortedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isSorted:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Sorted: ", planets.isSorted())
   sortedPlanets = planets.sortList()
   print ("   After sort:")
   print (sortedPlanets)
   print ("   Sorted: ", sortedPlanets.isSorted())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
