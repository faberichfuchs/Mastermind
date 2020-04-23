# Import the pygame library and initialise the game engine
import pygame as pg
from mastermind import Mastermind
from view import View


class Controller(object):

    def __init__(self):
        self.pygame = pg
        self.pygame.init()
        self.pygame.font.init()
        self.pygame.display.set_caption("TGMastermind!")
        self.mastermind = Mastermind(self)
        self.view = View(self)
        self.playing = True

    def run_game(self):
        # The loop will carry on until the user exit the game (e.g. clicks the close button).
        carryOn = True

        # The clock will be used to control how fast the screen updates
        clock = self.pygame.time.Clock()

        # -------- Main Program Loop -----------
        while carryOn:
            # --- Main event loop
            for event in self.pygame.event.get():  # User did something
                if event.type == self.pygame.QUIT:  # If user clicked close
                    carryOn = False  # Flag that we are done so we exit this loop
                if self.playing:
                    self.view.confirm.handle_event(event)
                    self.view.solve.handle_event(event)
                    if event.type == self.pygame.MOUSEBUTTONUP:
                        pos = self.pygame.mouse.get_pos()

                        # Color selection
                        self.view.color_selected(pos)
                        # entering a colored pin
                        self.view.pin_entered(pos)
                else:
                    self.view.give_restart_option()
                    # if self.view.confirm.collidepoint(pos):
                    #
                    #if self.view.solve.collidepoint(pos):
                        #colors = self.mastermind.solve_mystery()
                        #self.view.solve_mystery(colors)

                # --- Game logic should go here

                # --- Drawing code should go here
                # First, clear the screen to white.
            self.view.confirm.update()
            self.view.solve.update()

            # --- Go ahead and update the screen with what we've drawn.
            self.pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Once we have exited the main program loop we can stop the game engine:
        self.pygame.quit()

    def confirm_guess(self):
        hints = self.mastermind.check_input(self.view.current_guess)
        if hints != "WIN":
            self.view.add_hints(hints)

    def solve_mystery(self):
        colors = self.mastermind.solve_mystery()
        self.view.solve_mystery(colors)

    def guesser_won(self):
        self.view.add_hints(['BLACK', 'BLACK', 'BLACK', 'BLACK'])
        self.view.guesser_won(self.mastermind.solve_mystery())
