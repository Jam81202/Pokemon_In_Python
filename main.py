import pygame
import os
import time
import random
import sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 650
BG_W, BG_H = 6000, 5450
SPRITE_W, SPRITE_H = 65, 65
WIN = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Borpa")

FONT = pygame.font.SysFont("comicsans", 16)

'''Things with images'''
# Map
PALLET_TOWN = pygame.transform.scale(pygame.image.load(os.path.join("assets", "world_map.png")), (BG_W, BG_H))
VERMILION_CITY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "vermilion_city.png")), (1500, 1404))

# Pokemon
PIKA_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Pika.png")), (SPRITE_W, SPRITE_H))
CHAR_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "char.png")), (SPRITE_W, SPRITE_H))
BULB_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bulb.png")), (SPRITE_W, SPRITE_H))
UMB_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "umb.png")), (SPRITE_W, SPRITE_H))
GENGAR_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "gengar.png")), (SPRITE_W, SPRITE_H))
TOTODILE_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "totodile.png")), (SPRITE_W, SPRITE_H))

# Trainer
TRAINER_DOWN_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "trainer_down.png")), (SPRITE_W,SPRITE_H))
TRAINER_UP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "trainer_up.png")), (SPRITE_W,SPRITE_H))
TRAINER_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "trainer_left.png")), (SPRITE_W,SPRITE_H))
TRAINER_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "trainer_right.png")), (SPRITE_W,SPRITE_H))

RUN_RIGHT_ANIMATION = [CHAR_IMG, PIKA_IMG]
RUN_LEFT_ANIMATION = [BULB_IMG, UMB_IMG]

# Battle start animation
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Pokemon:
    def __init__(self, name, poke_img, level, hp, atk, df, spatk, spdf, speed, move1, move2, move3, move4):
        self.name = name
        self.poke_img = poke_img
        self.level = level
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spatk = spatk
        self.spdf = spdf
        self.speed = speed
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.maxhp = hp

        self.partypoke_level = level
        self.partypoke_hp = hp
        self.partypoke_maxhp = self.maxhp
        self.partypoke_atk = atk
        self.partypoke_df = df
        self.partypoke_spatk = spatk
        self.partypoke_spdf = spdf
        self.partypoke_speed = speed
        self.partypoke_move1 = move1
        self.partypoke_move2 = move2
        self.partypoke_move3 = move3
        self.partypoke_move4 = move4

    def heal(self, pokemon):
        pokemon.hp = pokemon.maxhp

    def get_random_moves(self, attacker, defender):
        random_move = random.randint(1, 4)

        if random_move == 1:
            attacker.move1.attack(attacker.move1, defender, attacker)

            print(attacker.name + " used " + attacker.move1.name)

        if random_move == 2:
            attacker.move2.attack(attacker.move2, defender, attacker)

            print(attacker.name + " used " + attacker.move2.name)

        if random_move == 3:
            attacker.move3.attack(attacker.move3, defender, attacker)

            print(attacker.name + " used " + attacker.move3.name)

        if random_move == 4:
            attacker.move4.attack(attacker.move4, defender, attacker)

            print(attacker.name + " used " + attacker.move4.name)

class Moves:
    def __init__(self, name, atk_type, dmg, accuracy, priority):
        self.name = name
        self.atk_type = atk_type
        self.dmg = dmg
        self.accuracy = accuracy
        self.priority = priority

    def attack(self, move, defender, attacker):
        if move.atk_type == "atk":
            defender.hp = int(defender.hp - (move.dmg * (attacker.atk / 200)))

        elif move.atk_type == "spatk":
            defender.hp = int(defender.hp - (move.dmg * (attacker.spatk / 200)))

class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, button):
        WIN.blit(button.surface, (self.x, self.y))

    def show_feedback(self, button):
        return button.feedback

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = PIKA_IMG

    def draw(self, window, img):
        window.blit(img, (self.x, self.y))

