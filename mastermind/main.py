# Import the pygame library and initialise the game engine
from builtins import range

import pygame

pygame.init()
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREY = (128, 128, 128)
DARK_GREY = (96, 96, 96)
SILVER = (192, 192, 192)

# Open a new window
size = (280, 620)
screen = pygame.display.set_mode(size)
screenWidth = screen.get_rect().width
screenHeight = screen.get_rect().height
pygame.display.set_caption("TGMastermind!")
numbers = []
guesses = [[]]
hints = [[]]
colors = []
confirm = 0
temp = []

myfont = pygame.font.SysFont('Raleway', 50)
textsurface = myfont.render('MASTERMIND', True, WHITE)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop

        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.
    screen.fill(DARK_GREY)

    # MASTERMIND text
    screen.blit(textsurface, (screenWidth / 2 - (textsurface.get_rect().width / 2), 10))

    # 4 Mysterious Dots
    for i in range(0, 4):
        pygame.draw.circle(screen, SILVER, ((int(screenWidth / 2) - 70) + 50 * i, 70), 20, 0)
    # Background rect
    pygame.draw.rect(screen, GREY, [0, 100, screenWidth, screenHeight - 100], 0)

    # 10 rows for payling field
    for i in range(0, 11):
        # Number rects
        numbers.append(pygame.draw.rect(screen, WHITE, [10, 110 + i * 40, 30, 30], 0))
        # 4 empty color selections for the guessing player
        for j in range(0, 4):
            temp.append(pygame.draw.circle(screen, SILVER, (70 + 50 * j, 125 + i * 40), 15, 0))
        # Border for the hints
        guesses.append(temp)
        temp.clear()
        pygame.draw.rect(screen, WHITE, [screenWidth - 35, 110 + i * 40, 30, 30], 1)
        # 4 hints from the mastermind to the guesser
        for j in range(0, 4):
            if j < 2:
                temp.append(pygame.draw.circle(screen, SILVER, (screenWidth - 27 + 14 * j, 118 + i * 40), 5, 0))
            else:
                temp.append(pygame.draw.circle(screen, SILVER, (screenWidth - 27 + 14 * (j - 2), 132 + i * 40), 5, 0))
        hints.append(temp)
        temp.clear()
    # 6 colors that can be selected
    colors.append(pygame.draw.circle(screen, RED, (int(screenWidth / 6) * 1 - 18, screenHeight - 55), 15, 0))
    colors.append(pygame.draw.circle(screen, BLUE, (int(screenWidth / 6) * 2 - 18, screenHeight - 55), 15, 0))
    colors.append(pygame.draw.circle(screen, GREEN, (int(screenWidth / 6) * 3 - 18, screenHeight - 55), 15, 0))
    colors.append(pygame.draw.circle(screen, YELLOW, (int(screenWidth / 6) * 4 - 18, screenHeight - 55), 15, 0))
    colors.append(pygame.draw.circle(screen, CYAN, (int(screenWidth / 6) * 5 - 18, screenHeight - 55), 15, 0))
    colors.append(pygame.draw.circle(screen, MAGENTA, (int(screenWidth / 6) * 6 - 18, screenHeight - 55), 15, 0))
    # confirm button
    confirm = pygame.draw.rect(screen, WHITE, [10, screenHeight - 35, int(screenWidth/2) - 15, 30], 0)
    # solve button
    solve = pygame.draw.rect(screen, WHITE, [int(screenWidth/2) + 5, screenHeight - 35, int(screenWidth/2) - 10, 30], 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
