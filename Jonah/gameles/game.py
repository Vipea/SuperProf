import pygame
pygame.init () # start pygame library

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))

x = 50
y = 50
width = 40
height = 60
vel = 5 # how fast we go

isJump = False # see if we are jumping
jumpCoundt = 10

# all pygame programs have main loop,
# check for mouse events, movement, collision

run = True # laat het spel rennen
while run:
    pygame.time.delay(20) # zodat spel niet te snel gaat

    # check for events, alles wat de gebruiker doet, bijv klikken
    for event in pygame.event.get():
        # kijk voor alles wat er is gebeurd

        #als iemand exit heeft gedaan
        if event.type == pygame.QUIT:
            run = False # dan ga uit de looop

    keys = pygame.key.get_pressed()

    # check wat er gedrukt is

    if keys[pygame.K_LEFT] and x > 0: # see if greater than 0 bc we dont want to move it off the screen, but then we can still move 5 pixels to -5 bc it is still allowed to move
        x -= vel

    if keys[pygame.K_RIGHT] and x < screen_width - width:
        x+= vel

    if keys[pygame.K_UP]:
        y -= vel and y > 0

    if keys[pygame.K_DOWN]:
        y += vel and y < screen_height - height

    if keys[pygame.K_SPACE]:
        pass

    # fill the screen before draw new rectangle
    win.fill((0,0,0))

    # maak een character
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) # first arg is window, second is color, then dimensions # circle / polygon

    # refresh screen to display it on the screen
    pygame.display.update()

    # now lets move the rectangle, with keyhold

pygame.quit()
