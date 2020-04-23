from tkinter import messagebox, Tk
from button import Button


class View:

    def __init__(self, controller):
        self.controller = controller
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.CYAN = (0, 255, 255)
        self.MAGENTA = (255, 0, 255)
        self.GREY = (128, 128, 128)
        self.DARK_GREY = (96, 96, 96)
        self.SILVER = (192, 192, 192)
        self.colors = {'RED': (255, 0, 0), 'GREEN': (0, 255, 0), 'BLUE': (0, 0, 255), 'CYAN': (0, 255, 255),
                       'MAGENTA': (255, 0, 255), 'YELLOW': (255, 255, 0)}
        self.screen = self.controller.pygame.display.set_mode((280, 700))
        self.screenWidth = self.screen.get_rect().width
        self.screenHeight = self.screen.get_rect().height
        self.mystery = []
        self.numbers = []
        self.guesses = []
        self.remaining_guesses = 12
        self.current_guess = []
        self.hints = []
        self.selectableColors = {}
        self.confirm = 0
        self.solve = 0
        self.selected_color = ""
        self.temp = []

    def create_ui(self):
        myfont = self.controller.pygame.font.SysFont('Raleway', 50)
        textsurface = myfont.render('MASTERMIND', True, self.WHITE)

        self.screen.fill(self.GREY)

        # MASTERMIND text
        self.screen.blit(textsurface, (self.screenWidth / 2 - (textsurface.get_rect().width / 2), 10))

        # 4 Mysterious Dots
        for i in range(0, 4):
            self.mystery.append(
                self.controller.pygame.draw.circle(self.screen, self.SILVER,
                                                   ((int(self.screenWidth / 2) - 70) + 50 * i, 70), 20,
                                                   0))
        # Background rect
        self.controller.pygame.draw.rect(self.screen, self.DARK_GREY,
                                         [0, 100, self.screenWidth, self.screenHeight - 100], 0)

        # 12 rows for playing field
        for i in range(0, 13):
            # Number rects
            self.numbers.append(
                self.controller.pygame.draw.rect(self.screen, self.WHITE, [10, 110 + i * 40, 30, 30], 0))
            # 4 empty color selections for the guessing player
            for j in range(0, 4):
                self.temp.append(
                    self.controller.pygame.draw.circle(self.screen, self.SILVER, (70 + 50 * j, 125 + i * 40), 15, 0))
                # print(temp)
            # Border for the hints
            self.guesses.append(self.temp.copy())
            # print(guesses)
            self.temp.clear()
            self.controller.pygame.draw.rect(self.screen, self.WHITE, [self.screenWidth - 35, 110 + i * 40, 30, 30], 1)
            # 4 hints from the mastermind to the guesser
            for j in range(0, 4):
                if j < 2:
                    self.temp.append(
                        self.controller.pygame.draw.circle(self.screen, self.SILVER,
                                                           (self.screenWidth - 27 + 14 * j, 119 + i * 40), 4, 1))
                else:
                    self.temp.append(
                        self.controller.pygame.draw.circle(self.screen, self.SILVER,
                                                           (self.screenWidth - 27 + 14 * (j - 2), 131 + i * 40), 4, 1))
            self.hints.append(self.temp.copy())
            self.temp.clear()
        # 6 colors that can be selected
        self.selectableColors.update(
            {'RED': self.controller.pygame.draw.circle(self.screen, self.RED,
                                                       (int(self.screenWidth / 6) * 1 - 18, self.screenHeight - 55), 15,
                                                       0)})
        self.selectableColors.update(
            {'GREEN': self.controller.pygame.draw.circle(self.screen, self.GREEN,
                                                         (int(self.screenWidth / 6) * 2 - 18, self.screenHeight - 55),
                                                         15, 0)})
        self.selectableColors.update(
            {'BLUE': self.controller.pygame.draw.circle(self.screen, self.BLUE,
                                                        (int(self.screenWidth / 6) * 3 - 18, self.screenHeight - 55),
                                                        15, 0)})
        self.selectableColors.update(
            {'CYAN': self.controller.pygame.draw.circle(self.screen, self.CYAN,
                                                        (int(self.screenWidth / 6) * 4 - 18, self.screenHeight - 55),
                                                        15, 0)})
        self.selectableColors.update(
            {'MAGENTA': self.controller.pygame.draw.circle(self.screen, self.MAGENTA,
                                                           (int(self.screenWidth / 6) * 5 - 18, self.screenHeight - 55),
                                                           15, 0)})
        self.selectableColors.update(
            {'YELLOW': self.controller.pygame.draw.circle(self.screen, self.YELLOW,
                                                          (int(self.screenWidth / 6) * 6 - 18, self.screenHeight - 55),
                                                          15, 0)})
        # confirm button
        self.confirm = Button("Confirm Guess", 10, self.screenHeight - 35, int(self.screenWidth / 2) - 15, 30, command=self.confirm_guess)
        self.confirm.draw(self.screen)
        # solve button
        self.solve = Button("Show Solution", int(self.screenWidth / 2) + 5, self.screenHeight - 35, int(self.screenWidth / 2) - 15, 30,
                              command=self.confirm_solve)
        self.solve.draw(self.screen)


    def color_selected(self, pos):
        for c in self.colors:
            for _ in self.selectableColors:
                if self.selectableColors[c].collidepoint(pos):
                    self.selected_color = c
        print(self.selected_color)

    def pin_entered(self, pos):
        if not self.current_guess:
            for i in range(0, 4):
                self.current_guess.append("")
        else:
            color = self.guesses[self.remaining_guesses]
            for i in range(0, 4):
                if color[i].collidepoint(pos):
                    if self.selected_color != "":
                        self.controller.pygame.draw.circle(self.screen, self.colors[self.selected_color],
                                                           (color[i].left + 15, color[i].top + 15), 15)
                        self.current_guess[i] = self.selected_color
        # print(self.current_guess)

    def confirm_guess(self):
        if self.current_guess:
            self.controller.confirm_guess()

    def confirm_solve(self):
        self.controller.solve_mystery()

    def solve_mystery(self, colors):
        for i in range(0, 4):
            self.controller.pygame.draw.circle(self.screen, self.colors[colors[i]],
                                               (self.mystery[i].left + 20, self.mystery[i].top + 20), 20)

    def add_hints(self, hints):
        print(self.hints)
        print(self.hints[self.remaining_guesses][0])
        for i in range(0, len(hints)):
            if hints[i] == 'BLACK':
                self.controller.pygame.draw.circle(self.screen, self.BLACK, (
                    self.hints[self.remaining_guesses][i].left + 4, self.hints[self.remaining_guesses][i].top + 4), 5,
                                                   0)
            else:
                self.controller.pygame.draw.circle(self.screen, self.WHITE, (
                    self.hints[self.remaining_guesses][i].left + 4, self.hints[self.remaining_guesses][i].top + 4), 5,
                                                   0)
        self.remaining_guesses -= 1

    def guesser_won(self, colors):
        self.solve_mystery(colors)
        Tk().wm_withdraw()  # to hide the main window
        # messagebox.showinfo('Continue', 'OK')
        messagebox._show('Victory', 'Congratulations!\nYou are the TGMastermind :)')

    def restart(self):
        print("Hallo")

    def give_restart_option(self):
        self.restart = Button("Restart game?", 10, self.screenHeight - 35, int(self.screenWidth / 2) - 15, 30,
                              command=self.restart)
        self.restart.draw(self.screen)
