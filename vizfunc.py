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
    # i max = 300, (dvs 100 på toppen), om 300/500 = 0.6. 500*0.8 = 300. i = 512, vill ska bli 
    # 400-512*x ska bli 100. 400-512*0.6 = 300
    print(max(A))
    whileiter = 0
    while running:
        screen.fill(background)
        j = 0 
        k += 1
        #print(k)
        if k % 100 == 0 and k != 0: 
            #print(A)
            iterfunc(whileiter)
            whileiter += 1 #You changed this line for the other function
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
            pygame.draw.rect(screen, barcolor, (j*maxlengthfraction, (height-10)-i*maxfraction, maxlengthfraction/2, i*maxfraction))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False