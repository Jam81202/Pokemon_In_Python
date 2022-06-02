import pygame
import os
import time
import random
import sys
import copy
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

    def heal(self):
        self.hp = self.maxhp

    def heal_party(self, player_party):
        for pokemon in player_party:
            pokemon.partypoke_hp = pokemon.partypoke_maxhp

    def get_random_moves(self, attacker, defender):
        random_move = random.randint(1, 4)

        if random_move == 1:
            attacker.move1.attack(attacker.move1, defender, attacker)

        elif random_move == 2:
            attacker.move2.attack(attacker.move2, defender, attacker)

        elif random_move == 3:
            attacker.move3.attack(attacker.move3, defender, attacker)

        elif random_move == 4:
            attacker.move4.attack(attacker.move4, defender, attacker)

    def stat_calc(self, level, stat):
        return int((stat + 1) + (0.4 * level) ** 1.5)

    def add_pokemon(self):
        rand_level = random.randint(1, 60)
        new_poke = Pokemon(self.name, self.poke_img, rand_level, self.stat_calc(rand_level, self.hp), self.stat_calc(rand_level, self.atk),
                           self.stat_calc(rand_level, self.df), self.stat_calc(rand_level, self.spatk), self.stat_calc(rand_level, self.spdf),
                           self.stat_calc(rand_level, self.speed), self.move1, self.move2, self.move3, self.move4)

        return new_poke

    # TODO add levelup function

class Moves:
    def __init__(self, name, atk_type, dmg, accuracy, priority):
        self.name = name
        self.atk_type = atk_type
        self.dmg = dmg
        self.accuracy = accuracy
        self.priority = priority

    def attack(self, move, defender, attacker):
        attack_hit = random.randint(1, 100)
        print(attacker.name + " used " + move.name)

        if attack_hit <= move.accuracy:
            print(attacker.name + ": hit")
            if move.atk_type == "atk":
                damage = 1 + max(0, (move.dmg / 500) * ((2 * attacker.atk) - defender.df))
                defender.hp -= int(damage)
                print("damage:", int(damage))

            elif move.atk_type == "spatk":
                damage = 1 + max(0, (move.dmg / 500) * ((2 * attacker.spatk) - defender.spdf))
                defender.hp -= int(damage)
                print("damage:", int(damage))

            elif move.atk_type == "status":
                if move.name == "Rest":
                    attacker.heal()

        else:
            print(attacker.name + ": Missed")

class Items:
    def __init__(self, name, level_raise, maxhp_raise, heal_amt, atk_raise, df_raise, spatk_raise, spdf_raise, speed_raise, catch_percent=None):
        self.name = name
        self.level_raise = level_raise
        self.maxhp_raise = maxhp_raise
        self.heal_amt = heal_amt
        self.atk_raise = atk_raise
        self.df_raise = df_raise
        self.spatk_raise = spatk_raise
        self.spdf_raise = spdf_raise
        self.speed_raise = speed_raise
        self.catch_percent = catch_percent

    def stat_raise(self, pokemon):
        if self.level_raise > 0:
            pokemon.level += self.level_raise

        elif self.maxhp_raise > 0:
            pokemon.maxhp += self.maxhp_raise

        elif self.heal_amt > 0:
            pokemon.hp += self.heal_amt

        elif self.atk_raise > 0:
            pokemon.atk += self.atk_raise

        elif self.df_raise > 0:
            pokemon.df += self.df_raise

        elif self.spatk_raise > 0:
            pokemon.spatk += self.spatk_raise

        elif self.spdf_raise > 0:
            pokemon.spdf += self.spdf_raise

        elif self.speed_raise > 0:
            pokemon.speed += self.speed_raise

    def catch(self, pokemon, player_party, pc):
        pokemon_caught = random.randint(1, 100)

        if pokemon_caught <= self.catch_percent:
            print("You successfully captured a " + pokemon.name + "!")
            new_poke = Pokemon(pokemon.name, pokemon.poke_img, pokemon.level, pokemon.hp, pokemon.atk, pokemon.df,
                                pokemon.spatk, pokemon.spdf, pokemon.speed, pokemon.move1, pokemon.move2, pokemon.move3, pokemon.move4)

            if len(player_party) < 6:
                player_party.append(new_poke)
                print("Added " + pokemon.name + " to party.")
                return "catch"

            else:
                pc.append(new_poke)
                print("Added " + pokemon.name + " to pc.")
                return "catch"

        else:
            print("You failed to catch " + pokemon.name)
            return "miss"

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
ITEMS_BATTLE_BUTTON = Button("BAG (I)", ((WIDTH/3)-125, HEIGHT * .85), font = 30, bg = "navy", feedback = "check bag")
RUN_BATTLE_BUTTON = Button("RUN (R)", (WIDTH/2+100, HEIGHT * .85), font = 30, bg = "navy", feedback = "you did not get away")

