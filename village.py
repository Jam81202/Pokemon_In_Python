from classes import *

pygame.init()

def village(w, h):
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
    village = Background(0 - w, 0 - h)

    def redraw_window():
        WIN.fill(BLACK)
        village.draw(WIN, VILLAGE)
        player.draw(WIN, TRAINER_DOWN_IMG)

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2] = 4, 0 - village.x, 0 - village.y
            return 8, 0, 0

        if keys[pygame.K_d]:
            village.x -= velocity
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_a]:
            village.x += velocity
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_s]:
            village.y -= velocity
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_w]:
            village.y += velocity
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

        if player.x + 65 >= village.x + BG_W:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 3, -300, 550

        if player.y + 65 >= village.y + BG_H:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 2, -100, -290

        redraw_window()
