from classes import *
from route_two import *
from village import *

pygame.init()

def route_one():
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
    route_one_sketch = Background(0-(BG_W * .175), 0 - (BG_H * .7))

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

    trainer1 = Player(0 + (BG_W * .22), 0 - (BG_H * .2))
    trainer2 = Player(0 + (BG_W * .185), 0 - (BG_H * .6))
    trainer3 = Player(0 - (WIDTH * .38), 0 + (HEIGHT * .35))

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

    def battle(pokemon = None):
        battling = True
        if trainer_battle:
            wild_pokemon = pokemon

        else:
            wild_pokemon = random.choice(POKE_DEX)
            wild_pokemon = wild_pokemon.add_pokemon(1, 8)
        wild_pokemon_img = Player(WIDTH / 2 + 100, HEIGHT * .20)
        party_slot_img = Player(WIDTH / 3 - 125, HEIGHT * .55)
        turn_counter = 1

        def fight():
            selecting = True
            while selecting:
                WIN.fill(BLACK)
                wild_pokemon_img.draw(WIN, wild_pokemon.poke_img)
                party_slot_img.draw(WIN, party_slot[0].poke_img)

                # Fight Buttons
                MOVE_1_BUTTON = Button("1: " + party_slot[0].move1.name, (WIDTH / 3 - 125, HEIGHT * .75), font=30,
                                       bg="navy", feedback=party_slot[0].move1.name)
                MOVE_2_BUTTON = Button("2: " + party_slot[0].move2.name, (WIDTH / 2 + 100, HEIGHT * .75), font=30,
                                       bg="navy", feedback=party_slot[0].move2.name)
                MOVE_3_BUTTON = Button("3: " + party_slot[0].move3.name, (WIDTH / 3 - 125, HEIGHT * .85), font=30,
                                       bg="navy", feedback=party_slot[0].move3.name)
                MOVE_4_BUTTON = Button("4: " + party_slot[0].move4.name, (WIDTH / 2 + 100, HEIGHT * .85), font=30,
                                       bg="navy", feedback=party_slot[0].move4.name)

                PLAYER_HP = Button("level " + str(party_slot[0].level) + " " + str(party_slot[0].name) + " | HP: " + str(party_slot[0].hp), (WIDTH / 3 - 125, HEIGHT * .65), font=20,
                                       bg="navy", feedback=party_slot[0].move4.name)

                ENEMY_HP = Button("level " + str(wild_pokemon.level) + " " + str(wild_pokemon.name) + " | HP: " + str(wild_pokemon.hp), (WIDTH / 2 + 100, HEIGHT * .15), font=20,
                                   bg="navy", feedback=party_slot[0].move4.name)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    if party_slot[0].speed >= wild_pokemon.speed:
                        party_slot[0].move1.attack(party_slot[0].move1, wild_pokemon, party_slot[0])

                        if wild_pokemon.hp > 0:
                            wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                    else:
                        wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                        if party_slot[0].hp > 0:
                            party_slot[0].move1.attack(party_slot[0].move1, wild_pokemon, party_slot[0])

                    break

                if keys[pygame.K_2]:
                    if party_slot[0].speed >= wild_pokemon.speed:
                        party_slot[0].move2.attack(party_slot[0].move2, wild_pokemon, party_slot[0])

                        if wild_pokemon.hp > 0:
                            wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                    else:
                        wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                        if party_slot[0].hp > 0:
                            party_slot[0].move2.attack(party_slot[0].move2, wild_pokemon, party_slot[0])

                    break

                if keys[pygame.K_3]:
                    if party_slot[0].speed >= wild_pokemon.speed:
                        party_slot[0].move3.attack(party_slot[0].move3, wild_pokemon, party_slot[0])

                        if wild_pokemon.hp > 0:
                            wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                    else:
                        wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                        if party_slot[0].hp > 0:
                            party_slot[0].move3.attack(party_slot[0].move3, wild_pokemon, party_slot[0])

                    break

                if keys[pygame.K_4]:
                    if party_slot[0].speed >= wild_pokemon.speed:
                        party_slot[0].move4.attack(party_slot[0].move4, wild_pokemon, party_slot[0])

                        if wild_pokemon.hp > 0:
                            wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                    else:
                        wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                        if party_slot[0].hp > 0:
                            party_slot[0].move4.attack(party_slot[0].move4, wild_pokemon, party_slot[0])

                    break


                MOVE_1_BUTTON.show(MOVE_1_BUTTON)
                MOVE_2_BUTTON.show(MOVE_2_BUTTON)
                MOVE_3_BUTTON.show(MOVE_3_BUTTON)
                MOVE_4_BUTTON.show(MOVE_4_BUTTON)
                PLAYER_HP.show(PLAYER_HP)
                ENEMY_HP.show(ENEMY_HP)

                pygame.display.update()

        def party():
            selecting = True

            while selecting:
                WIN.fill(BLACK)

                # Party Buttons
                PARTY_SLOT_1_BUTTON = Button("1: level " + str(party_slot[0].level) + " " + party_slot[0].name, (WIDTH / 3 - 125, HEIGHT * .15), font=30,
                                             bg="navy", feedback="You chose slot 1")
                PARTY_SLOT_2_BUTTON = Button("2: level " + str(party_slot[1].level) + " " + party_slot[1].name, (WIDTH / 2 + 100, HEIGHT * .15), font=30,
                                             bg="navy", feedback="You chose slot 2")
                PARTY_SLOT_3_BUTTON = Button("3: level " + str(party_slot[2].level) + " " + party_slot[2].name, (WIDTH / 3 - 125, HEIGHT * .25), font=30,
                                             bg="navy", feedback="You chose slot 3")
                PARTY_SLOT_4_BUTTON = Button("4: level " + str(party_slot[3].level) + " " + party_slot[3].name, (WIDTH / 2 + 100, HEIGHT * .25), font=30,
                                             bg="navy", feedback="You chose slot 4")
                PARTY_SLOT_5_BUTTON = Button("5: level " + str(party_slot[4].level) + " " + party_slot[4].name, (WIDTH / 3 - 125, HEIGHT * .35), font=30,
                                             bg="navy", feedback="You chose slot 5")
                PARTY_SLOT_6_BUTTON = Button("6: level " + str(party_slot[5].level) + " " + party_slot[5].name, (WIDTH / 2 + 100, HEIGHT * .35), font=30,
                                             bg="navy", feedback="You chose slot 6")

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    print(PARTY_SLOT_1_BUTTON.show_feedback(PARTY_SLOT_1_BUTTON))
                    return True

                if keys[pygame.K_2]:
                    print(PARTY_SLOT_2_BUTTON.show_feedback(PARTY_SLOT_2_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[1]
                    party_slot[1] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    return False

                if keys[pygame.K_3]:
                    print(PARTY_SLOT_3_BUTTON.show_feedback(PARTY_SLOT_3_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[2]
                    party_slot[2] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    return False

                if keys[pygame.K_4]:
                    print(PARTY_SLOT_4_BUTTON.show_feedback(PARTY_SLOT_4_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[3]
                    party_slot[3] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    return False

                if keys[pygame.K_5]:
                    print(PARTY_SLOT_5_BUTTON.show_feedback(PARTY_SLOT_5_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[4]
                    party_slot[4] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    return False

                if keys[pygame.K_6]:
                    print(PARTY_SLOT_6_BUTTON.show_feedback(PARTY_SLOT_6_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[5]
                    party_slot[5] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    return False

                PARTY_SLOT_1_BUTTON.show(PARTY_SLOT_1_BUTTON)
                PARTY_SLOT_2_BUTTON.show(PARTY_SLOT_2_BUTTON)
                PARTY_SLOT_3_BUTTON.show(PARTY_SLOT_3_BUTTON)
                PARTY_SLOT_4_BUTTON.show(PARTY_SLOT_4_BUTTON)
                PARTY_SLOT_5_BUTTON.show(PARTY_SLOT_5_BUTTON)
                PARTY_SLOT_6_BUTTON.show(PARTY_SLOT_6_BUTTON)

                pygame.display.update()

        def bag():
            selecting = True

            while selecting:
                WIN.fill(BLACK)

                # Bag buttons Buttons
                POTION_MENU_BUTTON = Button("Z: Potions", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Potions")
                LEVEL_ITEMS_MENU_BUTTON = Button("X: Level Items", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot Level Items")
                STAT_ITEMS_MENU_BUTTON = Button("C: Stat Items", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy", feedback="You chose slot Stat Items")
                POKE_BALLS_MENU_BUTTON = Button("V: Poke Balls", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy", feedback="You chose slot Poke Balls")

                BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

                def potions_menu():
                    while True:
                        WIN.fill(BLACK)

                        POTION_BUTTON = Button("1: Potion", (WIDTH / 3 - 125, HEIGHT * .15), font=30, bg="navy", feedback="You chose slot Potion")
                        SUPER_POTION_BUTTON = Button("2: Super Potion ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Super Potion")
                        HYPER_POTION_BUTTON = Button("3: Hyper Potion ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot Hyper Potion")
                        BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                        keys = pygame.key.get_pressed()

                        if keys[pygame.K_LEFT]:
                            time.sleep(1)
                            return True

                        if keys[pygame.K_1]:
                            POTION.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_2]:
                            SUPER_POTION.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_3]:
                            HYPER_POTION.stat_raise(party_slot[0])
                            return False

                        POTION_BUTTON.show(POTION_BUTTON)
                        SUPER_POTION_BUTTON.show(SUPER_POTION_BUTTON)
                        HYPER_POTION_BUTTON.show(HYPER_POTION_BUTTON)
                        BACK_BUTTON.show(BACK_BUTTON)

                        pygame.display.update()

                def level_items_menu():
                    while True:
                        WIN.fill(BLACK)

                        RARE_CANDY_BUTTON = Button("1: Rare Candy ", (WIDTH / 3 - 125, HEIGHT * .15), font=30, bg="navy", feedback="You chose slot Rare Candy")
                        XL_CANDY_BUTTON = Button("2: XL Candy ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot XL Candy")
                        L_CANDY_BUTTON = Button("3: L Candy ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot L Candy")
                        M_CANDY_BUTTON = Button("4: M Candy ", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy", feedback="You chose slot M Candy")
                        S_CANDY_BUTTON = Button("5: S Candy ", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy", feedback="You chose slot S Candy")
                        BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                        keys = pygame.key.get_pressed()

                        if keys[pygame.K_LEFT]:
                            time.sleep(1)
                            return True

                        if keys[pygame.K_1]:
                            RARE_CANDY.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_2]:
                            XL_CANDY.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_3]:
                            L_CANDY.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_4]:
                            M_CANDY.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_5]:
                            S_CANDY.stat_raise(party_slot[0])
                            return False

                        RARE_CANDY_BUTTON.show(RARE_CANDY_BUTTON)
                        XL_CANDY_BUTTON.show(XL_CANDY_BUTTON)
                        L_CANDY_BUTTON.show(L_CANDY_BUTTON)
                        M_CANDY_BUTTON.show(M_CANDY_BUTTON)
                        S_CANDY_BUTTON.show(S_CANDY_BUTTON)
                        BACK_BUTTON.show(BACK_BUTTON)

                        pygame.display.update()

                def stat_items_menu():
                    while True:
                        WIN.fill(BLACK)

                        CALCIUM_BUTTON = Button("1: Calcium ", (WIDTH / 3 - 125, HEIGHT * .15), font=30, bg="navy", feedback="You chose slot Calcium")
                        CARBOS_BUTTON = Button("2: Carbos ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Carbos")
                        HP_UP_BUTTON = Button("3: HP Up ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot HP Up")
                        IRON_BUTTON = Button("4: Iron ", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy", feedback="You chose slot Iron")
                        PROTEIN_BUTTON = Button("5: Protein ", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy", feedback="You chose slot Protein")
                        ZINC_BUTTON = Button("6: Zinc ", (WIDTH / 3 - 125, HEIGHT * .65), font=30, bg="navy", feedback="You chose slot Zinc")
                        BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                        keys = pygame.key.get_pressed()

                        if keys[pygame.K_LEFT]:
                            time.sleep(1)
                            return True

                        if keys[pygame.K_1]:
                            CALCIUM.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_2]:
                            CARBOS.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_3]:
                            HP_UP.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_4]:
                            IRON.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_5]:
                            PROTEIN.stat_raise(party_slot[0])
                            return False

                        if keys[pygame.K_6]:
                            ZINC.stat_raise(party_slot[0])
                            return False

                        CALCIUM_BUTTON.show(CALCIUM_BUTTON)
                        CARBOS_BUTTON.show(CARBOS_BUTTON)
                        HP_UP_BUTTON.show(HP_UP_BUTTON)
                        IRON_BUTTON.show(IRON_BUTTON)
                        PROTEIN_BUTTON.show(PROTEIN_BUTTON)
                        ZINC_BUTTON.show(ZINC_BUTTON)
                        BACK_BUTTON.show(BACK_BUTTON)

                        pygame.display.update()

                def poke_balls_menu():
                    while True:
                        WIN.fill(BLACK)

                        POKE_BALL_BUTTON = Button("1: Poke Ball ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Poke Ball")
                        GREAT_BALL_BUTTON = Button("2: Great Ball ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot Great Ball")
                        ULTRA_BALL_BUTTON = Button("3: Ultra Ball ", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy", feedback="You chose slot Ultra Ball")
                        MASTER_BALL_BUTTON = Button("4: Master Ball ", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy", feedback="You chose slot Master Ball")
                        BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                        keys = pygame.key.get_pressed()

                        if keys[pygame.K_LEFT]:
                            time.sleep(1)
                            return True

                        if keys[pygame.K_1]:
                            if POKE_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            return False

                        if keys[pygame.K_2]:
                            if GREAT_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            return False

                        if keys[pygame.K_3]:
                            if ULTRA_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            return False

                        if keys[pygame.K_4]:
                            if MASTER_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            return False


                        POKE_BALL_BUTTON.show(POKE_BALL_BUTTON)
                        GREAT_BALL_BUTTON.show(GREAT_BALL_BUTTON)
                        ULTRA_BALL_BUTTON.show(ULTRA_BALL_BUTTON)
                        MASTER_BALL_BUTTON.show(MASTER_BALL_BUTTON)
                        BACK_BUTTON.show(BACK_BUTTON)

                        pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    return True

                if keys[pygame.K_z]:
                    if not potions_menu():
                        break

                if keys[pygame.K_x]:
                    if not level_items_menu():
                        break

                if keys[pygame.K_c]:
                    if not stat_items_menu():
                        break

                if keys[pygame.K_v]:
                    if not trainer_battle:
                        if not poke_balls_menu():
                            break

                    else:
                        print("You can not attempt to catch another Trainers Pokemon.")
                        time.sleep(2)

                POTION_MENU_BUTTON.show(POTION_MENU_BUTTON)
                LEVEL_ITEMS_MENU_BUTTON.show(LEVEL_ITEMS_MENU_BUTTON)
                STAT_ITEMS_MENU_BUTTON.show(STAT_ITEMS_MENU_BUTTON)
                POKE_BALLS_MENU_BUTTON.show(POKE_BALLS_MENU_BUTTON)
                BACK_BUTTON.show(BACK_BUTTON)

                pygame.display.update()

        def run():
            return random.randint(1, 10)

        while battling:
            WIN.fill(BLACK)
            wild_pokemon_img.draw(WIN, wild_pokemon.poke_img)
            party_slot_img.draw(WIN, party_slot[0].poke_img)

            if party_slot[0].hp <= 0:
                party_slot[0].hp += abs(party_slot[0].hp)
                print("Your", party_slot[0].name, "has fainted!")
                time.sleep(2)
                party()

            if wild_pokemon.hp <= 0:
                wild_pokemon.hp += abs(wild_pokemon.hp)
                print("The wild", wild_pokemon.name, "has fainted!")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                fight()
                turn_counter += 1

            if keys[pygame.K_p]:
                skip = party()

                if not skip:
                    wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
                    turn_counter += 1

            if keys[pygame.K_i]:
                skip = bag()

                if wild_pokemon.hp > 0 and not skip:
                    wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
                    turn_counter += 1

                time.sleep(1)

            if keys[pygame.K_r]:
                if not trainer_battle:
                    run_away = run()
                    if run_away < 8:
                        print("you ran away")
                        time.sleep(1)
                        break

                    elif run_away > 7:
                        print("you did not run away")
                        time.sleep(1)
                        wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
                        turn_counter += 1

                else:
                    print("You can not run from a Trainer.")
                    time.sleep(2)

            PLAYER_HP = Button("level " + str(party_slot[0].level) + " " + str(party_slot[0].name) + " | HP: " + str(party_slot[0].hp), (WIDTH / 3 - 125, HEIGHT * .65), font=25, bg="navy", feedback=party_slot[0].move4.name)
            ENEMY_HP = Button("level " + str(wild_pokemon.level) + " " + str(wild_pokemon.name) + " | HP: " + str(wild_pokemon.hp), (WIDTH / 2 + 100, HEIGHT * .15), font=25, bg="navy", feedback=party_slot[0].move4.name)
            TURN_NUM = Button("Turn: " + str(turn_counter), (0, 0), font=30, bg="navy", feedback=str(turn_counter))

            FIGHT_BATTLE_BUTTON.show(FIGHT_BATTLE_BUTTON)
            POKEMON_BATTLE_BUTTON.show(POKEMON_BATTLE_BUTTON)
            ITEMS_BATTLE_BUTTON.show(ITEMS_BATTLE_BUTTON)
            RUN_BATTLE_BUTTON.show(RUN_BATTLE_BUTTON)
            PLAYER_HP.show(PLAYER_HP)
            ENEMY_HP.show(ENEMY_HP)
            TURN_NUM.show(TURN_NUM)

            pygame.display.update()

            if party_slot[0].hp <= 0:
                if party_slot[1].hp <= 0:
                    if party_slot[2].hp <= 0:
                        if party_slot[3].hp <= 0:
                            if party_slot[4].hp <= 0:
                                if party_slot[5].hp <= 0:
                                    print("You Lost!")
                                    time.sleep(2)
                                    break

            if wild_pokemon.hp == 0:
                time.sleep(2)
                break

        wild_pokemon.heal()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

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
            battle()

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
            break

        if player.y <= route_one_sketch.y and player.x >= trainer2.x:
            route_one_sketch.y -= 5
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            route_two()

        if player.y <= route_one_sketch.y:
            route_one_sketch.y -= 5
            WIN.fill(BLACK)
            LOADING_SCREEN = Button("LOADING. . . ", (WIDTH / 2 - 200, HEIGHT / 2), font=50, bg="navy", feedback="loading")
            LOADING_SCREEN.show(LOADING_SCREEN)
            pygame.display.update()
            time.sleep(1)
            village()

        if player.x + 50 >= trainer1.x and player.x + 50 <= (trainer1.x + 100) and player.y + 50 >= trainer1.y and player.y + 50 <= (trainer1.y + 100) and not trainer1_battle:
            trainer_battle = True

            for pokemon in trainer1_party:
                battle(pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer1_party:
                    pokemon.heal()

                for pokemon in party_slot:
                    pokemon.heal()

                print("Returning to Pokecenter.")
                time.sleep(2)

                route_one_sketch.x, route_one_sketch.y = 0 - (BG_W * .5), 0 - (BG_H / 2)
                trainer1.x, trainer1.y = (BG_W * .015) - (BG_W * .5), 0 - (BG_H / 25)
                trainer2.x, trainer2.y = (BG_W * .1) - (BG_W * .5), 0 - (BG_H / 25)
                trainer3.x, trainer3.y = (BG_W * .2) - (BG_W * .5), 0 - (BG_H / 25)

            else:
                trainer1_battle = True

            trainer_battle = False

        if player.x + 50 >= trainer2.x and player.x + 50 <= (trainer2.x + 100) and player.y + 50 >= trainer2.y and player.y + 50 <= (trainer2.y + 100) and not trainer2_battle:
            trainer_battle = True

            for pokemon in trainer2_party:
                battle(pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer1_party:
                    pokemon.heal()

                for pokemon in party_slot:
                    pokemon.heal()

                print("Returning to Pokecenter.")
                time.sleep(2)
                route_one_sketch.x, route_one_sketch.y = 0 - (BG_W * .5), 0 - (BG_H / 2)
                trainer1.x, trainer1.y = (BG_W * .015) - (BG_W * .5), 0 - (BG_H / 25)
                trainer2.x, trainer2.y = (BG_W * .1) - (BG_W * .5), 0 - (BG_H / 25)
                trainer3.x, trainer3.y = (BG_W * .2) - (BG_W * .5), 0 - (BG_H / 25)

            else:
                trainer2_battle = True

            trainer_battle = False

        if player.x + 50 >= trainer3.x and player.x + 50 <= (trainer3.x + 100) and player.y + 50 >= trainer3.y and player.y + 50 <= (trainer3.y + 100) and not trainer3_battle:
            trainer_battle = True

            for pokemon in trainer3_party:
                battle(pokemon)

            if party_slot[0].hp <= 0:
                for pokemon in trainer1_party:
                    pokemon.heal()

                for pokemon in party_slot:
                    pokemon.heal()

                print("Returning to Pokecenter.")
                time.sleep(2)
                route_one_sketch.x, route_one_sketch.y = 0 - (BG_W * .5), 0 - (BG_H / 2)
                trainer1.x, trainer1.y = (BG_W * .015) - (BG_W * .5), 0 - (BG_H / 25)
                trainer2.x, trainer2.y = (BG_W * .1) - (BG_W * .5), 0 - (BG_H / 25)
                trainer3.x, trainer3.y = (BG_W * .2) - (BG_W * .5), 0 - (BG_H / 25)

            else:
                trainer3_battle = True

            trainer_battle = False

        redraw_window()