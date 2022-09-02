from classes import *
from route_one import *
from pokecenter import *

pygame.init()

def starter_town(w, h):
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    velocity = 7

    # Player Trainer
    player = Player(WIDTH / 2 - 32, HEIGHT / 2 - 32)

    # Party Pokemon Overworld Sprite
    party_slot_img_right = Player(WIDTH / 2 - 115, HEIGHT / 2 - 32)
    party_slot_img_left = Player(WIDTH / 2 + 50, HEIGHT / 2 - 32)
    party_slot_img_down = Player(WIDTH / 2 - 32, HEIGHT / 2 - 115)
    party_slot_img_up = Player(WIDTH / 2 - 32, HEIGHT / 2 + 50)

    # Overworld Map
    starter_town = Background(0 - w, 0 - h)

    # Professor
    professor = Player(starter_town.x + BG_W / 3 - 100, starter_town.y + BG_H / 2 + 25)

    def redraw_window():
        WIN.fill(BLACK)
        starter_town.draw(WIN, STARTER_TOWN)
        player.draw(WIN, TRAINER_DOWN_IMG)
        professor.draw(WIN, PROFESSOR_LEFT)

        if left:
            player.draw(WIN, TRAINER_RIGHT_IMG)
            party_slot_img_right.draw(WIN, party_slot[0].poke_img)
            # step_counter += 1

        if right:
            player.draw(WIN, TRAINER_LEFT_IMG)
            party_slot_img_left.draw(WIN, party_slot[0].poke_img)

        if up:
            player.draw(WIN, TRAINER_DOWN_IMG)
            party_slot_img_down.draw(WIN, party_slot[0].poke_img)

        if down:
            player.draw(WIN, TRAINER_UP_IMG)
            party_slot_img_up.draw(WIN, party_slot[0].poke_img)

        pygame.display.update()

    def inventory():
        pass

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            #pygame.display.quit()
            pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            starter_town.x -= velocity
            professor.x -= velocity
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_a]:
            starter_town.x += velocity
            professor.x += velocity
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_s]:
            starter_town.y -= velocity
            professor.y -= velocity
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_w]:
            starter_town.y += velocity
            professor.y += velocity
            left = False
            right = False
            up = False
            down = True

        elif keys[pygame.K_i]:
            left = False
            right = False
            up = False
            down = False
            inventory()

        else:
            left = False
            right = False
            up = False
            down = False

        if player.y <= starter_town.y:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 2, 525, 840

        if player.x + 65 >= starter_town.x + BG_W / 3 + 50:
            starter_town.x += 15
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2] = 1, 0 - starter_town.x, 0 - starter_town.y
            return 6, 32, 75

        redraw_window()