class Background():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = PALLET_TOWN

    def draw(self, window, img):
        window.blit(img, (self.x, self.y))


FIGHT_BATTLE_BUTTON = Button("FIGHT (F)", ((WIDTH/3)-125, HEIGHT * .75), font = 30, bg = "navy", feedback = "start fight")
POKEMON_BATTLE_BUTTON = Button("POKEMON (P)", (WIDTH/2+100, HEIGHT * .75), font = 30, bg = "navy", feedback = "view party")
ITEMS_BATTLE_BUTTON = Button("BAG (B)", ((WIDTH/3)-125, HEIGHT * .85), font = 30, bg = "navy", feedback = "check bag")
RUN_BATTLE_BUTTON = Button("RUN (R)", (WIDTH/2+100, HEIGHT * .85), font = 30, bg = "navy", feedback = "you did not get away")

# Moves (name, attack type, damage, accuracy, priority)
EMPTY = Moves("Empty", "atk", 0, 0, 2) # Use this move to show you don't have a move in that slot

# Normal
QUICK_ATK = Moves("Quick Attack", "atk", 40, 100, 1)
TACKLE = Moves("Tackle", "atk", 40, 100, 2)
SLAM = Moves("Slam", "atk", 80, 75, 2)
SCRATCH = Moves("Scratch", "atk", 40, 100, 2)
BODY_SLAM = Moves("Body Slam", "atk", 85, 100, 2)

# Fire
EMBER = Moves("Ember", "spatk", 40, 100, 2)
FIRE_SPIN = Moves("Fire Spin", "spatk", 35, 95, 2)
FLAMETHROWER = Moves("Flamethrower", "apatk", 90, 100, 2)
FIRE_BLAST = Moves("Fire Blast", "spatk", 110, 85, 2)

# Electric
THUNDER_SHOCK = Moves("Thunder Shock", "spatk", 40, 100, 2)
THUNDER = Moves("Thunder", "spatk", 110, 70, 2)
THUNDER_PUNCH = Moves("Thunder Punch", "atk", 75, 100, 2)
THUNDERBOLT = Moves("Thunderbolt", "spatk", 90, 100, 2)

# Water
WATER_GUN = Moves("Water Gun", "atk", 40, 100, 2)
BUBBLE = Moves("Bubble", "spatk", 40, 100, 2)
WATERFALL = Moves("Waterfall", "atk", 80, 100, 2)
SURF = Moves("Surf", "spatk", 90, 100, 2)

# Ghost
LICK = Moves("Lick", "atk", 30, 100, 2)
NIGHT_SHADE = Moves("Night Shade", "spatk", 0, 100, 2) # Damage = user level

# Grass
RAZOR_LEAF = Moves("Razor Leaf", "atk", 55, 95, 2)
MEGA_DRAIN = Moves("Mega Drain", "spatk", 40, 100, 2)
VINE_WHIP = Moves("Vine Whipe", "atk", 45, 100, 2)
ABSORB = Moves("Absorb", "apatk", 20, 100, 2)

# Poison
ACID = Moves("Acid", "spatk", 40, 100, 2)
POISON_STING = Moves("Poison Sting", "atk", 15, 100, 2)
SLUDGE = Moves("Sludge", "spatk", 65, 100, 2)
SMOG = Moves("Smog", "spatk", 30, 70, 2)

# Ground
BONE_CLUB = Moves("Bone Club", "atk", 65, 85, 2)
DIG = Moves("Dig", "atk", 80, 100, 2)
EARTHQUAKE = Moves("Earthquake", "atk", 100, 100, 2)
FISSURE = Moves("Fissure", "atk", 0, 30, 2) # This attack 1 hit K.0. if it hits

# Flying
DRILL_PECK = Moves("Drill Peck", "atk", 80, 100, 2)
FLY = Moves("Fly", "atk", 90, 95, 2)
GUST = Moves("Gust", "apatk", 40, 100, 2)
PECK = Moves("Peck", "atk", 35, 100, 2)

