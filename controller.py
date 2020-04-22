# Import the pygame library and initialise the game engine

import pygame as pygame

from mastermind import Mastermind
from view import View

pygame.init()
pygame.font.init()
pygame.display.set_caption("TGMastermind!")

mastermind = Mastermind()
view = View(pygame)
view.create_ui()
print(view)
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
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # Color selection
            view.color_selected(pos)
            # entering a colored pin
            view.pin_entered(pos)
            if view.confirm.collidepoint(pos):
                hints = mastermind.check_input(view.current_guess)
                view.remaining_guesses -= 1
                view.add_hints(hints)
            if view.solve.collidepoint(pos):
                colors = mastermind.solve_mystery()
                view.solve_mystery(colors)

        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white.

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
