import random
import time

first = []
timez = []


def calculateTime():
    timez.append(time.process_time())
def create(amount, array):

    for index in range(0, amount):
        rand = random.randint(0, amount)
        array.append(rand)
def printOut(array):
    print(array)


def selectionSort(array):

        calculateTime()
        for i in range(0, len(array)):

            min = array[i]
            t = i
            index = i;
            for newMin in range(t, len(array)):

                    if(min > array[newMin]):
                        min = array[newMin]
                        index = newMin

            temp = array[i]
            array[i] = array[index]
            array[index] = temp

        calculateTime()
        return print("Bu işlem Selection Sort algoritmasında", len(array), "eleman için", timez[1]-timez[0], "saniye sürdü.")

def BubbleSort(array):

    calculateTime()
    for i in range(0, len(array)):
        for t in range(0, len(array)):
            if(t != len(array)-1):
                if(array[t] > array[t+1]):
                    temp = array[t+1]
                    array[t+1] = array[t]
                    array[t] = temp
            else:
                break
    calculateTime()
    return print("Bu işlem Bubble Sort algoritmasında", len(array), "eleman için", timez[5] - timez[4], "saniye sürdü.")

def InsertionSort(array):
    calculateTime()
    for i in range(1, len(array)):
        for t in range(0, i):
            if(array[i] < array[t]):
                temp = array[t]
                array[t] = array[i]
                array[i] = temp
    calculateTime()
    return print("Bu işlem Insertion Sort algoritmasında", len(array), "eleman için", timez[3]-timez[2], "saniye sürdü.")


create(100000, first)
selectionSort(first)
printOut(first)
InsertionSort(first)
printOut(first)
BubbleSort(first)
printOut(first)