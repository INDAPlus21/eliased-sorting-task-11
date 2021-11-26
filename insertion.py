# INSERTION SORT #
from numpy import random 
from sys import warnoptions
from vizfunc import pygameInit


def nextiter(whileiter):
    if whileiter < len(A):
        print("In while!")
        x = A[whileiter]
        j = whileiter - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x
        #whileiter = whileiter + 1

#wait = True
#whileiter = 1

A = []
for i in range(50): 
    A.append(random.randint(1000)) #[1,5,2,5,6,124,15,2,4,15,2,512,123,5, 1245, 123,3412, 125, 124, 125]

print(A)

pygameInit(nextiter, A)
