# Import the pygame library and initialise the game engine
from builtins import range

import pygame

pygame.init()
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 0, 255)
LIGHT_BLUE = (159, 255, 248)
PINK = (0, 0, 255)
GREY = (128, 128, 128)
DARK_GREY = (96, 96, 96)

SILVER = (192, 192, 192)

# Open a new window
size = (300, 600)
screen = pygame.display.set_mode(size)
screenWidth = screen.get_rect().width
screenHeight = screen.get_rect().height
pygame.display.set_caption("Who is the true TGMastermind?")

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
        pygame.draw.circle(screen, SILVER, ((int(screenWidth / 2) - 80) + 50 * i, 70), 20, 0)
    # Background rect
    pygame.draw.rect(screen, GREY, [0, 100, screenWidth, screenHeight - 100], 0)

    #10 rows fo payling field
    for i in range(0, 11):
        pygame.draw.rect(screen, WHITE, [10, 110 + i * 40, 30, 30], 0)


    """
    pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
"""
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