# Items (name, level_raise, maxhp, heal_amt, atk_raise, df_raise, spatk_raise, spdf_raise, speed_raise)
# Healing items
POTION = Items("Potion", 0, 0, 20, 0, 0, 0, 0, 0)
SUPER_POTION = Items("Potion", 0, 0, 60, 0, 0, 0, 0, 0)
HYPER_POTION = Items("Potion", 0, 0, 120, 0, 0, 0, 0, 0)

# Level Items
RARE_CANDY = Items("Rare Candy", 0, 5, 0, 0, 0, 0, 0, 0)
XL_CANDY = Items("Extra Large Candy", 0, 4, 0, 0, 0, 0, 0, 0)
L_CANDY = Items("Large Candy", 0, 3, 0, 0, 0, 0, 0, 0)
M_CANDY = Items("Medium Candy", 0, 2, 0, 0, 0, 0, 0, 0)
S_CANDY = Items("Small Candy", 0, 1, 0, 0, 0, 0, 0, 0)

# Battle Stat Items
CALCIUM = Items("Calcium", 0, 0, 0, 0, 0, 10, 0, 0)
CARBOS = Items("Carbos", 0, 0, 0, 0, 0, 0, 0, 10)
HP_UP = Items("HP Up", 0, 10, 0, 0, 0, 0, 0, 0)
IRON = Items("Iron", 0, 0, 0, 0, 10, 0, 0, 0)
PROTEIN = Items("Protein", 0, 0, 0, 10, 0, 0, 0, 0)
ZINC = Items("Zinc", 0, 0, 0, 0, 0, 0, 10, 0)

# PokeBalls
POKE_BALL = Items("Poke Ball", 0, 0, 0, 0, 0, 0, 0, 0, 25)
GREAT_BALL = Items("Great Ball", 0, 0, 0, 0, 0, 0, 0, 0, 50)
ULTRA_BALL = Items("Ultra Ball", 0, 0, 0, 0, 0, 0, 0, 0, 75)
MASTER_BALL = Items("Master Ball", 0, 0, 0, 0, 0, 0, 0, 0, 100)

ITEM_LIST = [POTION, SUPER_POTION, HYPER_POTION, RARE_CANDY, XL_CANDY, L_CANDY, M_CANDY, S_CANDY, CALCIUM, CARBOS, HP_UP, IRON, PROTEIN, ZINC]

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
ABSORB = Moves("Absorb", "spatk", 20, 100, 2)

# Poison
ACID = Moves("Acid", "spatk", 40, 100, 2)
POISON_STING = Moves("Poison Sting", "atk", 15, 100, 2)
SLUDGE = Moves("Sludge", "spatk", 65, 100, 2)
SMOG = Moves("Smog", "spatk", 30, 70, 2)

# Ground
BONE_CLUB = Moves("Bone Club", "atk", 65, 85, 2)
DIG = Moves("Dig", "atk", 80, 100, 2)
EARTHQUAKE = Moves("Earthquake", "atk", 100, 100, 2)
FISSURE = Moves("Fissure", "atk", 1000000, 30, 2) # This attack 1 hit K.0. if it hits

# Flying
DRILL_PECK = Moves("Drill Peck", "atk", 80, 100, 2)
FLY = Moves("Fly", "atk", 90, 95, 2)
GUST = Moves("Gust", "spatk", 40, 100, 2)
PECK = Moves("Peck", "atk", 35, 100, 2)

# Dragon
DRAGON_RAGE = Moves("Dragon Rage", "spatk", 40, 100, 2) # This move always damages by 40 hp

# Psychic
CONFUSION = Moves("Confusion", "spatk", 50, 100, 2)
PSYBEAM = Moves("Psybeam", "spatk", 65, 100, 2)
PSYCHIC = Moves("Psychic", "spatk", 90, 100, 2)
TELEPORT = Moves("Teleport", "status", 0, 100, 2) # Allows user to flee wild battles
REST = Moves("Rest", "status", 0, 100, 2) # Heals pokemon to full but makes the user fall asleep

# Fighting
DOUBLE_KICK = Moves("Double Kick", "atk", 60, 100, 2)
ROLLING_KICK = Moves("Rolling Kick", "atk", 60, 85, 2)

