from classes import *
from city_one import *

pygame.init()

def pokecenter(w, h):
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    velocity = 7

    # Player Trainer
    player = Player(WIDTH / 2 - w, HEIGHT - h)
    # player_box = pygame.Rect(0, 0, 65, 65)

    # Nurse
    nurse = Player(WIDTH / 2 - 50,  20)
    # nurse_box = pygame.Rect(0, 0, 100, 75)

    # Overworld Map
    pokecenter_img = Background(0, 0)

    def redraw_window():
        WIN.fill(BLACK)
        pokecenter_img.draw(WIN, POKECENTER)
        player.draw(WIN, TRAINER_DOWN_IMG)
        nurse.draw(WIN, NURSE_LIGHT_OFF)

        if left:
            player.draw(WIN, TRAINER_RIGHT_IMG)

        if right:
            player.draw(WIN, TRAINER_LEFT_IMG)

        if up:
            player.draw(WIN, TRAINER_DOWN_IMG)

        if down:
            player.draw(WIN, TRAINER_UP_IMG)

        pygame.display.update()

    def inventory():
        pass

    while run:
        clock.tick(FPS)

        '''
        player_box.center = (player.x + 32, player.y + 32)
        nurse_box.center = (nurse.x + 50, nurse.y + 50)
        collide = nurse_box.colliderect(player_box)
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player.x + 65 <= WIDTH:
            player.x += velocity
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_a] and player.x >= 0:
            player.x -= velocity
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_s] and player.y + 65 <= HEIGHT:
            player.y += velocity
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_w] and player.y >= 100:
            player.y -= velocity
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

        if (player.x + 65 >= nurse.x and player.x + 65 <= nurse.x + 100 and player.y + 65 >= nurse.y and player.y + 65 <= nurse.y + 100)\
                or (player.x  >= nurse.x and player.x <= nurse.x + 100 and player.y >= nurse.y and player.y <= nurse.y + 100):
            if keys[pygame.K_RETURN]:
                for pokemon in party_slot:
                    if pokemon.name != "":
                        pokemon.heal()
                        nurse.draw(WIN, NURSE_LIGHT_ON)
                        pygame.display.update()
                        time.sleep(.5)
                        redraw_window()
                        time.sleep(.5)

                print("Party has been healed")

        if player.y + 65 >= HEIGHT:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2]

        redraw_window()
