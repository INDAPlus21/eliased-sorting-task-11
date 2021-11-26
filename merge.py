# MERGE SORT (top-down) #

from numpy import random
#from notherviz import #pygameInit
import time 
import asyncio
import pygame
from notherviz import pygameInit
from vizfunc import pygameInit as otherpygameInit

def mergesort(A, startindex):
    global reverse
    if len(A) == 1:
        reverse = True
        return A

    print(startindex)

    #time.sleep(0.05)

    left = A[0:int(len(A)/2)]
    right = A[int(len(A)/2):]

    left = mergesort(left, startindex)
    right = mergesort(right, int(len(A)/2))

    #if reverse == True and len(A) != 1:
    #   pygameInit(left+right)

    global fullarray 

    print(fullarray)
    endofslice = startindex+len(left)
    endofrightslice = int(len(A)/2)+len(right)
    print("start, left right: ", startindex, len(left), len(right), left, right, endofslice, endofrightslice, len(fullarray))
    #if len(left)+len(right) != len(fullarray):
    fullarray[startindex:endofslice] = left
    fullarray[int(len(A)/2):endofrightslice] = right 
    pygameInit(fullarray)

    #time.sleep(0.0001)
    ##pygameInit(A)

    return merge(left, right)


def merge(A, B):
    print("in merge!!!")
    global currentlength
    #print(len(A), len(B))
    if not (len(A) > currentlength + 1 or len(B) > currentlength +1):
        currentlength = max(len(A), len(B))
        print(currentlength)
    C = []

    while len(A) > 0 and len(B) > 0:
        #if len(C):
            ##pygameInit(C)
        if A[0] > B[0]:
            C.append(B[0])
            B.pop(0)
        else:
            C.append(A[0]) 
            A.pop(0) 

    #pygameInit(C)
        
    while len(A) > 0:
        #pygameInit(C)
        C.append(A[0]) 
        A.pop(0)
    
    #pygameInit(C)
    
    while len(B) > 0:
        #pygameInit(C)
        C.append(B[0]) 
        B.pop(0)  

    #pygameInit(C)
    whattodisplay = C
    time.sleep(0.05)
    running = False

    global toplevela 
    toplevela = toplevela[len(A):]
    #pygameInit(C) #"""toplevela""")
    
    return C

A = []
for i in range(50): 
    A.append(random.randint(1000)) #[1,5,2,5,6,124,15,2,4,15,2,512,123,5, 1245, 123,3412, 125, 124, 125]
#A = [4, 0, 6, 1, 5, 2, 3]
fullarray = A
reverse = False

currentlength = 1
realarray = []
toplevela = A
C = mergesort(A, 0)
running = True
def nothing(no):
    i = 1
while running: 
    print(C)
    otherpygameInit(nothing, C)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

"""background = (0,0,0)
barcolor = (255, 50, 255)
(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Selection sort')
screen.fill(background)
pygame.display.flip()
running = True
k = 0 
maxfraction = (height-30)/max(A)
maxlengthfraction = width/len(A)
# i max = 300, (dvs 100 på toppen), om 300/500 = 0.6. 500*0.8 = 300. i = 512, vill ska bli 
# 400-512*x ska bli 100. 400-512*0.6 = 300
#print(max(A))
whileiter = 0
#while running:
screen.fill(background)
j = 0 
k += 1
#print(k)"""
"""if k % 100 == 0: 
    whileiter += 1
    #print(A)
    iterfunc(whileiter)"""

"""print(mergesort(A))

whattodisplay = A

while running: 
    for i in whattodisplay:
        j += 1
        # Rect is "initial coordinates", then how long x, y, to the right, to bottom 
        # If y = 100 and want up to 200 i need to add 200-100
        # If y = 150 and want up to 200 i need to 200-150 
        # If y = 123 and want up to 200, need to add 200-123
        # To get both of them down to 50 i need to do 100-50, 150-50 (the coordinate at the bottom)
        # 200+j*3 
        # Now I need to get 5 to be smaller than 500. Currently it draws from 200+i. 
        # It should draw from 400-i
        pygame.draw.rect(screen, barcolor, (j*maxlengthfraction, (height-10)-i*maxfraction, maxlengthfraction/2, i*maxfraction))
    pygame.display.flip()"""
"""for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False"""
""""""