MOVE_INDEX = [EMPTY, QUICK_ATK, TACKLE, SLAM, SCRATCH, BODY_SLAM, EMBER, FIRE_SPIN, FLAMETHROWER, FIRE_BLAST,
              THUNDER, THUNDER_PUNCH, THUNDER_SHOCK, THUNDERBOLT, BUBBLE, SURF, WATERFALL, WATER_GUN,
              LICK, NIGHT_SHADE, RAZOR_LEAF, MEGA_DRAIN, VINE_WHIP, ABSORB, ACID, POISON_STING, SLUDGE, SMOG,
              BONE_CLUB, DIG, EARTHQUAKE, FISSURE, DRILL_PECK, FLY, GUST, PECK, DRAGON_RAGE,
              CONFUSION, PSYBEAM, PSYCHIC, TELEPORT, REST, DOUBLE_KICK, ROLLING_KICK]

# Pokemon name, poke_img, level, hp, atk, df, spatk, spdf, speed, move1, move2, move3, move4
PIKACHU = Pokemon("Pikachu", PIKA_IMG, 1, 12, 6, 6, 5, 6, 7, QUICK_ATK, TACKLE, THUNDER_SHOCK, FISSURE)
CHARMANDER = Pokemon("Charmander", CHAR_IMG, 1, 12, 6, 6, 5, 6, 6, TACKLE, EMPTY, EMBER, FIRE_SPIN)
TOTODILE = Pokemon("Totodile", TOTODILE_IMG, 1, 12, 6, 6, 5, 6, 6, EMPTY, WATER_GUN, TACKLE, SCRATCH)
BULBASAUR = Pokemon("Bulbasaur", BULB_IMG, 1, 12, 6, 6, 5, 6, 6, RAZOR_LEAF, EMPTY, TACKLE, SLAM)
EEVEE = Pokemon("Eevee", UMB_IMG, 1, 12, 6, 6, 5, 6, 6, EMPTY, TACKLE, QUICK_ATK, SCRATCH)
GENGAR = Pokemon("Gengar", GENGAR_IMG, 1, 12, 6, 6, 6, 6, 7, EMPTY, NIGHT_SHADE, SLUDGE, QUICK_ATK)
CATERPIE = Pokemon("Caterpie", GENGAR_IMG, 1, 12, 5, 6, 4, 5, 6, QUICK_ATK, SCRATCH, TACKLE, EMPTY)
WEEDLE = Pokemon("Weedle", GENGAR_IMG, 1, 12, 6, 5, 4, 5, 6, POISON_STING, SCRATCH, TACKLE, QUICK_ATK)
PIDGEY = Pokemon("Pidgey", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 6, FLY, GUST, TACKLE, QUICK_ATK)
RATTATA = Pokemon("Rattata", GENGAR_IMG, 1, 11, 6, 6, 4, 6, 6, THUNDERBOLT, SCRATCH, TACKLE, QUICK_ATK)
SPEAROW = Pokemon("Spearow", GENGAR_IMG, 1, 12, 6, 5, 4, 5, 6, PECK, DRILL_PECK, GUST, QUICK_ATK)
EKANS = Pokemon("Ekans", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 6, SLUDGE, POISON_STING, ACID, QUICK_ATK)
SANDSHREW = Pokemon("Sandshrew", GENGAR_IMG, 1, 12, 6, 7, 4, 5, 6, POISON_STING, SCRATCH, DIG, EARTHQUAKE)
CLEFAIRY = Pokemon("Clefairy", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 6, PSYCHIC, PSYBEAM, CONFUSION, SLAM)
VULPIX = Pokemon("Vulpix", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 6, EMBER, FLAMETHROWER, FIRE_BLAST, QUICK_ATK)
ZUBAT = Pokemon("Zubat", GENGAR_IMG, 1, 12, 6, 6, 4, 6, 6, ABSORB, POISON_STING, GUST, QUICK_ATK)
ODDISH = Pokemon("Oddish", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 5, ACID, ABSORB, MEGA_DRAIN, POISON_STING)
PSYDUCK = Pokemon("Psyduck", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 6, CONFUSION, SCRATCH, WATER_GUN, BUBBLE)
MANKEY = Pokemon("Mankey", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 6, THUNDER_PUNCH, SCRATCH, ROLLING_KICK, DOUBLE_KICK)
GROWLITHE = Pokemon("Growlithe", GENGAR_IMG, 1, 12, 6, 6, 5, 6, 6, EMBER, FLAMETHROWER, TACKLE, FIRE_SPIN)
ABRA = Pokemon("Abra", GENGAR_IMG, 1, 11, 5, 5, 6, 6, 7, TELEPORT, EMPTY, EMPTY, EMPTY)
SNORLAX = Pokemon("Snorlax", GENGAR_IMG, 1, 14, 7, 6, 5, 7, 5, BODY_SLAM, SCRATCH, TACKLE, REST)
DRAGONITE = Pokemon("Dragonite", GENGAR_IMG, 1, 13, 7, 7, 6, 7, 6, DRAGON_RAGE, FLY, THUNDER_PUNCH, SURF)

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
global pc

