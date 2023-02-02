from classes import *
from battle import *

pygame.init()

def route_one(w, h):
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    velocity = 7

    # Player Trainer
    player = Player(WIDTH/2-32, HEIGHT/2-32)

    # Party Pokemon Overworld Sprite
    party_slot_img_right = Player(WIDTH / 2 - 115, HEIGHT / 2 - 32)
    party_slot_img_left = Player(WIDTH / 2 + 50, HEIGHT / 2 - 32)
    party_slot_img_down = Player(WIDTH / 2 - 32, HEIGHT / 2 - 115)
    party_slot_img_up = Player(WIDTH / 2 - 32, HEIGHT / 2 + 50)

    # Overworld Map
    route_one_sketch = Background(0 - w, 0 - h)

    # Trainers
    global trainer_battle
    global trainer1_battle
    global trainer2_battle
    global trainer3_battle

    # Trainer 1
    trainer1_poke1 = Pokemon(RATTATA.name, RATTATA.poke_img, 4, RATTATA.stat_calc(4, RATTATA.hp),
                             RATTATA.stat_calc(4, RATTATA.atk), RATTATA.stat_calc(4, RATTATA.df),
                             RATTATA.stat_calc(4, RATTATA.spatk),
                             RATTATA.stat_calc(4, RATTATA.spdf), RATTATA.stat_calc(4, RATTATA.speed), RATTATA.move1,
                             RATTATA.move2, RATTATA.move3, RATTATA.move4)
    trainer1_party = [trainer1_poke1]

    # Trainer 2
    trainer2_poke1 = Pokemon(WEEDLE.name, WEEDLE.poke_img, 4, WEEDLE.stat_calc(4, WEEDLE.hp),
                             WEEDLE.stat_calc(4, WEEDLE.atk), WEEDLE.stat_calc(4, WEEDLE.df),
                             WEEDLE.stat_calc(4, WEEDLE.spatk),
                             WEEDLE.stat_calc(4, WEEDLE.spdf), WEEDLE.stat_calc(4, WEEDLE.speed), WEEDLE.move1,
                             WEEDLE.move2, WEEDLE.move3, WEEDLE.move4)
    trainer2_party = [trainer2_poke1]

    # Trainer 3
    trainer3_poke1 = Pokemon(WEEDLE.name, WEEDLE.poke_img, 4, WEEDLE.stat_calc(4, WEEDLE.hp),
                             WEEDLE.stat_calc(4, WEEDLE.atk), WEEDLE.stat_calc(4, WEEDLE.df),
                             WEEDLE.stat_calc(4, WEEDLE.spatk),
                             WEEDLE.stat_calc(4, WEEDLE.spdf), WEEDLE.stat_calc(4, WEEDLE.speed), WEEDLE.move1,
                             WEEDLE.move2, WEEDLE.move3, WEEDLE.move4)
    trainer3_poke2 = Pokemon(CATERPIE.name, CATERPIE.poke_img, 4, CATERPIE.stat_calc(4, CATERPIE.hp),
                             CATERPIE.stat_calc(4, CATERPIE.atk), CATERPIE.stat_calc(4, CATERPIE.df),
                             CATERPIE.stat_calc(4, CATERPIE.spatk),
                             CATERPIE.stat_calc(4, CATERPIE.spdf), CATERPIE.stat_calc(4, CATERPIE.speed),
                             CATERPIE.move1, CATERPIE.move2, CATERPIE.move3, CATERPIE.move4)
    trainer3_party = [trainer3_poke1, trainer3_poke2]

    trainer1 = Player(route_one_sketch.x + BG_W / 2 - 300, route_one_sketch.y + BG_H / 2)
    trainer2 = Player(route_one_sketch.x + BG_W / 2 - 425, route_one_sketch.y + 125)
    trainer3 = Player(route_one_sketch.x + 225, route_one_sketch.y + BG_H - 125)

    global step_counter, left, right

    if step_counter > 1:
        step_counter = 0

    def redraw_window():
        WIN.fill(BLACK)
        route_one_sketch.draw(WIN, ROUTE_1)
        player.draw(WIN, TRAINER_DOWN_IMG)
        trainer1.draw(WIN, TRAINER_DOWN_IMG)
        trainer2.draw(WIN, TRAINER_DOWN_IMG)
        trainer3.draw(WIN, TRAINER_DOWN_IMG)

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
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2] = 2, 0 - route_one_sketch.x, 0 - route_one_sketch.y
            return 8, 0, 0

        if keys[pygame.K_d]:
            route_one_sketch.x -= velocity
            trainer1.x -= velocity
            trainer2.x -= velocity
            trainer3.x -= velocity
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_a]:
            route_one_sketch.x += velocity
            trainer1.x += velocity
            trainer2.x += velocity
            trainer3.x += velocity
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_s]:
            route_one_sketch.y -= velocity
            trainer1.y -= velocity
            trainer2.y -= velocity
            trainer3.y -= velocity
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_w]:
            route_one_sketch.y += velocity
            trainer1.y += velocity
            trainer2.y += velocity
            trainer3.y += velocity
            left = False
            right = False
            up = False
            down = True

        elif keys[pygame.K_b]:
            left = False
            right = False
            up = False
            down = False
            battle(1)

        elif keys[pygame.K_i]:
            left = False
            right = False
            up = False
            down = False
            inventory()

        elif keys[pygame.K_p]:
            for pokemon in PC_STORAGE:
                print(pokemon.name, pokemon.level)

        else:
            left = False
            right = False
            up = False
            down = False

        if player.y + 65 >= route_one_sketch.y + BG_H:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 1, 475, -290

        if player.y <= route_one_sketch.y and route_one_sketch.x <= -600:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 3, 600, 840

        if player.y <= route_one_sketch.y:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 4, 325, 840

        if player.x + 50 >= trainer1.x and player.x + 50 <= (trainer1.x + 100) and player.y + 50 >= trainer1.y and player.y + 50 <= (trainer1.y + 100) and not trainer1_battle:
            trainer_battle = True

            for pokemon in trainer1_party:
                battle(1, pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer1_party:
                    pokemon.heal()

                for pokemon in party_slot:
                    pokemon.heal()

                print("Returning to Pokecenter.")
                time.sleep(2)
                return LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2]

            else:
                trainer1_battle = True

            trainer_battle = False

        if player.x + 50 >= trainer2.x and player.x + 50 <= (trainer2.x + 100) and player.y + 50 >= trainer2.y and player.y + 50 <= (trainer2.y + 100) and not trainer2_battle:
            trainer_battle = True

            for pokemon in trainer2_party:
                battle(1, pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer1_party:
                    pokemon.heal()

                for pokemon in party_slot:
                    pokemon.heal()

                print("Returning to Pokecenter.")
                time.sleep(2)
                return LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2]

            else:
                trainer2_battle = True

            trainer_battle = False

        if player.x + 50 >= trainer3.x and player.x + 50 <= (trainer3.x + 100) and player.y + 50 >= trainer3.y and player.y + 50 <= (trainer3.y + 100) and not trainer3_battle:
            trainer_battle = True

            for pokemon in trainer3_party:
                battle(1, pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer1_party:
                    pokemon.heal()

                for pokemon in party_slot:
                    pokemon.heal()

                print("Returning to last Pokecenter.")
                time.sleep(2)
                return LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2]

            else:
                trainer3_battle = True

            trainer_battle = False

        redraw_window()