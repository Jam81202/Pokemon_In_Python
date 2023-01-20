from classes import *

def menu():

    in_menu = True
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WIN.fill(BLACK)

        RETURN_TO_MAIN_MENU_BUTTON = Button("Z: Return to Main Menu", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy",
                                        feedback="Returning to Main Menu")

        SAVE_GAME_BUTTON = Button("X: Save Game", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy",
                                        feedback="Saving...")

        QUIT_BUTTON = Button("C: Quit Game", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy",
                                        feedback="Closing Game")

        BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            in_menu = False
            print(BACK_BUTTON.feedback)

        if keys[pygame.K_z]:
            in_menu = False
            print(RETURN_TO_MAIN_MENU_BUTTON.feedback)

        if keys[pygame.K_x]:
            in_menu = True
            print(SAVE_GAME_BUTTON.feedback)

        if keys[pygame.K_c]:
            print(QUIT_BUTTON.feedback)
            pygame.quit()

        RETURN_TO_MAIN_MENU_BUTTON.show(RETURN_TO_MAIN_MENU_BUTTON)
        SAVE_GAME_BUTTON.show(SAVE_GAME_BUTTON)
        QUIT_BUTTON.show(QUIT_BUTTON)
        BACK_BUTTON.show(BACK_BUTTON)

        pygame.display.update()

    return LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2]
