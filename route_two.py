from classes import *

pygame.init()

def route_two(w, h):
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
    route_two_sketch = Background(0 - w, 0 - h)

    # Trainers
    global trainer_battle
    global trainer5_battle
    global trainer6_battle
    global trainer7_battle

    # Trainer 5
    trainer5_poke1 = Pokemon(RATTATA.name, RATTATA.poke_img, 7, RATTATA.stat_calc(7, RATTATA.hp),
                             RATTATA.stat_calc(7, RATTATA.atk), RATTATA.stat_calc(7, RATTATA.df),
                             RATTATA.stat_calc(7, RATTATA.spatk), RATTATA.stat_calc(7, RATTATA.spdf),
                             RATTATA.stat_calc(7, RATTATA.speed), RATTATA.move1,RATTATA.move2, RATTATA.move3,
                             RATTATA.move4)

    trainer5_poke2 = Pokemon(SPEAROW.name, SPEAROW.poke_img, 8, SPEAROW.stat_calc(8, SPEAROW.hp),
                             SPEAROW.stat_calc(8, SPEAROW.atk), SPEAROW.stat_calc(8, SPEAROW.df),
                             SPEAROW.stat_calc(8, SPEAROW.spatk), SPEAROW.stat_calc(8, SPEAROW.spdf),
                             SPEAROW.stat_calc(8, SPEAROW.speed), SPEAROW.move1, SPEAROW.move2, SPEAROW.move3,
                             SPEAROW.move4)

    trainer5_party = [trainer5_poke1, trainer5_poke2]

    # Trainer 6
    trainer6_poke1 = Pokemon(ODDISH.name, ODDISH.poke_img, 11, ODDISH.stat_calc(11, ODDISH.hp),
                             ODDISH.stat_calc(11, ODDISH.atk), ODDISH.stat_calc(11, ODDISH.df),
                             ODDISH.stat_calc(11, ODDISH.spatk), ODDISH.stat_calc(11, ODDISH.spdf),
                             ODDISH.stat_calc(11, ODDISH.speed), ODDISH.move1, ODDISH.move2, ODDISH.move3, ODDISH.move4)

    trainer6_party = [trainer6_poke1]

    # Trainer 7
    trainer7_poke1 = Pokemon(PIDGEY.name, PIDGEY.poke_img, 14, PIDGEY.stat_calc(14, PIDGEY.hp),
                             PIDGEY.stat_calc(14, PIDGEY.atk), PIDGEY.stat_calc(14, PIDGEY.df),
                             PIDGEY.stat_calc(14, PIDGEY.spatk), PIDGEY.stat_calc(14, PIDGEY.spdf),
                             PIDGEY.stat_calc(14, PIDGEY.speed), PIDGEY.move1, PIDGEY.move2, PIDGEY.move3, PIDGEY.move4)

    trainer7_poke2 = Pokemon(CATERPIE.name, CATERPIE.poke_img, 15, CATERPIE.stat_calc(15, CATERPIE.hp),
                             CATERPIE.stat_calc(15, CATERPIE.atk), CATERPIE.stat_calc(15, CATERPIE.df),
                             CATERPIE.stat_calc(15, CATERPIE.spatk), CATERPIE.stat_calc(15, CATERPIE.spdf),
                             CATERPIE.stat_calc(15, CATERPIE.speed), CATERPIE.move1, CATERPIE.move2, CATERPIE.move3,
                             CATERPIE.move4)

    trainer7_party = [trainer7_poke1, trainer7_poke2]

    trainer5 = Player(route_two_sketch.x + BG_W / 2 + 150, route_two_sketch.y + BG_H / 2 + 275)
    trainer6 = Player(route_two_sketch.x + BG_W / 2 + 525, route_two_sketch.y + 150)
    trainer7 = Player(route_two_sketch.x + BG_W / 2 + 825, route_two_sketch.y + BG_H / 2 - 35)

    global step_counter, left, right

    if step_counter > 1:
        step_counter = 0

    def redraw_window():
        WIN.fill(BLACK)
        route_two_sketch.draw(WIN, ROUTE_2)
        player.draw(WIN, TRAINER_DOWN_IMG)
        trainer5.draw(WIN, TRAINER_DOWN_IMG)
        trainer6.draw(WIN, TRAINER_DOWN_IMG)
        trainer7.draw(WIN, TRAINER_DOWN_IMG)

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
            LAST_LOCATION[0], LAST_LOCATION[1], LAST_LOCATION[2] = 3, 0 - route_two_sketch.x, 0 - route_two_sketch.y
            return 8, 0, 0

        if keys[pygame.K_d]:
            route_two_sketch.x -= velocity
            trainer5.x -= velocity
            trainer6.x -= velocity
            trainer7.x -= velocity
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_a]:
            route_two_sketch.x += velocity
            trainer5.x += velocity
            trainer6.x += velocity
            trainer7.x += velocity
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_s]:
            route_two_sketch.y -= velocity
            trainer5.y -= velocity
            trainer6.y -= velocity
            trainer7.y -= velocity
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_w]:
            route_two_sketch.y += velocity
            trainer5.y += velocity
            trainer6.y += velocity
            trainer7.y += velocity
            left = False
            right = False
            up = False
            down = True

        elif keys[pygame.K_b]:
            left = False
            right = False
            up = False
            down = False
            player.battle(2, False)

            if party_slot[0].hp <= 0:
                player.blackout()
                return LAST_POKECENTER[0], LAST_POKECENTER[1], LAST_POKECENTER[2]

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

        if player.y + 65 >= route_two_sketch.y + BG_H:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy",
                                    feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 2, 775, -290

        if player.x <= route_two_sketch.x:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy",
                                    feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 4, 2525, 150

        if player.x + 65 >= route_two_sketch.x + BG_W:
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy",
                                    feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            return 5, -300, 150

        if player.x + 50 >= trainer5.x and player.x + 50 <= (trainer5.x + 100) and player.y + 50 >= trainer5.y and player.y + 50 <= (trainer5.y + 100) and not trainer5_battle:

            for pokemon in trainer5_party:
                player.battle(2, True, pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer5_party:
                    pokemon.heal()

                player.blackout()
                return LAST_POKECENTER[0], LAST_POKECENTER[1], LAST_POKECENTER[2]

            else:
                trainer5_battle = True

            trainer_battle = False

        if player.x + 50 >= trainer6.x and player.x + 50 <= (trainer6.x + 100) and player.y + 50 >= trainer6.y and player.y + 50 <= (trainer6.y + 100) and not trainer6_battle:

            for pokemon in trainer6_party:
                player.battle(2, True, pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer6_party:
                    pokemon.heal()

                player.blackout()
                return LAST_POKECENTER[0], LAST_POKECENTER[1], LAST_POKECENTER[2]

            else:
                trainer6_battle = True

            trainer_battle = False

        if player.x + 50 >= trainer7.x and player.x + 50 <= (trainer7.x + 100) and player.y + 50 >= trainer7.y and player.y + 50 <= (trainer7.y + 100) and not trainer7_battle:

            for pokemon in trainer7_party:
                player.battle(2, True, pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer7_party:
                    pokemon.heal()

                player.blackout()
                return LAST_POKECENTER[0], LAST_POKECENTER[1], LAST_POKECENTER[2]

            else:
                trainer7_battle = True

            trainer_battle = False

        redraw_window()