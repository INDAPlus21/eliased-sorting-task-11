from numpy import random
import time 
import pygame
from notherviz import pygameInit
from vizfunc import pygameInit as otherpygameInit

def mergesort(A, startindex):
    if len(A) == 1:
        return A

    left = A[0:int(len(A)/2)]
    right = A[int(len(A)/2):]

    left = mergesort(left, startindex)
    right = mergesort(right, int(len(A)/2))

    global fullarray 

    endofslice = startindex+len(left)
    endofrightslice = int(len(A)/2)+len(right)
    fullarray[startindex:endofslice] = left
    fullarray[int(len(A)/2):endofrightslice] = right 
    pygameInit(fullarray)

    return merge(left, right)


def merge(A, B):
    C = []

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
    
    return C

A = []
for i in range(100): 
    A.append(random.randint(1000)) 
fullarray = A

C = mergesort(A, 0)
running = True
def nothing(no):
    i = 1
while running: 
    otherpygameInit(nothing, C)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False