PARTY_POKE_1 = Pokemon(GENGAR.name, GENGAR.poke_img, GENGAR.level, GENGAR.hp, GENGAR.atk, GENGAR.df, GENGAR.spatk, GENGAR.spdf, GENGAR.speed, GENGAR.move1, GENGAR.move2, GENGAR.move3, GENGAR.move4)
PARTY_POKE_2 = Pokemon(CHARMANDER.name, CHARMANDER.poke_img, CHARMANDER.level, CHARMANDER.hp, CHARMANDER.atk, CHARMANDER.df, CHARMANDER.spatk, CHARMANDER.spdf, CHARMANDER.speed, CHARMANDER.move1, CHARMANDER.move2, CHARMANDER.move3, CHARMANDER.move4)
PARTY_POKE_3 = Pokemon(TOTODILE.name, TOTODILE.poke_img, TOTODILE.level, TOTODILE.hp, TOTODILE.atk, TOTODILE.df, TOTODILE.spatk, TOTODILE.spdf, TOTODILE.speed, TOTODILE.move1, TOTODILE.move2, TOTODILE.move3, TOTODILE.move4)
PARTY_POKE_4 = Pokemon(BULBASAUR.name, BULBASAUR.poke_img, BULBASAUR.level, BULBASAUR.hp, BULBASAUR.atk, BULBASAUR.df, BULBASAUR.spatk, BULBASAUR.spdf, BULBASAUR.speed, BULBASAUR.move1, BULBASAUR.move2, BULBASAUR.move3, BULBASAUR.move4)
PARTY_POKE_5 = Pokemon(EEVEE.name, EEVEE.poke_img, EEVEE.level, EEVEE.hp, EEVEE.atk, EEVEE.df, EEVEE.spatk, EEVEE.spdf, EEVEE.speed, EEVEE.move1, EEVEE.move2, EEVEE.move3, EEVEE.move4)
PARTY_POKE_6 = Pokemon(PIKACHU.name, PIKACHU.poke_img, PIKACHU.level, PIKACHU.hp, PIKACHU.atk, PIKACHU.df, PIKACHU.spatk, PIKACHU.spdf, PIKACHU.speed, PIKACHU.move1, PIKACHU.move2, PIKACHU.move3, PIKACHU.move4)