# Dragon
DRAGON_RAGE = Moves("Dragon Rage", "spatk", 0, 100, 2) # This move always damages by 40 hp

# Psychic
CONFUSION = Moves("Confusion", "spatk", 50, 100, 2)
PSYBEAM = Moves("Psybeam", "spatk", 65, 100, 2)
PSYCHIC = Moves("Psychic", "spatk", 90, 100, 2)
TELEPORT = Moves("Teleport", "status", 0, 100, 2) # Allows user to flee wild battles
REST = Moves("Rest", "status", 0, 0, 2)

# Fighting
DOUBLE_KICK = Moves("Double Kick", "atk", 60, 100, 2)
ROLLING_KICK = Moves("Rolling Kick", "atk", 60, 85, 2)

MOVE_INDEX = [EMPTY, QUICK_ATK, TACKLE, SLAM, SCRATCH, BODY_SLAM, EMBER, FIRE_SPIN, FLAMETHROWER, FIRE_BLAST,
              THUNDER, THUNDER_PUNCH, THUNDER_SHOCK, THUNDERBOLT, BUBBLE, SURF, WATERFALL, WATER_GUN,
              LICK, NIGHT_SHADE, RAZOR_LEAF, MEGA_DRAIN, VINE_WHIP, ABSORB, ACID, POISON_STING, SLUDGE, SMOG,
              BONE_CLUB, DIG, EARTHQUAKE, FISSURE, DRILL_PECK, FLY, GUST, PECK, DRAGON_RAGE,
              CONFUSION, PSYBEAM, PSYCHIC, TELEPORT, REST, DOUBLE_KICK, ROLLING_KICK]

