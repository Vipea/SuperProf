import pygame
pygame.init () # start pygame library

win = pygame.display.set_mode((500, 500))

x = 50
y = 50
width = 40
height = 60
vel = 5 # how fast we go

# all pygame programs have main loop,
# check for mouse events, movement, collision

run = True # laat het spel rennen
while run:
    pygame.time.delay(100) # zodat spel niet te snel gaat

    # check for events, alles wat de gebruiker doet, bijv klikken
    for event in pygame.event.get():
        # kijk voor alles wat er is gebeurd

        #als iemand exit heeft gedaan
        if event.type == pygame.QUIT:
            run = False # dan ga uit de looop

    keys = pygame.key.get_pressed()

    # check wat er gedrukt is
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x+= vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    # fill the screen before draw new rectangle
    win.fill((0,0,0))

    # maak een character
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) # first arg is window, second is color, then dimensions # circle / polygon

    # refresh screen to display it on the screen
    pygame.display.update()

    # now lets move the rectangle, with keyhold

pygame.quit()
