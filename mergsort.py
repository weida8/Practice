import random
def mergeSort(alist):
    if len(alist) > 1:
        print("alist on top: ", alist)
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        print("left half: "+str(lefthalf))
        righthalf = alist[mid:]
        print("right half: "+str(righthalf))

        mergeSort(lefthalf)
        print("alist: ", alist)
        print("len of alist: ", len(alist))
        print("done with left ************************************")
        mergeSort(righthalf)
        print("alist: ", alist)
        print("len of alist: ", len(alist))
        print("done with right ????????????????????????????????????")


        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            print("a")
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            print("b")
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            print("c")
            alist[k] = righthalf[j]
            j += 1
            k += 1

def main():
    myList1000 = [i for i in range(10)]
    random.shuffle(myList1000)
    mergeSort(myList1000)
    print(myList1000)

main()