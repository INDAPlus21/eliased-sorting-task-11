# SELECTION SORT #

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
        #i = i + 1

i = 0

A = []
for i in range(50): 
    A.append(random.randint(1000)) #[1,5,2,5,6,124,15,2,4,15,2,512,123,5, 1245, 123,3412, 125, 124, 125]

pygameInit(loopiter, A)

print(A)

"""import pygame
background = (0,0,0)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Selection sort')
screen.fill(background)
pygame.display.flip()
running = True
while running:
    j = 0 
    for i in A:
        j += 1
        # Rect is "initial coordinates", then how long x, y, to the right, to bottom 
        # If y = 100 and want up to 200 i need to add 200-100
        # If y = 150 and want up to 200 i need to 200-150 
        # If y = 123 and want up to 200, need to add 200-123
        # To get both of them down to 50 i need to do 100-50, 150-50 (the coordinate at the bottom)
        # 200+j*3 
        # Now I need to get 5 to be smaller than 500. Currently it draws from 200+i. 
        # It should draw from 400-i
        pygame.draw.rect(screen, (255, 50, 255), (j*20, 400-i, 10, i))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False"""