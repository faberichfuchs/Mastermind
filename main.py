from controller import Controller

if __name__ == '__main__':
    c = Controller()
    c.setup()
    c.view.create_ui()
    c.run_game()
