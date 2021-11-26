import pygame

def pygameInit(iterfunc, A): 
    background = (0,0,0)
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
    whileiter = 0
    while running:
        screen.fill(background)
        j = 0 
        k += 1
        if k % 100 == 0 and k != 0: 
            iterfunc(whileiter)
            whileiter += 1 
        for i in A:
            j += 1
            # Rect is "initial coordinates", then how long x, y, to the right, to bottom 
            pygame.draw.rect(screen, barcolor, (j*maxlengthfraction, (height-10)-i*maxfraction, maxlengthfraction/2, i*maxfraction))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False