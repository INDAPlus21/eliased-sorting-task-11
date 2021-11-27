from notherviz import pygameInit
from numpy import random
import time

def selection_sort(A):
    i = 0
    while i < len(A)-1:
        minIndex = i
        j = i + 1
        while j < len(A):
            if A[j] < A[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            savedminindex = A[minIndex]
            A[minIndex] = A[i]
            A[i] = savedminindex
        
        i += 1

        # Comment out if you want it to faster
        time.sleep(0.05) 

        pygameInit(A)
    return A

if __name__ == "__main__":
    A = []
    for i in range(100): 
        A.append(random.randint(1000)) 

    print(selection_sort(A))