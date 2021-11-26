from numpy import random
import time 
from notherviz import pygameInit

def mergesort(A, startindex, fullarray):
    if len(A) == 1:
        return A

    left = A[0:int(len(A)/2)]
    right = A[int(len(A)/2):]

    left = mergesort(left, startindex, fullarray)
    right = mergesort(right, int(len(A)/2), fullarray)

    endofslice = startindex+len(left)
    endofrightslice = int(len(A)/2)+len(right)
    fullarray[startindex:endofslice] = left
    fullarray[int(len(A)/2):endofrightslice] = right 
    pygameInit(fullarray)

    return merge(left, right, fullarray)


def merge(A, B, fullarray):
    C = []

    printfinal = False
    if len(A) + len(B) == len(fullarray):
        printfinal = True

    while len(A) > 0 and len(B) > 0:
        if A[0] > B[0]:
            C.append(B[0])
            B.pop(0)
        else:
            C.append(A[0]) 
            A.pop(0) 
        
    while len(A) > 0:
        C.append(A[0]) 
        A.pop(0)
        
    while len(B) > 0:
        C.append(B[0]) 
        B.pop(0)  

    time.sleep(0.05)

    if printfinal:
        pygameInit(C)
    
    return C

A = []
for i in range(100): 
    A.append(random.randint(1000)) 

C = mergesort(A, 0, A)

def merge_test():
    assert mergesort([1,4,512,25,2], 0, [1,4,512,25,2]) == [1,2,4,25,512]

merge_test()