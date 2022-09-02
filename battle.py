from classes import *
from route_one import *
from route_two import *

pygame.init()

def battle(route_num, pokemon=None):
    battling = True
    if trainer_battle:
        wild_pokemon = pokemon

    else:
        wild_pokemon = random.choice(POKE_DEX)

        if route_num == 1:
            wild_pokemon = wild_pokemon.add_pokemon(1, 8)

        elif route_num == 2:
            wild_pokemon = wild_pokemon.add_pokemon(7, 15)

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

            PLAYER_HP = Button(
                "level " + str(party_slot[0].level) + " " + str(party_slot[0].name) + " | HP: " + str(party_slot[0].hp),
                (WIDTH / 3 - 125, HEIGHT * .65), font=20,
                bg="navy", feedback=party_slot[0].move4.name)

            ENEMY_HP = Button(
                "level " + str(wild_pokemon.level) + " " + str(wild_pokemon.name) + " | HP: " + str(wild_pokemon.hp),
                (WIDTH / 2 + 100, HEIGHT * .15), font=20,
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
            PARTY_SLOT_1_BUTTON = Button("1: level " + str(party_slot[0].level) + " " + party_slot[0].name,
                                         (WIDTH / 3 - 125, HEIGHT * .15), font=30,
                                         bg="navy", feedback="You chose slot 1")
            PARTY_SLOT_2_BUTTON = Button("2: level " + str(party_slot[1].level) + " " + party_slot[1].name,
                                         (WIDTH / 2 + 100, HEIGHT * .15), font=30,
                                         bg="navy", feedback="You chose slot 2")
            PARTY_SLOT_3_BUTTON = Button("3: level " + str(party_slot[2].level) + " " + party_slot[2].name,
                                         (WIDTH / 3 - 125, HEIGHT * .25), font=30,
                                         bg="navy", feedback="You chose slot 3")
            PARTY_SLOT_4_BUTTON = Button("4: level " + str(party_slot[3].level) + " " + party_slot[3].name,
                                         (WIDTH / 2 + 100, HEIGHT * .25), font=30,
                                         bg="navy", feedback="You chose slot 4")
            PARTY_SLOT_5_BUTTON = Button("5: level " + str(party_slot[4].level) + " " + party_slot[4].name,
                                         (WIDTH / 3 - 125, HEIGHT * .35), font=30,
                                         bg="navy", feedback="You chose slot 5")
            PARTY_SLOT_6_BUTTON = Button("6: level " + str(party_slot[5].level) + " " + party_slot[5].name,
                                         (WIDTH / 2 + 100, HEIGHT * .35), font=30,
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
            POTION_MENU_BUTTON = Button("Z: Potions", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy",
                                        feedback="You chose slot Potions")
            LEVEL_ITEMS_MENU_BUTTON = Button("X: Level Items", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy",
                                             feedback="You chose slot Level Items")
            STAT_ITEMS_MENU_BUTTON = Button("C: Stat Items", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy",
                                            feedback="You chose slot Stat Items")
            POKE_BALLS_MENU_BUTTON = Button("V: Poke Balls", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy",
                                            feedback="You chose slot Poke Balls")

            BACK_BUTTON = Button("<-- Back", (0, 0), font=30, bg="navy", feedback="You chose to go back")

            def potions_menu():
                while True:
                    WIN.fill(BLACK)

                    POTION_BUTTON = Button("1: Potion", (WIDTH / 3 - 125, HEIGHT * .15), font=30, bg="navy",
                                           feedback="You chose slot Potion")
                    SUPER_POTION_BUTTON = Button("2: Super Potion ", (WIDTH / 3 - 125, HEIGHT * .25), font=30,
                                                 bg="navy", feedback="You chose slot Super Potion")
                    HYPER_POTION_BUTTON = Button("3: Hyper Potion ", (WIDTH / 3 - 125, HEIGHT * .35), font=30,
                                                 bg="navy", feedback="You chose slot Hyper Potion")
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

                    RARE_CANDY_BUTTON = Button("1: Rare Candy ", (WIDTH / 3 - 125, HEIGHT * .15), font=30, bg="navy",
                                               feedback="You chose slot Rare Candy")
                    XL_CANDY_BUTTON = Button("2: XL Candy ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy",
                                             feedback="You chose slot XL Candy")
                    L_CANDY_BUTTON = Button("3: L Candy ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy",
                                            feedback="You chose slot L Candy")
                    M_CANDY_BUTTON = Button("4: M Candy ", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy",
                                            feedback="You chose slot M Candy")
                    S_CANDY_BUTTON = Button("5: S Candy ", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy",
                                            feedback="You chose slot S Candy")
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

                    CALCIUM_BUTTON = Button("1: Calcium ", (WIDTH / 3 - 125, HEIGHT * .15), font=30, bg="navy",
                                            feedback="You chose slot Calcium")
                    CARBOS_BUTTON = Button("2: Carbos ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy",
                                           feedback="You chose slot Carbos")
                    HP_UP_BUTTON = Button("3: HP Up ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy",
                                          feedback="You chose slot HP Up")
                    IRON_BUTTON = Button("4: Iron ", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy",
                                         feedback="You chose slot Iron")
                    PROTEIN_BUTTON = Button("5: Protein ", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy",
                                            feedback="You chose slot Protein")
                    ZINC_BUTTON = Button("6: Zinc ", (WIDTH / 3 - 125, HEIGHT * .65), font=30, bg="navy",
                                         feedback="You chose slot Zinc")
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

                    POKE_BALL_BUTTON = Button("1: Poke Ball ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy",
                                              feedback="You chose slot Poke Ball")
                    GREAT_BALL_BUTTON = Button("2: Great Ball ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy",
                                               feedback="You chose slot Great Ball")
                    ULTRA_BALL_BUTTON = Button("3: Ultra Ball ", (WIDTH / 3 - 125, HEIGHT * .45), font=30, bg="navy",
                                               feedback="You chose slot Ultra Ball")
                    MASTER_BALL_BUTTON = Button("4: Master Ball ", (WIDTH / 3 - 125, HEIGHT * .55), font=30, bg="navy",
                                                feedback="You chose slot Master Ball")
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

        alive_pokemon = 0

        for pokemon in party_slot:
            if pokemon.hp > 0:
                alive_pokemon += 1

        if alive_pokemon == 0:
            print("You Lost!")
            time.sleep(2)
            break

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

        PLAYER_HP = Button(
            "level " + str(party_slot[0].level) + " " + str(party_slot[0].name) + " | HP: " + str(party_slot[0].hp),
            (WIDTH / 3 - 125, HEIGHT * .65), font=25, bg="navy", feedback=party_slot[0].move4.name)
        ENEMY_HP = Button(
            "level " + str(wild_pokemon.level) + " " + str(wild_pokemon.name) + " | HP: " + str(wild_pokemon.hp),
            (WIDTH / 2 + 100, HEIGHT * .15), font=25, bg="navy", feedback=party_slot[0].move4.name)
        TURN_NUM = Button("Turn: " + str(turn_counter), (0, 0), font=30, bg="navy", feedback=str(turn_counter))

        FIGHT_BATTLE_BUTTON.show(FIGHT_BATTLE_BUTTON)
        POKEMON_BATTLE_BUTTON.show(POKEMON_BATTLE_BUTTON)
        ITEMS_BATTLE_BUTTON.show(ITEMS_BATTLE_BUTTON)
        RUN_BATTLE_BUTTON.show(RUN_BATTLE_BUTTON)
        PLAYER_HP.show(PLAYER_HP)
        ENEMY_HP.show(ENEMY_HP)
        TURN_NUM.show(TURN_NUM)

        pygame.display.update()

        if wild_pokemon.hp == 0:
            time.sleep(2)
            break

    wild_pokemon.heal()
