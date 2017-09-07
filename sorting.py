#  File: sorting.py
#  Description: Homework 10 
#  Student's Name: Wei-Da Pan
#  Student's UT EID: wp3479
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 12/3/15
#  Date Last Modified: 12/3/15

import random
import time
import sys
sys.setrecursionlimit(10000)

#perform bubblesort
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#perform selectionsort
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

#perform insertionsort
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

#perform shellsort
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

#perform gapinsertionsort
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

#perform mergesort
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

#perform quicksort
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

#reads in a list and perform each of the sort functions
#5 times and take the average of the value
#the value is then appended into a final list and returned
def functionCalc(myList):

    resultList = []
    totalTime = 0
    for i in range(5):

        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime

    averagedTime = totalTime/5
    resultList.append(averagedTime)

    for i in range(5):

        startTime = time.perf_counter()
        selectionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime

    averagedTime = totalTime/5
    resultList.append(averagedTime)

    for i in range(5):

        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime

    averagedTime = totalTime/5
    resultList.append(averagedTime)

    for i in range(5):

        startTime = time.perf_counter()
        shellSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime

    averagedTime = totalTime/5
    resultList.append(averagedTime)

    for i in range(5):

        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime

    averagedTime = totalTime/5
    resultList.append(averagedTime)

    for i in range(5):

        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        totalTime += elapsedTime

    averagedTime = totalTime/5
    resultList.append(averagedTime)

    return(resultList)


def main():

    #create three lists with 10 integers, 100, and 1000
    myList10 = [i for i in range(10)]
    myList100 = [i for i in range(100)]
    myList1000 = [i for i in range(1000)]

    #randomize each of the list
    random.shuffle(myList10)
    random.shuffle(myList100)
    random.shuffle(myList1000)

    #call for the function to return the final list for each list 
    randList10 = functionCalc(myList10)
    randList100 = functionCalc(myList100)
    randList1000 = functionCalc(myList1000)

    #sort each list in order
    myList10.sort()
    myList100.sort()
    myList1000.sort()

    #call for the function to return the final list for each of the list
    sortedList10 = functionCalc(myList10)
    sortedList100 = functionCalc(myList100)
    sortedList1000 = functionCalc(myList1000)

    #reverse each list 
    myList10.reverse()
    myList100.reverse()
    myList1000.reverse()

    #call for the function to return the final list for each of the list
    reverseList10 = functionCalc(myList10)
    reverseList100 = functionCalc(myList100)
    reverseList1000 = functionCalc(myList1000)

    #print out the output in the right format
    print("Input type = Random")
    print("                    "+" avg time   "+"avg time   "+ "avg time")
    print("   Sort function    "+"  (n=10)   "+" (n=100)   "+" (n=1000)")
    print("-------------------------------------------------------")
    print("      bubbleSort"+"     {0:<5f}".format(randList10[0])+"   {0:<5f}".format(randList100[0])+"   {0:<5f}".format(randList1000[0]))
    print("   selectionSort"+"     {0:<5f}".format(randList10[1])+"   {0:<5f}".format(randList100[1])+"   {0:<5f}".format(randList1000[1]))
    print("   insertionSort"+"     {0:<5f}".format(randList10[2])+"   {0:<5f}".format(randList100[2])+"   {0:<5f}".format(randList1000[2]))
    print("       shellSort"+"     {0:<5f}".format(randList10[3])+"   {0:<5f}".format(randList100[3])+"   {0:<5f}".format(randList1000[3]))
    print("       mergeSort"+"     {0:<5f}".format(randList10[4])+"   {0:<5f}".format(randList100[4])+"   {0:<5f}".format(randList1000[4]))
    print("       quickSort"+"     {0:<5f}".format(randList10[5])+"   {0:<5f}".format(randList100[5])+"   {0:<5f}".format(randList1000[5]))
    print("")
    print("Input type = Sorted")
    print("                    "+" avg time   "+"avg time   "+ "avg time")
    print("   Sort function    "+"  (n=10)   "+" (n=100)   "+" (n=1000)")
    print("-------------------------------------------------------")
    print("      bubbleSort"+"     {0:<5f}".format(sortedList10[0])+"   {0:<5f}".format(sortedList100[0])+"   {0:<5f}".format(sortedList1000[0]))
    print("   selectionSort"+"     {0:<5f}".format(sortedList10[1])+"   {0:<5f}".format(sortedList100[1])+"   {0:<5f}".format(sortedList1000[1]))
    print("   insertionSort"+"     {0:<5f}".format(sortedList10[2])+"   {0:<5f}".format(sortedList100[2])+"   {0:<5f}".format(sortedList1000[2]))
    print("       shellSort"+"     {0:<5f}".format(sortedList10[3])+"   {0:<5f}".format(sortedList100[3])+"   {0:<5f}".format(sortedList1000[3]))
    print("       mergeSort"+"     {0:<5f}".format(sortedList10[4])+"   {0:<5f}".format(sortedList100[4])+"   {0:<5f}".format(sortedList1000[4]))
    print("       quickSort"+"     {0:<5f}".format(sortedList10[5])+"   {0:<5f}".format(sortedList100[5])+"   {0:<5f}".format(sortedList1000[5]))
    print("")
    print("Input type = Reverse")
    print("                    "+" avg time   "+"avg time   "+ "avg time")
    print("   Sort function    "+"  (n=10)   "+" (n=100)   "+" (n=1000)")
    print("-------------------------------------------------------")
    print("      bubbleSort"+"     {0:<5f}".format(reverseList10[0])+"   {0:<5f}".format(reverseList100[0])+"   {0:<5f}".format(reverseList1000[0]))
    print("   selectionSort"+"     {0:<5f}".format(reverseList10[1])+"   {0:<5f}".format(reverseList100[1])+"   {0:<5f}".format(reverseList1000[1]))
    print("   insertionSort"+"     {0:<5f}".format(reverseList10[2])+"   {0:<5f}".format(reverseList100[2])+"   {0:<5f}".format(reverseList1000[2]))
    print("       shellSort"+"     {0:<5f}".format(reverseList10[3])+"   {0:<5f}".format(reverseList100[3])+"   {0:<5f}".format(reverseList1000[3]))
    print("       mergeSort"+"     {0:<5f}".format(reverseList10[4])+"   {0:<5f}".format(reverseList100[4])+"   {0:<5f}".format(reverseList1000[4]))
    print("       quickSort"+"     {0:<5f}".format(reverseList10[5])+"   {0:<5f}".format(reverseList100[5])+"   {0:<5f}".format(reverseList1000[5]))



main()