# Pokemon name, poke_img, level, hp, atk, df, spatk, spdf, speed, move1, move2, move3, move4
PIKACHU = Pokemon("Pikachu", PIKA_IMG, 5, 35, 55, 40, 50, 50, 90, QUICK_ATK, TACKLE, THUNDER_SHOCK, EMPTY)
CHARMANDER = Pokemon("Charmander", CHAR_IMG, 5, 39, 52, 43, 60, 50, 65, TACKLE, EMPTY, EMBER, FIRE_SPIN)
TOTODILE = Pokemon("Totodile", TOTODILE_IMG, 5, 50, 65, 64, 44, 48, 43, EMPTY, WATER_GUN, TACKLE, SCRATCH)
BULBASAUR = Pokemon("Bulbasaur", BULB_IMG, 5, 45, 49, 49, 65, 65, 45, RAZOR_LEAF, EMPTY, TACKLE, SLAM)
EEVEE = Pokemon("Eevee", UMB_IMG, 5, 95, 65, 110, 60, 130, 65, EMPTY, TACKLE, QUICK_ATK, SCRATCH)
GENGAR = Pokemon("Gengar", GENGAR_IMG, 5, 60, 65, 60, 130, 75, 110, EMPTY, NIGHT_SHADE, SLUDGE, QUICK_ATK)
CATERPIE = Pokemon("Caterpie", GENGAR_IMG, 5, 45, 30, 35, 20, 20, 45, QUICK_ATK, SCRATCH, TACKLE, EMPTY)
WEEDLE = Pokemon("Weedle", GENGAR_IMG, 5, 40, 35, 30, 20, 20, 50, POISON_STING, SCRATCH, TACKLE, QUICK_ATK)
PIDGEY = Pokemon("Pidgey", GENGAR_IMG, 5, 40, 45, 40, 35, 35, 56, FLY, GUST, TACKLE, QUICK_ATK)
RATTATA = Pokemon("Rattata", GENGAR_IMG, 5, 30, 56, 35, 25, 35, 72, THUNDERBOLT, SCRATCH, TACKLE, QUICK_ATK)
SPEAROW = Pokemon("Spearow", GENGAR_IMG, 5, 40, 60, 30, 31, 31, 70, PECK, DRILL_PECK, GUST, QUICK_ATK)
EKANS = Pokemon("Ekans", GENGAR_IMG, 5, 35, 60, 44, 40, 54, 55, SLUDGE, POISON_STING, ACID, QUICK_ATK)
SANDSHREW = Pokemon("Sandshrew", GENGAR_IMG, 5, 50, 75, 85, 20, 30, 40, POISON_STING, SCRATCH, DIG, EARTHQUAKE)
CLEFAIRY = Pokemon("Clefairy", GENGAR_IMG, 5, 70, 45, 48, 60, 65, 35, PSYCHIC, PSYBEAM, CONFUSION, SLAM)
VULPIX = Pokemon("Vulpix", GENGAR_IMG, 5, 38, 41, 40, 50, 65, 65, EMBER, FLAMETHROWER, FIRE_BLAST, QUICK_ATK)
ZUBAT = Pokemon("Zubat", GENGAR_IMG, 5, 40, 45, 35, 30, 40, 55, ABSORB, POISON_STING, GUST, QUICK_ATK)
ODDISH = Pokemon("Oddish", GENGAR_IMG, 5, 45, 50, 55, 75, 65, 30, ACID, ABSORB, MEGA_DRAIN, POISON_STING)
PSYDUCK = Pokemon("Psyduck", GENGAR_IMG, 5, 50, 52, 48, 65, 50, 55, CONFUSION, SCRATCH, WATER_GUN, BUBBLE)
MANKEY = Pokemon("Mankey", GENGAR_IMG, 5, 40, 80, 35, 35, 45, 70, THUNDER_PUNCH, SCRATCH, ROLLING_KICK, DOUBLE_KICK)
GROWLITHE = Pokemon("Growlithe", GENGAR_IMG, 5, 55, 70, 45, 70, 50, 60, EMBER, FLAMETHROWER, TACKLE, FIRE_SPIN)
ABRA = Pokemon("Abra", GENGAR_IMG, 5, 25, 20, 15, 105, 55, 90, TELEPORT, EMPTY, EMPTY, EMPTY)
SNORLAX = Pokemon("Snorlax", GENGAR_IMG, 5, 160, 110, 65, 65, 110, 30, BODY_SLAM, SCRATCH, TACKLE, REST)
DRAGONITE = Pokemon("Dragonite", GENGAR_IMG, 5, 91, 134, 95, 100, 100, 80, DRAGON_RAGE, FLY, THUNDER_PUNCH, SURF)

POKE_DEX = [PIKACHU, CHARMANDER, TOTODILE, BULBASAUR, EEVEE, GENGAR, CATERPIE, WEEDLE, WEEDLE, PIDGEY,
            RATTATA, SPEAROW, EKANS, SANDSHREW, CLEFAIRY, VULPIX, ZUBAT, ODDISH, PSYDUCK, MANKEY, GROWLITHE,
            ABRA, SNORLAX, DRAGONITE]


# Party Pokemon (poke_name, poke_img, level, hp, atk, df, spatk, spdf, speed, move1, move2, move3, move4)
global PARTY_POKE_1
global PARTY_POKE_2
global PARTY_POKE_3
global PARTY_POKE_4
global PARTY_POKE_5
global PARTY_POKE_6
global party

PARTY_POKE_1 = PIKACHU
PARTY_POKE_2 = CHARMANDER
PARTY_POKE_3 = TOTODILE
PARTY_POKE_4 = BULBASAUR
PARTY_POKE_5 = EEVEE
PARTY_POKE_6 = GENGAR

party_slot = [PARTY_POKE_1, PARTY_POKE_2, PARTY_POKE_3, PARTY_POKE_4, PARTY_POKE_5, PARTY_POKE_6]

left = False
right = False
up = False
down = False
step_counter = 0

