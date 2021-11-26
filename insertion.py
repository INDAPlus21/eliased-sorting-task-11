from numpy import random 
from vizfunc import pygameInit


def nextiter(whileiter):
    if whileiter < len(A):
        x = A[whileiter]
        j = whileiter - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x


A = []
for i in range(100): 
    A.append(random.randint(1000))

print(A)

pygameInit(nextiter, A)
