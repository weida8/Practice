class Node(object):

    def __init__(self, initdata):
        self.data = initdata
        self.next= None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def __str__(self):
        return (str(self.data))

class LinkedList(object):

    def __init__(self):
        self.head = None

    def getLength(self):

        current = self.head
        count = 0
        while(current != None):
            count += 1
            current = current.getNext()
        return count

    def addFirst(self, item):

        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def addLast(self, item):

        current = self.head
        previous = None
        if(current == None):
            self.head  = Node(item)
        else:
            while(current != None):
                previous = current
                current = current.getNext()
            temp = Node(item)
            previous.setNext(temp)

    def addInOrder(self, item):

        temp = Node(item)
        current = self.head
        previous = None
        if(current == None):
            self.head = temp
        elif(temp.getData() < current.getData()):
            print("temp:" + temp.getData())
            print("current: " + current.getData())
            temp.setNext(current)
            self.head = temp
        else:
            while(current != None and temp.getData() > current.getData()):
                previous = current
                current = current.getNext()
            previous.setNext(temp)
            temp.setNext(current)
        print(self)

    def findUnordered(self, item):
        current = self.head
        if(current == None):
            return False
        while(current.getNext() != None):
            if(current.getData() == item):
                return True
            current = current.getNext()
        return False

    def findOrdered(self, item):
        current = self.head
        if(current == None):
            return False
        while(current.getNext() != None):
            if(current.getData() == item):
                return True
            current = current.getNext()
        return False

    def delete(self, item):
        current = self.head
        previous = None
        while(current != None):
            if(previous == None and current.getData() == item):
                self.head = current.getNext()
                return
            elif(current.getData() == item):
                previous.setNext(current.getNext())
                return
            previous = current
            current = current.getNext()


    def __str__(self):

        current = self.head
        count = 0
        newString = ""
        while(current != None):
            if(count <= 10):
                newString += str(current.getData()) + "  "
                current = current.getNext()
            else:
                count = 0
                newString += "\n" + str(current.getData()) +  "  "
                current = current.getNext()
        return(newString)

    def copyList(self):
        current = self.head
        if(current == None):
            return None
        copyList = Node(current.getData())
        while(current != None):
            current = current.getNext()
            copyList.setNext(current)
        return copyList

    #def reverseList(self):

    #def sortList(self):

    #def isSorted(self):

    #def isEmpty(self):

    #def isEqual(self):

    #def mergeList(self):

    #def removeDuplicates(self):

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
