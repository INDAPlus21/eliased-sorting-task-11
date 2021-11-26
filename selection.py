import pygame
from vizfunc import pygameInit
from numpy import random

def loopiter(i):
    if i < len(A)-1:
        minIndex = i
        j = i + 1
        print("first j: ", j)
        while j < len(A):
            if A[j] < A[minIndex]:
                print("hello")
                minIndex = j
            j += 1
        if minIndex != i:
            savedminindex = A[minIndex]
            A[minIndex] = A[i]
            A[i] = savedminindex

i = 0

A = []
for i in range(100): 
    A.append(random.randint(1000)) 

pygameInit(loopiter, A)