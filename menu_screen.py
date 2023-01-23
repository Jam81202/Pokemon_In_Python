from classes import *

def menu():

    in_menu = True
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WIN.fill(BLACK)

        LOAD_SAVE_BUTTON = Button("L: Loading Save", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy",
                                        feedback="Returning to Main Menu")

        SAVE_GAME_BUTTON = Button("S: Save Game", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy",
                                        feedback="Saving...")

        QUIT_BUTTON = Button("Q: Quit Game", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy",
                                        feedback="Closing Game")

        BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            in_menu = False
            print(BACK_BUTTON.feedback)

        if keys[pygame.K_l]:
            in_menu = False
            print(LOAD_SAVE_BUTTON.feedback)
            LAST_LOCATION = pickle.load(open("lastlocation_savefile.pickle", "rb"))
            LAST_POKECENTER = pickle.load(open("lastpokecenter_savefile.pickle", "rb"))
            trainer_status = pickle.load(open("trainerstatus_savefile.pickle", "rb"))
            break

        if keys[pygame.K_s]:
            in_menu = True
            save_game()
            print(SAVE_GAME_BUTTON.feedback)
            break

        if keys[pygame.K_q]:
            print(QUIT_BUTTON.feedback)
            pygame.quit()

        LOAD_SAVE_BUTTON.show(LOAD_SAVE_BUTTON)
        SAVE_GAME_BUTTON.show(SAVE_GAME_BUTTON)
        QUIT_BUTTON.show(QUIT_BUTTON)
        BACK_BUTTON.show(BACK_BUTTON)

        pygame.display.update()

    return LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2]
