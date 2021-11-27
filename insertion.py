from numpy import random 
from notherviz import pygameInit
import time


def insertion_sort(A):
    whileiter = 0 
    while whileiter < len(A):
        x = A[whileiter]
        j = whileiter - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x
        whileiter += 1 
        pygameInit(A)
        time.sleep(0.05)
    return A

if __name__ == "__main__":
    A = []
    for i in range(100): 
        A.append(random.randint(1000))

    print(A)

    insertion_sort(A)
