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

if __name__ == "__main__":
    A = []
    for i in range(6): 
        A.append(random.randint(1000))

    print(A)

    print(bogo_sort(A))

