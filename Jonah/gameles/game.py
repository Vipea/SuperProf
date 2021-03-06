import pygame
pygame.init () # start pygame library

screen_width = 500
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Jonah")


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 40
height = 60
vel = 5 # how fast we go

isJump = False # see if we are jumping
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    # fill the screen before draw new rectangle
    win.blit(bg, (0,0)) # fill with picture, and position

    # maak een character
    if walkCount + 1 >= 27:
        walkCount = 0 # bc i fgreater than 27 than not enough sprites

    if left:
        win.blit(walkLeft[walkCount//3], (x,y)) #intg div by 3 to get rid of decimals
        walkCount += 1

    if right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1

    else:
        win.blit(char, (x,y))

    # refresh screen to display it on the screen
    pygame.display.update()

# all pygame programs have main loop,
# check for mouse events, movement, collision

run = True # laat het spel rennen
while run:
    clock.tick(27) # fps at 7

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
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < screen_width - width:
        x+= vel
        left = False
        right = True
    else:
        left = False
        right = False # all these to determine sprites
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_UP] and y > 0:
            y -= vel

        if keys[pygame.K_DOWN] and y < screen_height - height:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
            # quadratic function to model jump in order to simulate jump gravity
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg # we gonna start moving with 10**2, next one moves 9 ** 2, etc..
            jumpCount -= 1
        else: # jump has concluded, user can move up and down again
            isJump = False
            jumpCount = 10

    redrawGameWindow()


    # now lets move the rectangle, with keyhold

pygame.quit()