party_slot = [PARTY_POKE_1, PARTY_POKE_2, PARTY_POKE_3, PARTY_POKE_4, PARTY_POKE_5, PARTY_POKE_6]
PC_STORAGE = []

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

    party_slot_img_right = Player(WIDTH / 2 - 125, HEIGHT / 2 - 50)
    party_slot_img_left = Player(WIDTH / 2 + 25, HEIGHT / 2 -50)
    party_slot_img_down = Player(WIDTH / 2 - 50, HEIGHT / 2 - 125)
    party_slot_img_up = Player(WIDTH / 2 - 50, HEIGHT / 2 + 25)

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

    def battle():
        battling = True
        wild_pokemon = random.choice(POKE_DEX)
        wild_pokemon = wild_pokemon.add_pokemon()
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
                        SUPER_POTION_BUTTON = Button("2: Super Potion ", (WIDTH / 2 + 100, HEIGHT * .15), font=30, bg="navy", feedback="You chose slot Super Potion")
                        HYPER_POTION_BUTTON = Button("3: Hyper Potion ", (WIDTH / 3 - 125, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Hyper Potion")
                        BACK_BUTTON = Button("<-- Back", (WIDTH / 2 + 100, HEIGHT * .35), font=30, bg="navy", feedback="You chose to go back")

                        POTION_BUTTON.show(POTION_BUTTON)
                        SUPER_POTION_BUTTON.show(SUPER_POTION_BUTTON)
                        HYPER_POTION_BUTTON.show(HYPER_POTION_BUTTON)
                        BACK_BUTTON.show(BACK_BUTTON)

                        pygame.display.update()

                def level_items_menu():
                    while True:
                        WIN.fill(BLACK)

                        RARE_CANDY_BUTTON = Button("1: Rare Candy ", (WIDTH / 2 + 100, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Rare Candy")
                        XL_CANDY_BUTTON = Button("2: XL Candy ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot XL Candy")
                        L_CANDY_BUTTON = Button("3: L Candy ", (WIDTH / 2 + 100, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot L Candy")
                        M_CANDY_BUTTON = Button("4: M Candy ", (WIDTH / 2 + 100, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot M Candy")
                        S_CANDY_BUTTON = Button("5: S Candy ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot S Candy")
                        BACK_BUTTON = Button("<-- Back", (WIDTH / 2 + 100, HEIGHT * .35), font=30, bg="navy", feedback="You chose to go back")



                        RARE_CANDY_BUTTON.show(RARE_CANDY_BUTTON)
                        XL_CANDY_BUTTON.show(XL_CANDY_BUTTON)
                        L_CANDY_BUTTON.show(L_CANDY_BUTTON)
                        M_CANDY_BUTTON.show(M_CANDY_BUTTON)
                        S_CANDY_BUTTON.show(S_CANDY_BUTTON)
                        BACK_BUTTON.show(BACK_BUTTON)

                def stat_items_menu():
                    while True:
                        WIN.fill(BLACK)

                        CALCIUM_BUTTON = Button("1: Calcium ", (WIDTH / 2 + 100, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot Calcium")
                        CARBOS_BUTTON = Button("2: Carbos ", (WIDTH / 2 + 100, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Carbos")
                        HP_UP_BUTTON = Button("3: HP Up ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot HP Up")
                        IRON_BUTTON = Button("4: Iron ", (WIDTH / 2 + 100, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot Iron")
                        PROTEIN_BUTTON = Button("5: Protein ", (WIDTH / 2 + 100, HEIGHT * .25), font=30, bg="navy", feedback="You chose slot Protein")
                        ZINC_BUTTON = Button("6: Zinc ", (WIDTH / 3 - 125, HEIGHT * .35), font=30, bg="navy", feedback="You chose slot Zinc")
                        BACK_BUTTON = Button("<-- Back", (WIDTH / 2 + 100, HEIGHT * .35), font=30, bg="navy", feedback="You chose to go back")

                        CALCIUM_BUTTON.show(CALCIUM_BUTTON)
                        CARBOS_BUTTON.show(CARBOS_BUTTON)
                        HP_UP_BUTTON.show(HP_UP_BUTTON)
                        IRON_BUTTON.show(IRON_BUTTON)
                        PROTEIN_BUTTON.show(PROTEIN_BUTTON)
                        ZINC_BUTTON.show(ZINC_BUTTON)
                        BACK_BUTTON.show(BACK_BUTTON)

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
                            break

                        if keys[pygame.K_1]:
                            if POKE_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            break

                        if keys[pygame.K_2]:
                            if GREAT_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            break

                        if keys[pygame.K_3]:
                            if ULTRA_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            break

                        if keys[pygame.K_4]:
                            if MASTER_BALL.catch(wild_pokemon, party_slot, PC_STORAGE) == "catch":
                                wild_pokemon.hp = 0
                            break


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
                    break

                if keys[pygame.K_z]:
                    potions_menu()
                    break

                if keys[pygame.K_x]:
                    level_items_menu()
                    break

                if keys[pygame.K_c]:
                    stat_items_menu()
                    break

                if keys[pygame.K_v]:
                    poke_balls_menu()
                    break

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
                if party_slot[1].hp <= 0:
                    if party_slot[2].hp <= 0:
                        if party_slot[3].hp <= 0:
                            if party_slot[4].hp <= 0:
                                if party_slot[5].hp <= 0:
                                    print("You Lost!")
                                    break

            if party_slot[0].hp <= 0:
                party_slot[0].hp += abs(party_slot[0].hp)
                print("Your", party_slot[0].name, "has fainted!")

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
                party()
                wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])
                turn_counter += 1

            if keys[pygame.K_i]:
                bag()

                if wild_pokemon.hp > 0:
                    wild_pokemon.get_random_moves(wild_pokemon, party_slot[0])

                time.sleep(1)
                turn_counter += 1

            if keys[pygame.K_r]:
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

            if party_slot[0].hp == 0:
                time.sleep(2)
                party()

            if wild_pokemon.hp == 0:
                time.sleep(2)
                break

        wild_pokemon.heal()

    def inventory():
        pass

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

        redraw_window()

main()