def main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60

    velocity = 7
    player = Player(WIDTH/2-50, HEIGHT/2-50)

    pallet_town = Background(0-(BG_W * .015), 0-(BG_H/2))

    global step_counter, left, right

    if step_counter > 1:
        step_counter = 0

    def redraw_window():
        WIN.fill(BLACK)
        pallet_town.draw(WIN, PALLET_TOWN)

        player.draw(WIN, TRAINER_DOWN_IMG)

        if left:
            player.draw(WIN, TRAINER_RIGHT_IMG)
            # step_counter += 1

        if right:
            player.draw(WIN, TRAINER_LEFT_IMG)

        if up:
            player.draw(WIN, TRAINER_DOWN_IMG)

        if down:
            player.draw(WIN, TRAINER_UP_IMG)

        pygame.display.update()

    def battle():
        battling = True
        wild_pokemon = random.choice(POKE_DEX)

        def fight():
            selecting = True
            while selecting:
                WIN.fill(BLACK)

                # Fight Buttons
                MOVE_1_BUTTON = Button("1: " + party_slot[0].move1.name, (WIDTH / 3 - 125, HEIGHT * .75), font=30,
                                       bg="navy", feedback=party_slot[0].move1.name)
                MOVE_2_BUTTON = Button("2: " + party_slot[0].move2.name, (WIDTH / 2 + 100, HEIGHT * .75), font=30,
                                       bg="navy", feedback=party_slot[0].move2.name)
                MOVE_3_BUTTON = Button("3: " + party_slot[0].move3.name, (WIDTH / 3 - 125, HEIGHT * .85), font=30,
                                       bg="navy", feedback=party_slot[0].move3.name)
                MOVE_4_BUTTON = Button("4: " + party_slot[0].move4.name, (WIDTH / 2 + 100, HEIGHT * .85), font=30,
                                       bg="navy", feedback=party_slot[0].move4.name)

                PLAYER_HP = Button(str(party_slot[0].name) + " " + str(party_slot[0].hp), (WIDTH / 3 - 125, HEIGHT * .65), font=30,
                                       bg="navy", feedback=party_slot[0].move4.name)

                ENEMY_HP = Button(str(wild_pokemon.name) + " " + str(wild_pokemon.hp), (WIDTH / 2 + 100, HEIGHT * .15), font=30,
                                   bg="navy", feedback=party_slot[0].move4.name)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    print(party_slot[0].name + " used " + MOVE_1_BUTTON.show_feedback(MOVE_1_BUTTON))
                    party_slot[0].move1.attack(party_slot[0].move1, wild_pokemon, party_slot[0])
                    wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
                    break

                if keys[pygame.K_2]:
                    print(party_slot[0].name + " used " + MOVE_2_BUTTON.show_feedback(MOVE_2_BUTTON))
                    party_slot[0].move2.attack(party_slot[0].move2, wild_pokemon, party_slot[0])
                    wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
                    break

                if keys[pygame.K_3]:
                    print(party_slot[0].name + " used " + MOVE_3_BUTTON.show_feedback(MOVE_3_BUTTON))
                    party_slot[0].move3.attack(party_slot[0].move3, wild_pokemon, party_slot[0])
                    wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
                    break

                if keys[pygame.K_4]:
                    print(party_slot[0].name + " used " + MOVE_4_BUTTON.show_feedback(MOVE_4_BUTTON))
                    party_slot[0].move4.attack(party_slot[0].move4, wild_pokemon, party_slot[0])
                    wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
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
                PARTY_SLOT_1_BUTTON = Button("1: " + party_slot[0].name, (WIDTH / 3 - 125, HEIGHT * .15), font=30,
                                             bg="navy", feedback="You chose slot 1")
                PARTY_SLOT_2_BUTTON = Button("2: " + party_slot[1].name, (WIDTH / 2 + 100, HEIGHT * .15), font=30,
                                             bg="navy", feedback="You chose slot 2")
                PARTY_SLOT_3_BUTTON = Button("3: " + party_slot[2].name, (WIDTH / 3 - 125, HEIGHT * .25), font=30,
                                             bg="navy", feedback="You chose slot 3")
                PARTY_SLOT_4_BUTTON = Button("4: " + party_slot[3].name, (WIDTH / 2 + 100, HEIGHT * .25), font=30,
                                             bg="navy", feedback="You chose slot 4")
                PARTY_SLOT_5_BUTTON = Button("5: " + party_slot[4].name, (WIDTH / 3 - 125, HEIGHT * .35), font=30,
                                             bg="navy", feedback="You chose slot 5")
                PARTY_SLOT_6_BUTTON = Button("6: " + party_slot[5].name, (WIDTH / 2 + 100, HEIGHT * .35), font=30,
                                             bg="navy", feedback="You chose slot 6")

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    print(PARTY_SLOT_1_BUTTON.show_feedback(PARTY_SLOT_1_BUTTON))
                    break

                if keys[pygame.K_2]:
                    print(PARTY_SLOT_2_BUTTON.show_feedback(PARTY_SLOT_2_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[1]
                    party_slot[1] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    break

                if keys[pygame.K_3]:
                    print(PARTY_SLOT_3_BUTTON.show_feedback(PARTY_SLOT_3_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[2]
                    party_slot[2] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    break

                if keys[pygame.K_4]:
                    print(PARTY_SLOT_4_BUTTON.show_feedback(PARTY_SLOT_4_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[3]
                    party_slot[3] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    break

                if keys[pygame.K_5]:
                    print(PARTY_SLOT_5_BUTTON.show_feedback(PARTY_SLOT_5_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[4]
                    party_slot[4] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    break

                if keys[pygame.K_6]:
                    print(PARTY_SLOT_6_BUTTON.show_feedback(PARTY_SLOT_6_BUTTON))
                    temp = party_slot[0]
                    party_slot[0] = party_slot[5]
                    party_slot[5] = temp

                    if party_slot[0].hp <= 0:
                        print("You must pick a conscious pokemon")
                        party()

                    break

                PARTY_SLOT_1_BUTTON.show(PARTY_SLOT_1_BUTTON)
                PARTY_SLOT_2_BUTTON.show(PARTY_SLOT_2_BUTTON)
                PARTY_SLOT_3_BUTTON.show(PARTY_SLOT_3_BUTTON)
                PARTY_SLOT_4_BUTTON.show(PARTY_SLOT_4_BUTTON)
                PARTY_SLOT_5_BUTTON.show(PARTY_SLOT_5_BUTTON)
                PARTY_SLOT_6_BUTTON.show(PARTY_SLOT_6_BUTTON)

                pygame.display.update()

        def bag():
            pass

        def run():
            return random.randint(1, 10)

        while battling:
            WIN.fill(BLACK)

            if wild_pokemon.hp <= 0:
                print("You Won!")
                break

            if party_slot[0].hp <= 0:
                if party_slot[1].hp <= 0:
                    if party_slot[2].hp <= 0:
                        if party_slot[3].hp <= 0:
                            if party_slot[4].hp <= 0:
                                if party_slot[5].hp <= 0:
                                    print("You Lost!")
                                    break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                fight()

            if keys[pygame.K_p]:
                party()

            if keys[pygame.K_b]:
                bag()

            if keys[pygame.K_r]:
                run_away = run()
                if run_away < 8:
                    print("you ran away")
                    time.sleep(1)
                    break

                elif run_away > 7:
                    print("you did not run away")
                    time.sleep(1)

            FIGHT_BATTLE_BUTTON.show(FIGHT_BATTLE_BUTTON)
            POKEMON_BATTLE_BUTTON.show(POKEMON_BATTLE_BUTTON)
            ITEMS_BATTLE_BUTTON.show(ITEMS_BATTLE_BUTTON)
            RUN_BATTLE_BUTTON.show(RUN_BATTLE_BUTTON)

            pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            pallet_town.x -= velocity
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_a]:
            pallet_town.x += velocity
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_s]:
            pallet_town.y -= velocity
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_w]:
            pallet_town.y += velocity
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

        else:
            left = False
            right = False
            up = False
            down = False

        redraw_window()

main()