import pygame

def pygameInit(A): 
    background = (0,0,0)
    barcolor = (255, 50, 255)
    (width, height) = (500, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Sort')
    screen.fill(background)
    pygame.display.flip()
    maxfraction = (height-30)/max(A)
    maxlengthfraction = width/len(A)
    screen.fill(background)
    j = 0 
    for i in A:
        # Rect is "initial coordinates", then how long x, y, to the right, to bottom 
        pygame.draw.rect(screen, barcolor, (j*maxlengthfraction, (height-10)-i*maxfraction, maxlengthfraction/2, i*maxfraction))
        j += 1
    pygame.display.flip()