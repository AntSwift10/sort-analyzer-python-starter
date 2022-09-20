# SORT ANALYZER STARTER CODE

#Import Libraries
import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp

# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

#Student Work

#Bubble Sort
def bubbleSort(anArray):
    for n in anArray:
        comparison1 = 0
        comparison2 = 1
        i = 1
        for i in range(len(anArray) - i):
            if anArray[comparison1] > anArray[comparison2]:
                swap(anArray, comparison1, comparison2)
            comparison1 += 1
            comparison2 += 1
        i += 1
        if len(anArray) - i == 0:
            return()

#Selection Sort
def selectionSort(anArray):
    for i in range(len(anArray) - 1):
        #Search for Minimum
        minpos = i
        pos = i
        minval = anArray[minpos]
        for n in range(i, len(anArray)):
            if anArray[n] < minval:
                minpos = pos
                minval = anArray[n]
            pos += 1
        swap(anArray, i, minpos)

#swap Function
def swap(aList, index1, index2):
    aList[index1], aList[index2] = aList[index2], aList[index1]

#Insertion Sort
def insertionSort(anArray):
    for n in range(1, len(anArray)):
        insertVal = anArray[n]
        insertPos = n

        loop = True
        i = 1
        while loop:
            if n - i >= 0:
                if anArray[n - i] > insertVal:
                    #Value Before is Larger Than insertVal
                    anArray[n - i + 1] = anArray[n - i]
                    i += 1
                else:
                    loop = False
            else:
                loop = False

        anArray[n - i + 1] = insertVal

#Test
def test():
    i = 1
    avgtime = 0
    while i <= 20:
        reversedData = loadDataArray("data-files/reversed-values.txt")
        starttime = time.time()
        selectionSort(reversedData)
        endtime = time.time()
        timeelsapsed = endtime - starttime
        print(timeelsapsed)
        avgtime += timeelsapsed
        i += 1
    avgtime /= 20
    print(avgtime)

test()