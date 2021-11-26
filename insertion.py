from numpy import random 
from notherviz import pygameInit
import time


def insertionsort(A):
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


A = []
for i in range(100): 
    A.append(random.randint(1000))

print(A)

# If no error appears, it has passed the tests
def insertion_test():
    assert insertionsort([1,24,23,14,2]) == [1,2,14,23,24]

insertionsort(A)
insertion_test()