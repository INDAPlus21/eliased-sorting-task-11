from numpy import random 
from notherviz import pygameInit

def bogo_sort(A):
    sorted = False
    while not sorted:
        random.shuffle(A)
        sorted = True
        for i in range(len(A)):
            if A[i] < A[i-1] and i-1 >= 0:
                sorted = False
                #print("Not sorted!")
        pygameInit(A)
        if sorted:
            return A 

A = []
for i in range(6): 
    A.append(random.randint(1000))

print(A)

print(bogo_sort(A))

def test_bogo():
    assert bogo_sort([12,51, 124, 23, 5, 2]) == [2,5,12,23,51,124]

test_bogo()
