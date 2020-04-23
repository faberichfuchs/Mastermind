import random


class Mastermind(object):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, controller):
        self.controller = controller
        self.colors = ['RED', 'GREEN', 'BLUE', 'CYAN', 'MAGENTA', 'YELLOW']
        self.tries = 0
        self.comparable = {}
        self.code = []
        for i in range(0, 4):
            self.code = random.choices(self.colors, k=4)
        self.comparable = self.make_comparable(self.code)
        print(self.code)
        # print(self.comparable)

    def check_input(self, guess):
        print(guess)
        response = []
        comparable_guess = self.make_comparable(guess)
        comparable_code = self.comparable.copy()
        print(comparable_code)
        print(comparable_guess)
        for i in range(0, 4):
            if guess[i] == self.code[i]:
                response.append("BLACK")
                comparable_code[guess[i]] = comparable_code[guess[i]] - 1
                comparable_guess[guess[i]] = comparable_guess[guess[i]] - 1
        print(comparable_code)
        if len(response) == 4:
            self.controller.guesser_won()
            return "WIN"
        for color in comparable_guess:
            if color in comparable_code:
                if comparable_guess[color] <= comparable_code[color]:
                    amount = comparable_guess[color]
                else:
                    amount = comparable_code[color]
                for i in range(0, amount):
                    response.append("WHITE")
        self.tries += 1
        print(response)
        return response


    def solve_mystery(self):
        return self.code

    def make_comparable(self, code):
        comparable = {}
        for color in self.colors:
            # print(color)
            for i in range(0, 4):
                if color == code[i]:
                    if color in comparable:
                        comparable.update({color: comparable[color] + 1})
                    else:
                        comparable[color] = 1
        return comparable

